import json

from sanic import Sanic
from sanic.response import json as sanic_json
from sanic_jwt import exceptions, protected, initialize
from user import User
from utils import normalize_json

users = []

with open("user.json") as f:
    user = json.load(f)
    users.append(User(*user.values()))

username_table = {u.username: u for u in users}
userid_table = {u.user_id: u for u in users}


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user

app = Sanic("Polyrize Assignment")
initialize(app, authenticate=authenticate)


@app.post('/normalize')
@protected()
async def handle_post(request):
    return sanic_json(normalize_json(request.json))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8888)
