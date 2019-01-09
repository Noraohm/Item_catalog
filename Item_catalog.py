from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from Itemcatalog_db import Base, MovieType, MoviePage, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response, flash
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Upcoming movies"


# Connect to sqlite Database and create database for the project
engine = create_engine('sqlite:///Movie_page.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Log in path
@app.route('/login')
def showLogin():
    '''  defined showlogin to create the state'''
    state = ''.join(
                    random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():

    '''    start of google connect Oauth  '''
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
                                 json.dumps('''Failed to upgrade
                                            the authorization code.'''), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parse response
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
                                 json.dumps('''Token's user ID
                                 doesn't match given user ID.'''), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
                                 json.dumps('Current user is already connected'
                                            ), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't there, create new user
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ''' " style = "width: 300px; height: 300px;border-radius: 150px;
    -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '''
    flash("you are now logged in as %s" % login_session['username'])
    return output


def createUser(login_session):

    '''   This function to create the new user     '''
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    '''      To get the User info from the Database     '''
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    """  To get & view the user ID   """
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


@app.route('/gdisconnect')
def gdisconnect():
    """disconnect the current user & reset their login_session """

    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's session.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # error message to Appear when the user logout failed.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/Mainpage/<int:movietype_id>/list/JSON')
def MainTypePageJSON(movietype_id):

    """ Json Format  """
    movietype = session.query(MovieType).filter_by(id=movietype_id).one()
    movielist = session.query(MoviePage).filter_by(
        movietype_id=movietype_id).all()
    return jsonify(MoviePage=[i.serialize for i in movielist])


@app.route('/Mainpage/<int:movietype_id>/list/JSON')
def movieListJSON(movietype_id, list_id):
    """ Json Format  """
    movielist = session.query(MoviePage).filter_by(id=list_id).one()
    return jsonify(MoviePage=movielist.serialize)


@app.route('/')
@app.route('/Mainpage/')
def MainTypePage():
    """ This Function to show the Movie Genre page """
    movietype = session.query(MovieType).all()
    if 'username' not in login_session:
        return render_template('publicMainPage.html', movietype=movietype)
    else:
        return render_template('Mainpage.html', movietype=movietype)


@app.route('/Mainpage/<int:movietype_id>/list')
def movieList(movietype_id):
    """The Function is to show movie list page As per the(MovieType ID)"""
    movietype = session.query(MovieType).filter_by(id=movietype_id).one()
    movielist = session.query(MoviePage).filter_by(
                                         movietype_id=movietype_id).all()
    if 'username' not in login_session:
        return render_template('publicMovieCenter.html',
                               movietype=movietype,
                               movielist=movielist)
    else:
        return render_template(
                               'movie_center.html',
                               movietype=movietype,
                               movielist=movielist)


@app.route('/Mainpage/<int:movietype_id>/new', methods=['GET', 'POST'])
def newMovie(movietype_id):
    """This Function to Add the new Movie to the list  """
    if 'username' not in login_session:
        return redirect('/login')
    movietype = session.query(MovieType).filter_by(id=movietype_id).one()
    if request.method == 'POST':
        newMovie = MoviePage(
                           name=request.form['name'],
                           Storyline=request.form['Storyline'],
                           link=request.form['link'],
                           Director=request.form['Director'],
                           stars=request.form['stars'],
                           release=request.form['release'],
                           movietype_id=movietype_id,
                           user_id=movietype.user_id)
        session.add(newMovie)
        session.commit()
        return redirect(url_for('movieList', movietype_id=movietype_id))
    else:
        return render_template('newMovie.html', movietype_id=movietype_id)


@app.route(
           '/Mainpage/<int:movietype_id>/<int:list_id>/edit',
           methods=['GET', 'POST'])
def editMovieList(movietype_id, list_id):
    """ This Function to Edit the current movie list """
    if 'username' not in login_session:
        return redirect('/login')
    editmovielist = session.query(MoviePage).filter_by(id=list_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editmovielist.name = request.form['name']
        if request.form['Storyline']:
            editmovielist.Storyline = request.form['Storyline']
        if request.form['link']:
            editmovielist.link = request.form['link']
        if request.form['Director']:
            editmovielist.Director = request.form['Director']
        if request.form['stars']:
            editmovielist.stars = request.form['stars']
        if request.form['release']:
            editmovielist.release = request.form['release']
        session.add(editmovielist)
        session.commit()
        return redirect(url_for('movieList', movietype_id=movietype_id))
    else:
        return render_template('editMovie.html', movietype_id=movietype_id,
                               list_id=list_id, Mlist=editmovielist)


@app.route(
           '/Mainpage/<int:movietype_id>/<int:list_id>/delete',
           methods=['GET', 'POST'])
def deleteMovieList(movietype_id, list_id):
    """ This Function to delete the current Movie """
    if 'username' not in login_session:
        return redirect('/login')
    deletemovie = session.query(MoviePage).filter_by(id=list_id).one()
    if request.method == 'POST':
        session.delete(deletemovie)
        session.commit()
        return redirect(url_for('movieList', movietype_id=movietype_id))
    else:
        return render_template('deleteMovie.html', Mlist=deletemovie)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
