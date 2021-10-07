import random
import json

plosca = [[]]

velikost_plosce = 10

stevilo_ladij = 5

st_preostalih_strelov = 50

konec_igre = False

st_potopljenih_ladij = 0

pozicija_ladij = [[]]

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



class Uporabnik:
    def __init__(self, Ime, Priimek):
        Ime = self.Ime
        Priimek = self.Priimek

def preveri_plosco_in_postavi_ladjo(zacetna_vrst, koncna_vrst, zacetni_stol, koncni_stol):
    # Preveri, ce lahko tam postavi ladjo 
    global plosca
    global pozicija_ladij

    vse_velja = True
    for vrstica in range(zacetna_vrst, koncna_vrst):
        for stolpec in range(zacetni_stol, koncni_stol):
            if plosca[vrstica][stolpec] != '.':
                vse_velja = False
                break
    if vse_velja:
        pozicija_ladij.append([zacetna_vrst, koncna_vrst, zacetni_stol, koncni_stol])
        for vrstica in range(zacetna_vrst, koncna_vrst):
            for stolpec in range(zacetni_stol, koncni_stol):
                plosca[vrstica][stolpec] = 'O'

    return vse_velja

def poskusi_postavit_ladjo(vrstica, stolpec, smer, dolzina):
    # Glede na smer poskusi postavit ladjo
    global velikost_plosce

    # Definiramo zato, da se premikamo samo po eni vrstici/stolpci naenkrat
    zacetna_vrstica, koncna_vrstica, zacetni_stolpec, koncni_stolpec = vrstica, vrstica +1, stolpec, stolpec +1

    if smer == 'levo':
        if stolpec - dolzina < 0:
            return False
        zacetni_stolpec = stolpec - dolzina +1

    elif smer == 'desno':
        if stolpec + dolzina >= velikost_plosce:
            return False
        koncni_stolpec = stolpec + dolzina         

    elif smer == 'gor':
        if vrstica - dolzina < 0:
            return False
        zacetna_vrstica = vrstica - dolzina +1 

    elif smer == 'dol':
        if vrstica + dolzina >= velikost_plosce:
            return False
        koncna_vrstica = vrstica + dolzina

    return preveri_plosco_in_postavi_ladjo(zacetna_vrstica, koncna_vrstica, zacetni_stolpec, koncni_stolpec)


def ustvari_plosco():
    # Ustvari 10x10 plosco in nakljucno postavi 
    # lajde razlicnih velikosti v razlicne smeri
    global plosca
    global velikost_plosce
    global stevilo_ladij
    global pozicija_ladij

    plosca = []
    for vrstica in range(velikost_plosce):
        vrstica = []
        for stolpec in range(velikost_plosce):
            vrstica.append('.')
        plosca.append(vrstica)

    stevilo_postavljenih_ladij = 0
    pozicija_ladij = []

    indeks = 0
    while stevilo_postavljenih_ladij != stevilo_ladij:
        nakljucna_vrstica = random.randint(0, velikost_plosce - 1)
        nakljucni_stolpec = random.randint(0, velikost_plosce - 1)
        smer = random.choice(['levo', 'desno', 'gor', 'dol'])
        velikost_ladje = [2, 3, 3, 4, 5]
        if poskusi_postavit_ladjo(nakljucna_vrstica, nakljucni_stolpec, smer, velikost_ladje[indeks]):
            stevilo_postavljenih_ladij += 1
            indeks += 1
    

def izpisi_plosco():
    # Izpise plosco z vrsticami A-J in stolpci 0-9
    global plosca
    global abeceda

    debug_mode = True

    abeceda = abeceda[0: len(plosca) + 1]

    for vrstica in range(len(plosca)):
        print(abeceda[vrstica], end=') ')
        for stolpec in range(len(plosca[vrstica])):
            if plosca[vrstica][stolpec] == 'O':
                if debug_mode:
                    print('.', end=' ')
                else:
                    print('.', end=' ')
            else:
                print(plosca[vrstica][stolpec], end= ' ')
        print('')

    print('  ', end= ' ')

    for i in range(len(plosca[0])):
        print(str(i), end=' ')
    print('')


