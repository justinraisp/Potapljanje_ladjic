import bottle
from bottle_login import LoginPlugin
import model

SKRIVNOST = 'moja skrivnost'


@bottle.route('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova-igra/')
def nova_igra():
    id_igre = model.main()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')


@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    crka = bottle.request.forms.getunicode('crka')    
    bottle.redirect('/igra/')

@bottle.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='./')






#app = Bottle()
#app.config['SECRET_KEY'] = 'secret'

#login = app.install(LoginPlugin())

#@login.load_user
#def load_user_by_id(user_id):
    


# Some application views

#@app.route('/')
#def index():
#    current_user = login.get_user()
#    return current_user.name

#@app.route('/signout')
#def signout():
    # Implement logout
#    login.logout_user()
#    return redirect('/')

#@app.route('/signin')
#def signin():
    # Implement login (you can check passwords here or etc)
#    user_id = int(request.GET.get('user_id'))
#    login.login_user(user_id)
#    return redirect('/')

#@route('/', method='POST')
#def index():
#    return '<h1>index</h1>'


#@error(404)
#def error404(error):
    #return '<h1>You have experienced a 404</h1>'

#@error(405)
#def error405(error):
    #return '<h1>This method is not allowed</h1>'

#@error(500)
#def error500(error):
    #return '<h1>Something went wrong</h1>'


#@route('/')
#def index():
#    return {'name' : 'jsonData', 'myList': [1,2,3,4,5]}


#@route('/querytest')
#def querytest():
#    p1 = request.query.p1
#    p2 = request.query.p2
#    return '<h1>The value of p1 is: ' + p1 + ' and the value of p2 is: ' + p2 + '</h1>'




if __name__ == '__main__':
    bottle.run(debug=True, reloader=True)