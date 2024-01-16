# meta-coursera-django-littlelemon

**Does the web application use Django to serve static HTML content?**

In the browser, go to 
http://127.0.0.1:8000/restaurant/
which is loaded via static HTML content


**Has the learner committed the project to a Git repository?**

Project available at:
https://github.com/v111317/meta-coursera-django-littlelemon.git


**Does the application connect the backend to a MySQL database?**

Please
check settings.py


**Are the menu and table booking APIs implemented?**

In the browser or insomnia, try accessing
http://127.0.0.1:8000/restaurant/menu/
http://127.0.0.1:8000/restaurant/menu/1
http://127.0.0.1:8000/restaurant/booking/tables/


**Is the application set up with user registration and authentication?**

Try accessing http://127.0.0.1:8000/restaurant/menu/ with and without token

**Does the application contain unit tests?**

Run the tests in the command line as:
python manage.py test littlelemon.tests.test-models.MenuTest.test_get_item
python manage.py test littlelemon.tests.test-views.MenuViewTest.test_getall


**Can the API be tested with the Insomnia REST client?**

Try accessing
http://127.0.0.1:8000/restaurant/menu/
http://127.0.0.1:8000/restaurant/menu/1