def sprejmi_veljavni_strel():
    # Pridobi veljavno vrstico in stolpec za strel

    global abeceda
    global plosca
    je_veljavno = False
    vrstica = -1
    stolpec = -1

    while not je_veljavno:
        lokacija = input('Vnesi vrstico (A-J) in stolpec (0-9), primer B4: ')
        lokacija = lokacija.upper()
        if len(lokacija) <= 0 or len(lokacija) > 2:
            print('Napaka: Vnesi eno vrstico in en stolpec kot B4') 
            continue
        vrstica = lokacija[0]
        stolpec = lokacija[1]

        if not vrstica.isalpha() or not stolpec.isnumeric():
            print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
            continue
        vrstica = abeceda.find(vrstica)

        if not (-1 < vrstica < velikost_plosce):
            print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
            continue
        stolpec = int(stolpec)

        if not (-1 < stolpec < velikost_plosce):
            print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
            continue

        if plosca[vrstica][stolpec] == '#' or plosca[vrstica][stolpec] == 'X':
            print('Na to pozicijo je ze bil ustreljen strel, izberi drugo pozicijo')
            continue
        if plosca[vrstica][stolpec] == '.' or plosca[vrstica][stolpec] == 'O':
            je_veljavno = True

    return vrstica, stolpec


def preveri_potopljeno_ladjo(vrstica, stolpec):
    # Preveri, ce so vsi deli ladje zadeti
    global pozicija_ladij
    global plosca

    for pozicija in pozicija_ladij:
        zacetna_vrstica = pozicija[0]
        koncna_vrstica = pozicija[1]
        zacetni_stolpec = pozicija[2]
        koncni_stolpec = pozicija[3]
        if zacetna_vrstica <= vrstica <= koncna_vrstica and zacetni_stolpec <= stolpec <= koncni_stolpec:
            # Ladja najdena, preveri ce je potopljena
            for vrst in range(zacetna_vrstica, koncna_vrstica):
                for stolp in range(zacetni_stolpec, koncni_stolpec):
                    if plosca[vrst][stolp] != 'X':
                        return False
    return True


def izstreli_strel():
    global plosca
    global st_potopljenih_ladij
    global st_preostalih_strelov

    vrstica, stolpec = sprejmi_veljavni_strel()
    print("")
    print("----------------------------")

    if plosca[vrstica][stolpec] == ".":
        print("Zgresen strel, nobena ladja ni bila zadeta")
        plosca[vrstica][stolpec] = "#"
    elif plosca[vrstica][stolpec] == "O":
        print("Zadetek!", end=" ")
        plosca[vrstica][stolpec] = "X"
        if preveri_potopljeno_ladjo(vrstica, stolpec):
            print("Ladja je potopljena!")
            st_potopljenih_ladij += 1
        else:
            print("Ladja je bila zadeta!")

    st_preostalih_strelov-= 1


def preveri_konec_igre():
    # Ali so potopljene vse ladje, ali nam je zmanjkalo strelov
    global st_preostalih_strelov
    global stevilo_ladij
    global konec_igre
    global st_potopljenih_ladij

    if st_potopljenih_ladij == stevilo_ladij:
        print('Cestitke, zmagali ste!')
        konec_igre = True
    elif st_preostalih_strelov <= 0:
        print('Zal ste izgubili! Zmanjkalo vam je strelov')
        konec_igre = True


def main():
    # Poveze vse metode skupaj
    global konec_igre

    print('---Dobrodosli v igri potapljanje ladjic---')
    print('Imate 50 strelov, da zadanete 5 ladij velikosti 2, 3, 3, 4, 5. Naj se bitka zacne!')

    ustvari_plosco()

    while not konec_igre:
        izpisi_plosco()
        print('Stevilo preostalih ladij: ' + str(stevilo_ladij - st_potopljenih_ladij))
        print('Stevilo preostalih strelov: ' + str(st_preostalih_strelov))
        izstreli_strel()
        print('---------------------------')
        print('')
        preveri_konec_igre()

if __name__ == '__main__':
    main()