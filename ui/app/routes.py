from app import application

@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'GSSS'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
        <link rel="stylesheet" href="/static/stylesheets/style.css">
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <div class="row">
        <div class="column">C1</div>
        <div class="column">C2</div>
        <div class="column">C3</div>
    </div> 
    </body>
</html>'''
        #<link rel="stylesheet" href="{{ url_for('static', filename='stylesheets/style.css') }}">
