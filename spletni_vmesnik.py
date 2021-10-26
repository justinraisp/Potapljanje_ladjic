import bottle
import model


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


@bottle.post('/ogled-statistike/')
def ogled():
    bottle.redirect('/statistika/')

@bottle.get('/statistika/')
def pokazi_statistiko():
    slovar_statistik = model.napisi_statistiko1(datoteka_s_stanjem)
    return bottle.template('statistika.tpl',
                           slovar_statistik=slovar_statistik)



if __name__ == '__main__':
    bottle.run(debug=True, reloader=True)