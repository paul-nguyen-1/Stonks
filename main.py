from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

usernames = []
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
# Home wrote
@app.get('/home/{username}')
def get_home(username: str):
    return {
        "Name": username
    }


@app.put('/username/{username}')
def put_home(username: str):
    usernames.append(username)
    print(username)
    return {
        "username": username
    }


@app.post('/postData')
def post_home(username: str):
    usernames.append(username)
    return {
        "usernames:": usernames
    }


@app.delete('/deleteData/{username}')
def delete_data(username: str):
    usernames.remove(username)
    return {
        "usernames:": usernames
    }

#Method to run on specific end point
@app.api_route("/homedata", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_homedata(username:"str"):
    print(username)
    return {
        "username": username
    }
