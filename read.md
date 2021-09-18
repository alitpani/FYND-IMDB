# Fynd IMDB TASK

### The application is hosted on heroku server using gunicorn. There is a simple UI also designed for Search and Get(get all) which can be accessed by the url: 
https://fynd-alit.herokuapp.com/

***

The features such as GET ALL and GET one can be used by anyone who so ever visits the site.

***

## GET-ALL url:
 https://fynd-alit.herokuapp.com/get this perticular URL can also be accessed by UI too.

***

## GET-ONE url: 
https://fynd-alit.herokuapp.com/get_one/39 
this url returs the vaalue based on the id that is passed as and integer. "https://fynd-alit.herokuapp.com/get_one/<id>"
pass id as per your convineance.

***

## Search url:
https://fynd-alit.herokuapp.com/search
you can search any movie by its name

***

### The features like DELETE, UPDATE and CREATE can only be accessed via admin login.(Use POSTMAN to test the below URLS)

if any of the above urls are accessed with out login it will through a message:
{
    "Message": "Please Login Via Admin"
}

***

## login url:
https://fynd-alit.herokuapp.com/login

JSON data to be passed in  postman:
{
"username":"admin",
"password":"admin"
}

***

## **Once logged in you can visit the below urls**

***

## DELETE url(method: 'POST'):
https://fynd-alit.herokuapp.com/delete
JSON data to be passed in  postman:
{
"name": " A Space Odyssey"
}

Pass the movie name you want to delete

***

## Create url(mothod:POST):
https://fynd-alit.herokuapp.com/create

JSON data to be passed in  postman:
 {
        "99popularity": "66.0",
        "director": "Giovanni Pastrone",
        "genre": [
            "Adventure",
            " Drama",
            " War"
        ],
        "imdb_score": 6.6,
        "name": "My Fair Lady"
    }


***

## Update_url(mothod:POST):

 {
        "99popularity": "66.0",
        "director": "Giovanni Pastrone",
        "genre": [
            "Adventure",
            " Drama",
            " War"
        ],
        "imdb_score": 6.6,
        "name": "My Fair Lady"
    }

***

## I have added one admin UI too which can be used to perform create, update and delete oprations via UI.

URl for login:https://fynd-alit.herokuapp.com/login_tmp/
URL for admin: https://fynd-alit.herokuapp.com/admin/

These UI admin page is implemented by FLASK-ADMIN