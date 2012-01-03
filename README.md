Templar
=======

A test bed for Django templates

Installation:

virtualenv --no-site-packages env                                               
source env/bin/activate                                                         
env/bin/pip install --upgrade -r REQUIREMENTS.txt   

cd project

../env/bin/python manage.py syncdb

../env/bin/python manage.py migrate

Usage:

Start the web server with:

../env/bin/python manage.py runserver

Just browse any URL at http://localhost:8000/ or the host and port your are
running the project at such as:

http://localhost:8000/products/001

Templar will look for the following template:

.../templates/products/001.html

This happens because a '.html' suffix gets appended to the requested URL.

If the .html file is not found a 404 error get displayed.

If the requested URL ends with a forward slash ('/') then the 'index.html'
suffix is appended instead so for example:

http://localhost:8000/products/

Looks for the following template file:

.../templates/products/index.html

For setting variables in the context just edit the context.json file at:

.../static/json/context.json

So, if you have this JSON file for example:

{
  "products" : [
     {
       "name"  : "Product 1",
       "price" : 1.00
     },
     {
       "name" : "Product 2",
       "price" : 10.00
     }
  ]
}

You'll be able to reference it in templates like this:

{% for p in products %}
<p>The price for product {{ p.name }} is {{ p.price }}.</p>
{% endfor %}

And that's it for now. This should help you practice with Django templates
if you're a designer or developer. Have fun!

(C) 2012 - Antonio Ognio <antonio@ognio.com>
