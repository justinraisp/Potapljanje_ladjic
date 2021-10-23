import random
import json
import numpy as np
from re import X
import time

velikost_plosce = 10

stevilo_ladij = 4

konec_igre = False

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

datoteka_s_stanjem = 'stanje.json'

ZACETEK = 'Z'
ZMAGA = 'W'
PORAZ = 'L'



class Uporabnik:
    def __init__(self, Ime, Priimek):
        Ime = self.Ime
        Priimek = self.Priimek



class Igra():

    def __init__(self, plosca=[], pozicija_ladij=[], st_preostalih_strelov=40, st_potopljenih_ladij=0, cas=time.time()):
        self.plosca = plosca
        self.pozicija_ladij = pozicija_ladij
        self.st_preostalih_strelov = st_preostalih_strelov
        self.st_potopljenih_ladij = st_potopljenih_ladij
        self.cas = cas





    def ustvari_plosco(self):
        # Ustvari 10x10 plosco in nakljucno postavi 
        # lajde razlicnih velikosti v razlicne smeri

        for vrstica in range(velikost_plosce):
            vrstica = []
            for stolpec in range(velikost_plosce):
                vrstica.append('.')
            self.plosca.append(vrstica)
            #print(self.plosca)

        stevilo_postavljenih_ladij = 0
        #print(self.plosca)
        indeks = 0
        while stevilo_postavljenih_ladij != stevilo_ladij:
            nakljucna_vrstica = random.randint(0, velikost_plosce - 1)
            nakljucni_stolpec = random.randint(0, velikost_plosce - 1)
            smer = random.choice(['levo', 'desno', 'gor', 'dol'])
            velikost_ladje = [2, 3, 3, 4, 5]
            if self.poskusi_postavit_ladjo(nakljucna_vrstica, nakljucni_stolpec, smer, velikost_ladje[indeks]):
                stevilo_postavljenih_ladij += 1
                indeks += 1 
                   
        



    def izpisi_plosco(self):
        # Izpise plosco z vrsticami A-J in stolpci 0-9
        global abeceda
        debug_mode = True
        abeceda = 'ABCDEFGHIJKLMNOP'
        #abeceda = abeceda[0: len(self.plosca) + 1]
        x = ''
        y = []

        for vrstica in range(len(self.plosca)):
            #print(abeceda[vrstica], end=') ')
            vrst = []
            x += str(abeceda[vrstica])
            vrst.append(abeceda[vrstica])
            for stolpec in range(len(self.plosca[vrstica])):
                if self.plosca[vrstica][stolpec] == 'O':
                    if debug_mode:
                        #print('.', end=' ')
                        x += '.'
                        vrst.append('.')
                    else:
                        #print('.', end=' ')
                        vrst.append('.')
                        x += '.'
                else:
                    #print(self.plosca[vrstica][stolpec], end= ' ')
                    vrst.append(str(self.plosca[vrstica][stolpec]))
                    x += str(self.plosca[vrstica][stolpec])
            #print('')
            x += ' , ' #+ '\n'
            y.append(vrst)

        #print('  ', end= ' ')
        x += '  '

        st = ['/']
        for i in range(len(self.plosca[0])):
            #print(str(i), end=' ')
            x+= str(i)
            st.append(str(i))
        #print('')
        y.append(st)
        a = np.array(y, dtype='object')
        return x


    def izstreli_strel(self, ugib):
        if self.sprejmi_veljavni_strel(ugib):
            lokacija = ugib.upper()
            vrstica = abeceda.find(lokacija[0])
            stolpec = int(lokacija[1])
            print("")
            print("----------------------------")

            if self.plosca[vrstica][stolpec] == ".":
                print("Zgresen strel, nobena ladja ni bila zadeta")
                self.plosca[vrstica][stolpec] = "#"
            elif self.plosca[vrstica][stolpec] == "O":
                print("Zadetek!", end=" ")
                self.plosca[vrstica][stolpec] = "X"
                if self.preveri_potopljeno_ladjo(vrstica, stolpec):
                    print("Ladja je potopljena!")
                    self.st_potopljenih_ladij += 1
                else:
                    print("Ladja je bila zadeta!")

            self.st_preostalih_strelov -= 1
        else:
            return None



    def preveri_plosco_in_postavi_ladjo(self, zacetna_vrst, koncna_vrst, zacetni_stol, koncni_stol):
        # Preveri, ce lahko tam postavi ladjo 
        vse_velja = True
        for vrstica in range(zacetna_vrst, koncna_vrst):
            for stolpec in range(zacetni_stol, koncni_stol):
                if self.plosca[vrstica][stolpec] != '.':
                    vse_velja = False
                    break
        if vse_velja:
            self.pozicija_ladij.append([zacetna_vrst, koncna_vrst, zacetni_stol, koncni_stol])
            for vrstica in range(zacetna_vrst, koncna_vrst):
                for stolpec in range(zacetni_stol, koncni_stol):
                    self.plosca[vrstica][stolpec] = 'O'

        return vse_velja




    def poskusi_postavit_ladjo(self, vrstica, stolpec, smer, dolzina):
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

        return self.preveri_plosco_in_postavi_ladjo(zacetna_vrstica, koncna_vrstica, zacetni_stolpec, koncni_stolpec)



    def preveri_potopljeno_ladjo(self, vrstica, stolpec):
        # Preveri, ce so vsi deli ladje zadeti

        for pozicija in self.pozicija_ladij:
            zacetna_vrstica = pozicija[0]
            koncna_vrstica = pozicija[1]
            zacetni_stolpec = pozicija[2]
            koncni_stolpec = pozicija[3]
            if zacetna_vrstica <= vrstica <= koncna_vrstica and zacetni_stolpec <= stolpec <= koncni_stolpec:
                # Ladja najdena, preveri ce je potopljena
                for vrst in range(zacetna_vrstica, koncna_vrstica):
                    for stolp in range(zacetni_stolpec, koncni_stolpec):
                        if self.plosca[vrst][stolp] != 'X':
                            return False
        return True



    def sprejmi_veljavni_strel(self, lokacija):
        # Pridobi veljavno vrstico in stolpec za strel
        je_veljavno = False
        vrstica = -1
        stolpec = -1
        #lokacija = input('Vnesi vrstico (A-J) in stolpec (0-9), primer B4: ')
        lokacija = str(lokacija).upper()
        while not je_veljavno:
            if len(lokacija) != 2:
                print('Napaka: Vnesi eno vrstico in en stolpec kot B4') 
                return False
            vrstica = lokacija[0]
            stolpec = lokacija[1]

            if not vrstica.isalpha() or not stolpec.isnumeric():
                print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
                return je_veljavno
            vrstica = abeceda.find(vrstica)

            if not (-1 < vrstica < velikost_plosce):
                print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
                return je_veljavno
            stolpec = int(stolpec)

            if not (-1 < stolpec < velikost_plosce):
                print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
                return je_veljavno

            if self.plosca[vrstica][stolpec] == '#' or self.plosca[vrstica][stolpec] == 'X':
                print('Na to pozicijo je ze bil ustreljen strel, izberi drugo pozicijo')
                return je_veljavno

            if self.plosca[vrstica][stolpec] == '.' or self.plosca[vrstica][stolpec] == 'O':
                je_veljavno = True
        return je_veljavno



    def preveri_konec_igre(self):
        # Ali so potopljene vse ladje, ali nam je zmanjkalo strelov

        if self.st_potopljenih_ladij == stevilo_ladij:
            print('Cestitke, zmagali ste!')
            Z = 'Zmaga'
            return Z
        elif self.st_preostalih_strelov <= 0:
            print('Zal ste izgubili! Zmanjkalo vam je strelov')
            P = 'Poraz'
            return P
        return False



