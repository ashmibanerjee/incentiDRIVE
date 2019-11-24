from app import application
from app import data_provider

@application.route('/')
@application.route('/index')
def index():
    #<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='stylesheets/style.css') }}">
    user_id = data_provider.load_user_id()
    user_routes = data_provider.get_user_routes(user_id)
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
                    + get_route_description(
                            user_routes[selected_route], user_id) + '''</div>
        </div> 
        </body>
    </html>'''

def get_routes_list(routes):
    route_elements = ["<h1>{}</h1><p>{}</p>".format(
        route.name, route.path.length()) for route in routes]
    return get_list(route_elements, "routes")

def get_route_description(route, user_id):
    return '''
    <div class="route-header">
        <h2>{}</h2>'''.format(route.name) + \
        '''<p>{} km</p>'''.format(route.path.length()) + \
    '''</div>
    <div class="route-personal-stats">
        <h2>Route progress</h2>
        <p>Completed route n times</p>
        <p>Avg fuel consumtion: x</p>
    </div>
    <div class="route-map">
        <p>Map</p>  '''+  get_map() +'''
    </div>
    <div class="leaderboard">''' \
            + get_leaderboard_list(route.participations) + '''</div>'''

def get_leaderboard_list(participations):
    # TODO: sort participations
    leaderboard_entries = ["{}: {} l on avg.".format(
            p.user_name, p.total_consumption / p.num_tries) \
            for p in participations]
    return get_list(leaderboard_entries, "leaderboard")

def get_list(elements, style_class):
    return "<ul style=\"list-style-type:{};\">\n".format(style_class) + \
            "\n".join("<li>{}</li>".format(el) for el in elements) + \
            "\n</ul>"

def get_map():
    return '''
    <iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d85097.0023446628!2d11.553186560314295!3d48.20119697892448!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e3!4m5!1s0x47a84e248d37632d%3A0xdead51b35f0e0bb3!2sMarienplatz%2C%20Marienplatz%2C%20Munich!3m2!1d48.1373932!2d11.5754485!4m5!1s0x479e72ece78d321f%3A0xf8d2874f0eb7c24c!2sGarching%20-%20Forschungszentrum%2C%2085748%20Garching%20bei%20M%C3%BCnchen!3m2!1d48.265043299999995!2d11.6715693!5e0!3m2!1sen!2sde!4v1574548853280!5m2!1sen!2sde" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen=""></iframe>
    '''
