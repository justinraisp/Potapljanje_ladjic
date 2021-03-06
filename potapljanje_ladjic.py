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
#crke pomenijo vrstico
    a, b, c, d = igra.izpisi_plosco()[0], igra.izpisi_plosco()[1], igra.izpisi_plosco()[2], igra.izpisi_plosco()[3]
    e, f, g = igra.izpisi_plosco()[4], igra.izpisi_plosco()[5], igra.izpisi_plosco()[6]
    h, i, j = igra.izpisi_plosco()[7], igra.izpisi_plosco()[8], igra.izpisi_plosco()[9]    
    return bottle.template('igra.tpl', igra=igra, a=a, b=b, c=c, d=d, e=e, f=f, g=g,h=h, i=i, j=j)


@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    lokacija = bottle.request.forms.getunicode('lokacija')
    potapljanje_ladjic.ugibaj(id_igre, lokacija)    
    bottle.redirect('/igra/')

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


@bottle.post('/nova-igra/')
def nova_igra():
    id_igre = potapljanje_ladjic.nova_igra()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')    


@bottle.get('/statistika/')
def pokazi_statistiko():
    potapljanje_ladjic.zapisi_igre_v_datoteko()
    slovar_statistik = model.napisi_statistiko(datoteka_s_stanjem)
    return bottle.template('statistika.tpl',
                           slovar_statistik=slovar_statistik)


bottle.run(reloader=True, debug=True)