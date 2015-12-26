The Software behind ```http://mihi.lo-res.org/```

online condolence book
======================

Features:
- relatively painless image upload with dropzone.js
- account-less content submissions and image upload, via django sessions
- approval process: all content on the site needs to be approved by admins
- video and link submissions
- main page is cached by default

TODO:
- print stylesheet
- generalize for other people to use

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
This needs the ```webpack``` program, which needs to be installed using NPM (which has its own dependencies. This was in the app template originally used for this, so: sorry).

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

RUNNING
=======
```
pip install -r requirements.txt
./manage.py collectstatic --noinput
./manage.py migrate
./manage.py runserver
```

DEPLOYING
=========

Django deployment guides exist. Make sure to create a ```local_settings.py``` (possibly by copying settings.py), configuring a proper™ database™ and setting a new ```SECRET_KEY```.

Let me know if you need help.
