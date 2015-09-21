The Software behind ```http://mihi.lo-res.org/```

online condolence book
======================

DONE:
- relatively painless image upload with dropzone.js
- account-less content submissions and image upload, via session storage.
- first non-stupid design approach
- non-manual approval process: admin filter for submitted but not
  approved messages, one-button approval, image preview in admin
- success message after successful content submission.
- prettier design
- video and link submissions
- display links and videos
- caching of main page

TODO:
- print stylesheet
- generalize for other people to use

NICE TO HAVE:
- prettier slider, maybe multiple images side-by-side (move away from
  bootstrap carousel for this)

MODERATION
==========

Create Superuser
```python manage.py createsuperuser```

Visit
```/admin/submissions/submission/?accepted=sent_not_accepted```

Detail pages have an "accept" button, if not acceptable then delete


ASSETS
======

This needs webpack, just ezec
```
npm install
```

in the directory and run
```
webpack --config webpack.config.js
```

for development, use
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
