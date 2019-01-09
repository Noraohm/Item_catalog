
# Item_catalog-project

**project overview**

You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.. _**(text from Udacity Project page)**_

## Prerequisites
To run a Python you need below:
1) Python 2 or 3 version from [click here](https://www.python.org/downloads/).
2) Virtual box (last update) [click here](https://www.virtualbox.org/wiki/Downloads)
3) Vagrant (last update) [click here](https://www.vagrantup.com/downloads.html).
4) command line (Git Bash for windows) [click here](https://git-scm.com/downloads).
5) Google & github to search if you stuck in any steps [click here](https://github.com/).
6) Python Pip to download the rest framework [click here](https://pip.pypa.io/en/stable/installing/).

## Installing:

follow the instruction in the download page for installing the programs.

### Steps:

1) Download and install (Python, vagrant & Virtual Box " don't lunch the program").

2) open Gitbash or the command line you use and access the path you add the directory in. like
```
$cd Documents/filename
```
3) Write the below to add the initial vagrantfile.
```
$cd vagrant init
```

4) Write the below to upload the vagrant file. it will update if there is any update need or any change you made in the file.
(better to search in google about the vagrant file which already been used to avoid the issue in psql)

```
$vagrant up
```
5) better to write (Vagrant provision) to make sure the vagrant connect to the virtual box + all the update done.
```
$vagrant provision
```
6) Write the vagrant ssh to connect the vagrant with the file to share the data.
```
$vagrant ssh
```
7) if it connected, go the vagrant file you have by typing
```
$cd /vagrant
```
8) for the first use of the vagrantfile. you need to install pip by following the instruction in the download page.

9) After pip installation done, you need to install flask , sqlalchemy, requests

```
$ pip install flask
```
```
$ pip install sqlalchemy
```
```
$ pip install requests
```




## Projct steps:

**for the project you need to create 3 python file.**
1st) for database creation. You will add all the db tables & the key relation inside the file.
2nd) for database information (seeder) you want to add.
3rd) for the Python code.

Here in the project we used flask , so you need to work in both python , html and you will call flask framework to make the queries much more
faster and easier to read.
for Authentication & Authorization, in the project we used the third party method ( google OAuth).

To check the code if it as pip code format type below

```
$ pycodestyle (project name).py
```
After finishing the project coding, you will access the path by typing the below after step 7 in above steps.

```
$ python (project name).py
```

To start the URL .. just write the URL in the browser.
```
http://localhost:(port number)

```

## Authors
Nora Almotairy
