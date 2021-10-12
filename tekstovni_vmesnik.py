import model

def izpis_igre():
    # Poveze vse metode skupaj
    konec_igre = model.konec_igre

    print('---Dobrodosli v igri potapljanje ladjic---')
    print('Imate 50 strelov, da zadanete 5 ladij velikosti 2, 3, 3, 4, 5. Naj se bitka zacne!')

    model.ustvari_plosco()

    while not konec_igre:
        model.izpisi_plosco()
        print('Stevilo preostalih ladij: ' + str(model.stevilo_ladij - model.st_potopljenih_ladij))
        print('Stevilo preostalih strelov: ' + str(model.st_preostalih_strelov))
        model.izstreli_strel()
        print('---------------------------')
        print('')
        model.preveri_konec_igre()