def nova_igra():
    igra = Igra([],[],40,0, time.time())
    igra.ustvari_plosco()
    igra.izpisi_plosco()
    return igra

class Potapljanje_ladjic:

    def __init__(self, datoteka_s_stanjem):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem

    
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def ugibaj(self, id_igre, ugib):
        self.nalozi_igre_iz_datoteke()
        igra = self.igre[id_igre]
        poskus = igra.izstreli_strel(ugib)
        self.igre[id_igre] = (igra)
        self.zapisi_igre_v_datoteko()


    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f)
            print(igre)
            for id_igre in igre.keys():
                plosca, pozicija_ladij, st_preostalih_strelov, st_potopljenih_ladij = self.preberi_podatke(igre, id_igre)
                self.igre.update({int(id_igre[0]):
                 Igra(plosca,pozicija_ladij, st_preostalih_strelov, st_potopljenih_ladij)})
            #self.igre = {int(id_igre[0]): (Igra())
                        #for id_igre in igre.items()}
            print(self.igre)

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            #print(self.datoteka_s_stanjem)
            #print(self.igre.items())
            igre = {id_igre: (igra.__dict__) 
                        for id_igre, igra in self.igre.items()}
            json.dump(igre, f)


    def preberi_podatke(self, datoteka, id_igre):
        podatki_igre = datoteka.get(str(id_igre))
        plosca = podatki_igre.get('plosca')
        pozicija_ladij = podatki_igre.get('pozicija_ladij')
        st_preostalih_strelov = podatki_igre.get('st_preostalih_strelov')
        st_potopljenih_ladij = podatki_igre.get('st_potopljenih_ladij')
        return plosca, pozicija_ladij, st_preostalih_strelov, st_potopljenih_ladij


    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra)
        self.zapisi_igre_v_datoteko()
        return id_igre
nova_igra()