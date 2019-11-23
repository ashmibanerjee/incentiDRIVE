from app.data.route import Route
from app.data.user import User

def load_user():
    return User(0, "Maxime Sampleman")

def get_user_routes(user):
    return [Route(0, "Munich center", 2.5),
            Route(1, "Munich - Stuttgart", 204.3)]
