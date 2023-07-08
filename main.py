from fastapi import FastAPI

app = FastAPI()


# Home wrote
@app.get('/home')
def get_home():
    return {
        "Name": "Paul Nguyen"
    }
