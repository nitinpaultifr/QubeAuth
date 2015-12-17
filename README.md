# QubeAuth
Simple token-based authentication API using Django REST Framework.

### Installation
1. Clone the project onto your local machine: `git clone https://github.com/npaul2811/QubeAuth.git` 
2. Create a virtual environment for the project using your favorite virtual environment tool.
3. `cd/into/qubeauth` 
4. Install the project requirements using: `pip install -r requirements.txt`
5. Perform db migrations for the installed apps: `python manage.py migrate`
6. Run the server like so: `python manage.py runserver` 

### Testing the API endpoints
There are 3 available endpoints in the API:
* APIRootView: Root of the API. Only receives GET requests and returns a JSON object with a relevant message.
* AuthView: API endpoint that generates auth-token for a remote client. GET request returns a JSON object with a relevant message. POST request authenticates and logs in the user if user already exists, if the user does not exist, a new user with the given credentials is created and is authenticated and logged in. In both cases, the remote client is authenticated and receives an auth-token along with a relevant message in a JSON object.
* UserDetailsView: If the remote client passes a valid auth-token in the request header, this endpoint returns user info based on the type of request:
  1. GET: Return data for all users
  2. POST: Return data for requested user

To test the various endpoints, you can use the curl command line tool, although you may use your favorite URL tool.
Make sure the Django server is running. You may use any port you wish. This document will use port 8000. Make changes in the commands as required:

* Checking the APIRootView:  
`curl http://localhost:8000`
* Assuming you have created a user 'remote' with password 'remotepass' in your database:  
`curl -X POST -d "username=remote&password=remotepass"  http://localhost:8000/auth/`  
The API will now return an auth-token with a message.
* Requesting auth-token with credentials not already in the database will result in the API creating the new user and returning the auth-toke:  
`curl -X POST -d "username=newremote&password=newpass"  http://localhost:8000/auth/`
* To access details of all users, you must pass your auth-token in the GET request header:
`curl http://localhost:8000/userdetails/ -H 'Authorization: Token 60a2f7ccd2913925e5992f27d0ad44e5f949dc7a'`
A JSON object with details of all users is returned.
* To access details of a specific user, you must pass the username attribute of the user in a POST request, aoong with the auth-token on the request header:
`curl -X POST -d "username=remote" http://localhost:8000/userdetails/ -H 'Authorization: Token 60a2f7ccd2913925e5992f27d0ad44e5f949dc7a'`

#### Dev Note
This API was developed purely as a learning experiment and is not intended to be plugged into an existing project. Feel free to use the code to learn and possibly add features or refactor parts of it to implement a feature in a better, more efficient way. 

Merry Christmas!
