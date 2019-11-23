from app import application

@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'GSSS'}
    #<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='stylesheets/style.css') }}">
    return '''
<html>
    <head>
        <title>IncentiDRIVE</title>
        <link rel="stylesheet" type="text/css" href="/static/stylesheets/style.css">
    </head>
    <body>
        <div class="row">IncentiDRIVE</div>
        <div class="column">''' + get_routes_list() + '''</div>
        <div class="column">''' + get_route_description() + '''</div>
    </div> 
    </body>
</html>'''

def get_routes_list():
    return get_list(["Route 1", "Route 2", "Route 3"], "routes")

def get_route_description():
    return '''
<div class="route-header">
    <h2>Route name</h2>
    <p>Route desciption</p>
</div>
<div class="route-personal-stats">
    <h2>Route progress</h2>
    <p>Completed route n times</p>
    <p>Avg fuel consumtion: x</p>
</div>
<div class="route-map">
    <p>Map</p>  '''+  get_map() +'''
</div>
<div class="leaderboard">''' + get_leaderboard_list() + '''</div>'''

def get_leaderboard_list():
    return get_list(["Person 1", "Person 2", "Person 3"], "leaderboard")

def get_list(elements, style_class):
    return "<ul style=\"list-style-type:{};\">\n".format(style_class) + \
            "\n".join("<li>{}</li>".format(el) for el in elements) + \
            "\n</ul>"

def get_map():
    return '''
    <iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d85097.0023446628!2d11.553186560314295!3d48.20119697892448!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e3!4m5!1s0x47a84e248d37632d%3A0xdead51b35f0e0bb3!2sMarienplatz%2C%20Marienplatz%2C%20Munich!3m2!1d48.1373932!2d11.5754485!4m5!1s0x479e72ece78d321f%3A0xf8d2874f0eb7c24c!2sGarching%20-%20Forschungszentrum%2C%2085748%20Garching%20bei%20M%C3%BCnchen!3m2!1d48.265043299999995!2d11.6715693!5e0!3m2!1sen!2sde!4v1574548853280!5m2!1sen!2sde" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen=""></iframe>
    '''