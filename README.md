# djwiki
Wiki pages in django

Features
--------

* Add categories for sorting/arranging articles
* Add/Edit/Delete Articles
* View Edit History/Summary

Unit Tests
--------

* Run tests as:-
 $ python manage.py test --keepdb

Setup Instructions
--------

* simple captcha

 - You must install following dependencies:-
    apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev

 - Then installing simple catcha with:-
    pip install Pillow
    pip install django-simple-captcha
