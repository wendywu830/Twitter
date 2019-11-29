# Twitter (CIS 192 HW6)

### How to Run
1. `cd twitter`
2. `pip install -r requirements.txt`
3. `python manage.py makemigrations core`
4. `python manage.py migrate`
5. It should be ready now! Run `python manage.py runserver`


### Routes
* / : Splash page with login and link to sign up
* /signup : sign up page
* /home : home with feed of recent tweets, input box to create tweets, list of recently tweeted hashtags and log out 
* /profile/< id > : profile of user with < id > and all their tweets
* /hashtag/< tag > : list of tweets with < tag >

### Design Considerations
I made 2 models, Tweet and Hashtag, and utilized Django's User model. Tweet had a foreign key to User to keep associations between a author and all tweets they've created. Tweet also had a many-to-many relationship to keep track of users who like and unlike a specific tweet. I also created a Hashtag model in which each tag's content and the tweet that it was written in, also a foreign key, is organized.
