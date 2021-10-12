import model

def izpis_igre(igra):
    # Poveze vse metode skupaj
    konec_igre = model.konec_igre

    print('---Dobrodosli v igri potapljanje ladjic---')
    print('Imate 50 strelov, da zadanete 5 ladij velikosti 2, 3, 3, 4, 5. Naj se bitka zacne!')

    igra.ustvari_plosco()

    while not konec_igre:
        igra.izpisi_plosco()
        print('Stevilo preostalih ladij: ' + str(model.stevilo_ladij - igra.st_potopljenih_ladij))
        print('Stevilo preostalih strelov: ' + str(igra.st_preostalih_strelov))
        igra.izstreli_strel()
        print('---------------------------')
        print('')
        igra.preveri_konec_igre()

IGRA = model.nova_igra()
izpis_igre(IGRA)