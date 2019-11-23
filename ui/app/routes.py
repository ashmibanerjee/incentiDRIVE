from app import application

@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'GSSS'}
    return '''
<html>
    <head>
        <title>IncentiDRIVE</title>
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='stylesheets/style.css') }}">
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <div class="row">Header</div>
        <div class="column">C1</div>
        <div class="column">C2</div>
        <div class="column">C3</div>
    </div> 
    </body>
</html>'''
