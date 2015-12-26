Hi there.

This was originally written to serve ```http://mihi.lo-res.org/```, but is now generalized to make it easier to create personalized memorial sites, which allow online communities to come together and celebrate a lost one.

If you're in a position in which you need this, first of all: I'm sorry. This sucks. Thanks for doing this anyway.

online condolence book
======================

Features:
- relatively painless image upload with dropzone.js
- account-less content submissions and image upload, via django sessions
- approval process: all content on the site needs to be approved by admins
- video and link submissions
- main page is cached by default
- optional "message to the family" field, which will not be published

TODO:
- print stylesheet
- generalize for other people to use (change to example content)
- import bake-to-static code from other repo

NICE TO HAVE:
- prettier slider, maybe multiple images side-by-side (move away from
  bootstrap carousel for this)

MODERATION
==========

Create Superuser
```
    python manage.py createsuperuser
```

Visit
```
    /admin/submissions/submission/?accepted=sent_not_accepted
```

Detail pages have an "accept" button, if not acceptable then delete


ASSETS
======

The canonical forms of assets are stored in the ```static``` directory to enable less->css compilation and js minification.
The compiled versions are checked in, but if you need to customize things, you'll need the ```webpack``` program.
It needs to be installed using NPM (which has its own dependencies. This was in the app template originally used for this, so: sorry).

Install all this by navigating to the project root directory and running
```
npm install
```

To recompile assets, navigate to the ```static``` directory and run
```
webpack --config webpack.config.js
```

For asset development, you can use webpack's folder watching feature
```
webpack --config webpack.config.js --watch
```

Read more in the ```static/STATIC_README.md``` file.

RUNNING
=======
```
pip install -r requirements.txt
./manage.py collectstatic --noinput
./manage.py migrate
./manage.py runserver
```

PERSONALIZING
=============

Navigate to the ```/admin``` URL in your installation and create an instance of ```Site``` to customize the page title used for browser tabs.

Copy ```mysite/templates/_person_header.html``` and ```mysite/templates/_footer.html```  to the ```templates``` folder and customize them there.

Change ```static/src/less/custom.less``` and ```static/src/images/background.png```to suit your needs (see ASSETS above for details).


DEPLOYING
=========

Django deployment guides exist. Make sure to create a ```local_settings.py``` (possibly by copying settings.py), configuring a proper™ database™ and setting a new ```SECRET_KEY```.

Let me know if you need help.
