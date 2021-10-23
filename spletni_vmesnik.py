import bottle
from bottle_login import LoginPlugin
import model
from bottle import Bottle
import json

SKRIVNOST = 'moja skrivnost'
datoteka_s_stanjem = 'stanje.json'

potapljanje_ladjic = model.Potapljanje_ladjic(datoteka_s_stanjem)
potapljanje_ladjic.zapisi_igre_v_datoteko()


@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    igra = potapljanje_ladjic.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra)


@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    lokacija = bottle.request.forms.getunicode('lokacija')
    potapljanje_ladjic.ugibaj(id_igre, lokacija)    
    bottle.redirect('/igra/')

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


#@bottle.route('/registracija/')
#def registracija():
#    return bottle.template('registracija.tpl')


#@bottle.route('/prijava/')
#def prijava():
#    return bottle.template('prijava.tpl')


@bottle.post('/nova-igra/')
def nova_igra():
    id_igre = potapljanje_ladjic.nova_igra()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')    


#@bottle.get('/statistika/')
#def pokazi_statistiko():
#    slovar_statistik = model.statistika(datoteka_s_stanjem)
#    return bottle.template('statistika.tpl',
#                           slovar_statistik=slovar_statistik)


#usernames = ["username", "user"]
#passwords = ["password", "pass"]
#def preveri_prijavo(username, password):
#    if username in usernames and password in passwords:
#        return True
#    else:
#        return False


#@bottle.route('/prijava/', method='POST') 
#def do_login():
#    username = bottle.request.forms.get('username')
#    password = bottle.request.forms.get('password')
#    if preveri_prijavo(username, password):
#        bottle.response.set_cookie("account", username, secret='some-secret-key')
#        return bottle.template('Pozdravljen {{name}}. Dobrodosel nazaj.', name=username)
#    else:
#        return "<p>Your log in attempt has failed</p>"











#@app.route('/')
#def index():
#    current_user = login.get_user()
#    return current_user.name

#@app.route('/signout')
#def signout():
    # Implement logout
#    login.logout_user()
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







if __name__ == '__main__':
    bottle.run(debug=True, reloader=True)