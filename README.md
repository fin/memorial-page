# goodbye mihi

collaborative online condolence book, or something. help me!

DONE:
- relatively painless image upload with dropzone.js
- account-less content submissions and image upload, via session storage.
- first non-stupid design approach
- non-manual approval process: admin filter for submitted but not
  approved messages, one-button approval, image preview in admin
- success message after successful content submission.

TODO:
- video and link submissions: thought is to just have a text field with
  a link per line and run it through embedly
- prettier design
- print stylesheet

NICE TO HAVE:
- prettier slider, maybe multiple images side-by-side (move away from
  bootstrap carousel for this)
- caching of main page

MODERATION
==========

Create Superuser, visit
/admin/submissions/submission/?accepted=sent_not_accepted
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


```
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
