#!/usr/bin/python
# -*- coding: <encoding name> -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Itemcatalog_db import MovieType, Base, MoviePage,User

engine = create_engine("sqlite:///Movie_page.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

User1 = User(name="Nora Motairy", email="damo3ah@gmail.com",
             picture='https://lh3.googleusercontent.com/-R09k1uj_hGE/VLZpOkWb8KI/AAAAAAAAAHc/peF35Y_iXfYZddagR1JYuf4OHkkZhHCqQCEwYBhgL/w140-h140-p/20130619_151151.jpg')
session.add(User1)
session.commit()

#first Genre
movietype1 = MovieType(name = "Comedy",user_id=1)

session.add(movietype1)
session.commit()


Moviepage1 = MoviePage(name = "Fighting with My Family",
                       Storyline = '''A former wrestler and his family make a living performing at small venues around the country while his kids dream of joining World Wrestling Entertainment.''',
                       link= "https://www.youtube.com/embed/I-X5WnMzOvA", Director = "Stephen Merchant", stars = "Florence Pugh, Dwayne Johnson, Lena Headey",
                       release = "14 February 2019",user_id=1, movietype = movietype1)

session.add(Moviepage1)
session.commit()

Moviepage2 = MoviePage(name = "A Madea Family Funeral", Storyline = '''A joyous family reunion becomes a hilarious nightmare as Madea and the crew travel to backwoods Georgia,
where they find themselves unexpectedly planning a funeral that might unveil unsavory family secrets.''', link= "https://www.youtube.com/embed/RaA9elSYnpQ",
                       Director = "Tyler Perry",stars = "Courtney Burrell, Tyler Perry, Patrice Lovely", release = "1 March 2019", user_id=1,movietype = movietype1)

session.add(Moviepage2)
session.commit()

Moviepage3 = MoviePage(name = "What Men Want (2019)",
                       Storyline = "A woman is boxed out by the male sports agents in her profession, but gains an unexpected edge over them when she develops the ability to hear their thoughts.",
                       link= "https://www.youtube.com/embed/HeoLiTirRp4", Director = "Adam Shankman",stars = "Taraji P. Henson, Wendi McLendon-Covey, Pete Davidson",
                       release = "8 February 2019",user_id=1, movietype = movietype1)

session.add(Moviepage3)
session.commit()


#second Genre
movietype2 = MovieType(name = "Animation",user_id=1)

session.add(movietype2)
session.commit()

Moviepage1 = MoviePage(name = "Spies in Disguise", Storyline = '''When the world's best spy is turned into a pigeon, he must rely on his nerdy tech officer to save the world.''',
                       link= "https://www.youtube.com/embed/C5YeOc0N6Ao", Director = "Nick Bruno, Troy Quane", stars = "Karen Gillan, Ben Mendelsohn, Will Smith",
                       release = "13 September 2019",user_id=1, movietype = movietype2)

session.add(Moviepage1)
session.commit()

Moviepage2 = MoviePage(name = "Wonder Park",
                       Storyline = "Wonder Park tells the story of a magnificent amusement park where the imagination of a wildly creative girl named June comes alive.",
                       link= "https://www.youtube.com/embed/VML6rQWssSk", Director = " Josh Appelbaum , Andre Nemec",
                       stars = "Brianna Denski, Jennifer Garner, Ken Hudson Campbell", release = "15 March 2019",user_id=1, movietype = movietype2)

session.add(Moviepage2)
session.commit()

Moviepage3 = MoviePage(name = "Toy Story 4", Storyline = '''When a new toy called 'Forky' joins Woody and the gang, a road trip alongside old and new friends reveals
how big the world can be for a toy.''', link= "https://www.youtube.com/embed/P9-jf9-c9JM", Director = "Josh Cooley",stars = "John Lasseter (original story by), Andrew Stanton (original story by)",
                       release = " 21 June 2019",user_id=1, movietype = movietype2)


session.add(Moviepage3)
session.commit()



#third Genre
movietype3 = MovieType(name = "Action",user_id=1)

session.add(movietype3)
session.commit()

Moviepage1 = MoviePage(name = "COLD PURSUIT", Storyline = '''A snowplow driver seeks revenge against the drug dealers he thinks killed his son.
Based on the 2014 Norwegian film 'In Order of Disappearance'.''',
                       link= "https://www.youtube.com/embed/Ez5W8SN9Bqc", Director = " Hans Petter Moland", stars = "Liam Neeson, Emmy Rossum, Laura Dern",
                       release = "22 February 2019",user_id=1, movietype = movietype3)

session.add(Moviepage1)
session.commit()

Moviepage2 = MoviePage(name = "Miss Bala", Storyline = '''Gloria finds a power she never knew she had when she is drawn into a dangerous world of cross-border crime.
Surviving will require all of her cunning, inventiveness, and strength. Based on the Spanish-language film.''',
                       link= "https://www.youtube.com/embed/e-kPf-n4Mto", Director = "Catherine Hardwicke",stars = "Gina Rodriguez, Anthony Mackie, Thomas Dekker",
                       release = "1 February 2019",user_id=1, movietype = movietype3)

session.add(Moviepage2)
session.commit()

Moviepage3 = MoviePage(name = "Dark Phoenix", Storyline = '''Jean Grey begins to develop incredible powers that corrupt and turn her into a Dark Phoenix.
Now the X-Men will have to decide if the life of a team member is worth more than all the people living in the world.''',
                       link= "https://www.youtube.com/embed/QWbMckU3AOQ", Director = "Simon Kinberg",stars = " Jennifer Lawrence, Jessica Chastain, Sophie Turner",
                       release = "7 June 2019",user_id=1, movietype = movietype3)


session.add(Moviepage3)
session.commit()




#fourth Genre
movietype4 = MovieType(name = "Mystery",user_id=1)

session.add(movietype4 )
session.commit()

Moviepage1 = MoviePage(name = "Glass", Storyline = '''Following the conclusion of Split, Glass finds Dunn pursuing Crumb's superhuman figure of The Beast in a series of escalating encounters,
while the shadowy presence of Price emerges as an orchestrator who holds secrets critical to both men.''',
                       link= "https://www.youtube.com/embed/95ghQs5AmNk", Director = "M. Night Shyamalan", stars = "Bruce Willis, Anya Taylor-Joy, Sarah Paulson",
                       release = "18 January 2019",user_id=1, movietype = movietype4 )

session.add(Moviepage1)
session.commit()

Moviepage2 = MoviePage(name = "Ad Astra", Storyline = '''Astronaut Roy McBride (Brad Pitt) travels to the outer edges of the solar system to find his missing father and unravel a mystery that threatens the survival of our planet.
His journey will uncover secrets that challenge the nature of human existence and our place in the cosmos.''',
                       link= "https://www.youtube.com/embed/LZrLgN84euo", Director = "James Gray",stars = "Brad Pitt, Tommy Lee Jones, Donald Sutherland", release = "24 May 2019",user_id=1, movietype = movietype4 )

session.add(Moviepage2)
session.commit()

Moviepage3 = MoviePage(name = "Escape Room", Storyline = '''Six strangers find themselves in circumstances beyond their control, and must use their wits to survive.''',
                       link= "https://www.youtube.com/embed/6dSKUoV0SNI", Director = "Adam Robitel",stars = "Deborah Ann Woll, Tyler Labine, Taylor Russell",
                       release = " 4 January 2019",user_id=1, movietype = movietype4 )


session.add(Moviepage3)
session.commit()
print ("Movies been Added!")
