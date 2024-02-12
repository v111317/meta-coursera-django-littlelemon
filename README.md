# Meta Course Back-End Developer Capstone 

**Does the web application use Django to serve static HTML content?**

In the browser, go to 
http://127.0.0.1:8000/restaurant/
which is loaded via static HTML content
<br/><br/>

**Has the learner committed the project to a Git repository?**

Project available at:
https://github.com/v111317/meta-coursera-django-littlelemon.git
<br/><br/>

**Does the application connect the backend to a MySQL database?**

Please
check settings.py
<br/><br/>

**Are the menu and table booking APIs implemented?**

In the browser or insomnia, try accessing
http://127.0.0.1:8000/restaurant/menu/<br/>
http://127.0.0.1:8000/restaurant/menu/1<br/>
http://127.0.0.1:8000/restaurant/booking/tables/
<br/><br/>

**Is the application set up with user registration and authentication?**

Try accessing http://127.0.0.1:8000/restaurant/menu/ with and without token
<br/><br/>

**Does the application contain unit tests?**

Run the tests in the command line as:
python manage.py test littlelemon.tests.test-models.MenuTest.test_get_item<br/>
python manage.py test littlelemon.tests.test-views.MenuViewTest.test_getall
<br/><br/>

**Can the API be tested with the Insomnia REST client?**

Try accessing
http://127.0.0.1:8000/restaurant/menu/<br/>
http://127.0.0.1:8000/restaurant/menu/1
<br/><br/>
