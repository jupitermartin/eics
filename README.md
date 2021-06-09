# Getting Started with Buildin, Running APP

1. Install packages

-Make sure your local environment have python3.7 or later and pip installed
pip install Django==3.1.6
pip install icalendar
pip install mysqlclient

2. Database install

-Make sure that the name of your database that give me is 'fibre_map'
-Run commands
python manage.py makemigrations cudb
python manage.py migrate cudb
python manage.py runserver

