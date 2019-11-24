from app.data.route import Route, Path, Participation

def load_user_id():
    return 0

def get_user_routes(user):
    routes = [Route(0, "Munich city", Path(0, 1)),
            Route(1, "Munich - Stuttgart", Path(0, 1))]
    routes[0].set_participations([Participation(0, "Alice", 5, 21.3),
            Participation(1, "Bob", 6, 27.8)])
    routes[1].set_participations([Participation(0, "Alice", 5, 21.3),
            Participation(1, "Bob", 6, 27.8)])
    return routes
