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
    <p>Map</p>
</div>
<div class="leaderboard">''' + get_leaderboard_list() + '''</div>'''

def get_leaderboard_list():
    return get_list(["Person 1", "Person 2", "Person 3"], "leaderboard")

def get_list(elements, style_class):
    return "<ul style=\"list-style-type:{};\">\n".format(style_class) + \
            "\n".join("<li>{}</li>".format(el) for el in elements) + \
            "\n</ul>"
