from app import application
from app import data_provider

@application.route('/')
@application.route('/index')
def index():
    #<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='stylesheets/style.css') }}">
    user = data_provider.load_user()
    user_routes = data_provider.get_user_routes(user)
    selected_route = 0
    return '''
    <html>
        <head>
            <title>IncentiDRIVE</title>
            <link rel="stylesheet" type="text/css" href="/static/stylesheets/style.css">
        </head>
        <body>
            <div class="row">IncentiDRIVE</div>
            <div class="column">''' + get_routes_list(user_routes) + '''</div>
            <div class="column">''' \
                    + get_route_description(user_routes[selected_route], user) \
                    + '''</div>
        </div> 
        </body>
    </html>'''

def get_routes_list(routes):
    route_elements = [route.name for route in routes]
    return get_list(route_elements, "routes")

def get_leaderboard_list(leaderboard_list):
    leaderboard_entries = ["{}: {} FuelUnits".format(
            le.user.name, le.performance.fuel_consumption) \
            for le in leaderboard_list]
    return get_list(leaderboard_entries, "leaderboard")

def get_route_description(route, user):
    return '''
    <div class="route-header">
        <h2>{}</h2>'''.format(route.name) + \
        '''<p>{} km</p>'''.format(route.distance) + \
    '''</div>
    <div class="route-personal-stats">
        <h2>Route progress</h2>
        <p>Completed route n times</p>
        <p>Avg fuel consumtion: x</p>
    </div>
    <div class="route-map">
        <p>Map</p>
    </div>
    <div class="leaderboard">''' + get_leaderboard_list(route.leaderboard_list()) \
            + '''</div>'''

def get_list(elements, style_class):
    return "<ul style=\"list-style-type:{};\">\n".format(style_class) + \
            "\n".join("<li>{}</li>".format(el) for el in elements) + \
            "\n</ul>"
