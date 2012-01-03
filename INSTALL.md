Installation Instructions
=========================

Dependencies:

- python 2.6+
- git
- mysql 4.0+

1) Clone project from github


If you are reading this chances are you already did.

git clone git@github.com:muleros/mulatv.git

2) Install a VirtualEnv environment

cd mulatv
virtualenv --no-site-packages env
source env/bin/activate

3) Install Python dependencies using pip

env/bin/pip install --upgrade -r REQUIREMENTS.txt

4) Create database tables

cd project/
../env/bin/python manage.py syncdb
../env/bin/python manage.py migrate
