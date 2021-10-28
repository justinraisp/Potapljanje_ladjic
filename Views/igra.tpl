% import model 
% rebase('base.tpl')
% import time


<body>


        <h1>Imate 40 strelov in 3 minute, da zadanete 4 ladje velikosti 2, 3, 4, 5.</h1>

        <h2>{{igra.izpisi_plosco()}}</h2>

</body>


<% if igra.preveri_konec_igre() == 'Zmaga': %>
<div class='splash-container'>
  <h1 class='splash-title'>ZMAGA</h1>
    <h2>Rezultat: </h2>
<!--    <form action="/nova-igra/" method="post">
      <button type="submit" class='btn splash-btn'>Nova igra</button>
    </form>

    <form action="/statistika/" method="get">
      <button type="submit" class='btn splash-btn'>Ogled statistike preteklih iger</button>
    </form>
--> <div>
            <form action="/" method="get">
                <button type="submit" class='btn splash-btn'>Zacetna stran</button>
            </form>

    </div>


</div>

<% elif igra.preveri_konec_igre() == 'Poraz1': %>

<div class='splash-container'>
  <h1 class='splash-title'>PORAZ</h1>
    <h2>Zmanjkalo vam je strelov.</h2>
  <form action="/nova-igra/" method="post">
    <button type="submit" class='btn splash-btn'>Nova igra</button>
  </form>

  <form action="/statistika/" method="get">
    <button type="submit" class='btn splash-btn'>Ogled statistike preteklih iger</button>
  </form>



</div>

<% elif igra.preveri_konec_igre() == 'Poraz2': %>
<div class='splash-container'>
  <h1 class='splash-title'>PORAZ</h1>
    <h2>Zmanjkalo vam je časa.</h2>

<!--  <form action="/nova-igra/" method="post">
    <button type="submit" class='btn splash-btn'>Nova igra</button>
  </form>

  <form action="/statistika/" method="get">
    <button type="submit" class='btn splash-btn'>Ogled statistike preteklih iger</button>
  </form>
--> <div>
            <form action="/" method="get">
                <button type="submit" class='btn splash-btn'>Zacetna stran</button>
            </form>

    </div>

<% else: %>



        <h2 class='splash-izpis'>{{igra.izpisi_strel()}}</h2>






        <h2 class='splash-podatki'>Preostanek casa: {{round(180 - (time.time() - igra.cas))}} sekund</h2>






<h2 class='splash-podatki'>Stevilo preostalih ladij: {{model.stevilo_ladij - igra.st_potopljenih_ladij}}</h2>





        <h2 class='splash-podatki'>Stevilo preostalih strelov: {{igra.st_preostalih_strelov}}</h2>





        <h2 class='splash-podatki'>Stevilo zadetih strelov: {{igra.st_zadetih_strelov}}</h2>




        <h2 class='splash-podatki'>Natancnost: {{igra.natancnost}} %</h2>




  <form id = 'form' action='/igra/' method='post'>
    Vnesi vrstico (A-J) in stolpec (0-9), primer B4:  
      <input type='text' name='lokacija' id='lokacija' maxlength='2' minlength='2' pattern='^[A-j]\d+$' required>
      <button type="submit">Izstreli</button>
  </form>

<% end %>