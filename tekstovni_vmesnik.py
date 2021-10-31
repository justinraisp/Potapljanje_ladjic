import model
import time
def izpis_igre(igra):
    konec_igre = model.konec_igre

    print('---Dobrodosli v igri potapljanje ladjic---')
    print('Imate 40 strelov, da zadanete 4 ladje velikosti 2, 3, 4, 5. Naj se bitka zacne!')

    while not konec_igre:
        for vrstica in igra.izpisi_plosco():
            print(vrstica)
        print('Stevilo preostalih ladij: ' + str(model.stevilo_ladij - igra.st_potopljenih_ladij))
        print('Stevilo preostalih strelov: ' + str(igra.st_preostalih_strelov))
        preostali_cas = 180 - int(time.time() - int(igra.cas))
        print('Preostali cas: '+ str(preostali_cas) )
        ugib = input('Vnesi vrstico (A-J) in stolpec (0-9), primer B4: ')
        igra.izstreli_strel(ugib)
        print('---------------------------')
        print(igra.izpisi_strel())
        print('')
        if igra.stanje == 'W':
            print('Cestitke, zmagali ste!')
            konec_igre = True
        if igra.stanje == 'L':
            print('Zal ste izgubili, zmanjkalo vam je strelov.')
            konec_igre = True
        if time.time() - igra.cas >180:
            print('Zal ste izgubili, zmanjkalo vam je casa.')
            konec_igre = True

IGRA = model.nova_igra()
izpis_igre(IGRA)