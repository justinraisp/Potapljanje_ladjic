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










if __name__ == '__main__':
    bottle.run(debug=True, reloader=True)