% import model 
% rebase('base.tpl')
% import time


<!--
<script>
$( "#plosca" ).load( "plosca #plosca" );
</script>
<div include-html='plosca.html' id='plosca'></div>
<script src='jquery-3.6.0.js'></script>
<script src='include-html.js'></script>


  {%for value in igra.izpisi_plosco()%}
  {%endfor%}
-->
<body>

        <h1>Imate 40 strelov in 3 minute, da zadanete 4 ladje velikosti 2, 3, 4, 5.</h1>

<table>
    <tr>
      <td>A</td><td>{{a[1]}}</td><td>{{a[2]}}</td><td>{{a[3]}}</td><td>{{a[4]}}</td><td>{{a[5]}}</td><td>{{a[6]}}</td><td>{{a[7]}}</td><td>{{a[8]}}</td><td>{{a[9]}}</td><td>{{a[10]}}</td>
    </tr>
    <tr>
      <td>B</td><td>{{b[1]}}</td><td>{{b[2]}}</td><td>{{b[3]}}</td><td>{{b[4]}}</td><td>{{b[5]}}</td><td>{{b[6]}}</td><td>{{b[7]}}</td><td>{{b[8]}}</td><td>{{b[9]}}</td><td>{{b[10]}}</td>
    </tr>
    <tr>
      <td>C</td><td>{{c[1]}}</td><td>{{c[2]}}</td><td>{{c[3]}}</td><td>{{c[4]}}</td><td>{{c[5]}}</td><td>{{c[6]}}</td><td>{{c[7]}}</td><td>{{c[8]}}</td><td>{{c[9]}}</td><td>{{c[10]}}</td>
    </tr>
    <tr>
      <td>D</td><td>{{d[1]}}</td><td>{{d[2]}}</td><td>{{d[3]}}</td><td>{{d[4]}}</td><td>{{d[5]}}</td><td>{{d[6]}}</td><td>{{d[7]}}</td><td>{{d[8]}}</td><td>{{d[9]}}</td><td>{{d[10]}}</td>
    </tr>
    <tr>
      <td>E</td><td>{{e[1]}}</td><td>{{e[2]}}</td><td>{{e[3]}}</td><td>{{e[4]}}</td><td>{{e[5]}}</td><td>{{e[6]}}</td><td>{{e[7]}}</td><td>{{e[8]}}</td><td>{{e[9]}}</td><td>{{e[10]}}</td>
    </tr>
    <tr>
      <td>F</td><td>{{f[1]}}</td> <td>{{f[2]}}</td> <td>{{f[3]}}</td> <td>{{f[4]}}</td> <td>{{f[5]}}</td> <td>{{f[6]}}</td> <td>{{f[7]}}</td> <td>{{f[8]}}</td> <td>{{f[9]}}</td><td>{{f[10]}}</td>
    </tr>
    <tr>
      <td>G</td><td>{{g[1]}}</td><td>{{g[2]}}</td><td>{{g[3]}}</td><td>{{g[4]}}</td><td>{{g[5]}}</td><td>{{g[6]}}</td><td>{{g[7]}}</td><td>{{g[8]}}</td><td>{{g[9]}}</td><td>{{g[10]}}</td>
    </tr>
    <tr>
      <td>H</td><td>{{h[1]}}</td><td>{{h[2]}}</td><td>{{h[3]}}</td><td>{{h[4]}}</td><td>{{h[5]}}</td><td>{{h[6]}}</td><td>{{h[7]}}</td><td>{{h[8]}}</td><td>{{h[9]}}</td><td>{{h[10]}}</td>
    </tr>
    <tr>
      <td>I</td><td>{{i[1]}}</td><td>{{i[2]}}</td><td>{{i[3]}}</td><td>{{i[4]}}</td><td>{{i[5]}}</td><td>{{i[6]}}</td><td>{{i[7]}}</td><td>{{i[8]}}</td><td>{{i[9]}}</td><td>{{i[10]}}</td>
    </tr>
    <tr>
      <td>J</td><td>{{j[1]}}</td><td>{{j[2]}}</td><td>{{j[3]}}</td><td>{{j[4]}}</td><td>{{j[5]}}</td><td>{{j[6]}}</td><td>{{j[7]}}</td><td>{{j[8]}}</td><td>{{j[9]}}</td><td>{{j[10]}}</td>
    </tr>
    <tr>
      <td>/</td> <td>0</td> <td>1</td> <td>2</td> <td>3</td> <td>4</td> <td>5</td> <td>6</td> <td>7</td> <td>8</td> <td>9</td>
    </tr>

  </table>
</body>


<% if igra.preveri_konec_igre() == 'Zmaga': %>
<div class='splash-container'>
  <h1 class='splash-title'>ZMAGA</h1>
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
<!--
<div class='splash-container'>
  <h1 class='splash-title'>PORAZ</h1>
    <h2>Zmanjkalo vam je strelov.</h2>
  <form action="/nova-igra/" method="post">
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