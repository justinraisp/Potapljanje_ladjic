% import model 
% rebase('base.tpl')
% import time




<table>
<tr>
    <td>
        <h1>Imate 40 strelov in 3 minute, da zadanete 4 ladje velikosti 2, 3, 3, 4.</h1>
    </td>
</tr>
<tr>
    <td>
        <h2>{{igra.izpisi_plosco()}}</h2>
    </td>
</tr>

</table>

<% if igra.preveri_konec_igre() == 'Zmaga': %>
<div class='splash-container'>
  <h1 class='splash-title'>ZMAGA</h1>
    <h2>Rezultat: </h2>
    <form action="/nova-igra/" method="post">
      <button type="submit">Nova igra</button>
    </form>
</div>

<% elif igra.preveri_konec_igre() == 'Poraz1': %>

<div class='splash-container'>
  <h1 class='splash-title'>PORAZ</h1>
    <h2>Zmanjkalo vam je strelov.</h2>
  <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
</div>

<% elif igra.preveri_konec_igre() == 'Poraz2': %>
<div class='splash-container'>
  <h1 class='splash-title'>PORAZ</h1>
    <h2>Zmanjkalo vam je časa.</h2>

  <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
</div>

<% else: %>

<tr>
    <td>
        <h2 class='splash-podatki'>{{igra.izpisi_strel()}}</h2>
    </td>
</tr>


<tr>
    <td>
        <h2>Preostanek casa: {{round(180 - (time.time() - igra.cas))}} sekund</h2>
    </td>
</tr>


<tr>
    <td>
        <h2>Stevilo preostalih ladij: {{model.stevilo_ladij - igra.st_potopljenih_ladij}}</h2>
    </td>
</tr>

<tr>
    <td>
        <h2>Stevilo preostalih strelov: {{igra.st_preostalih_strelov}}</h2>
    </td>
</tr>

<tr>

  <form id = 'form' action='/igra/' method='post'>
    Vnesi vrstico (A-J) in stolpec (0-9), primer B4:  
      <input type='text' name='lokacija' id='lokacija' maxlength='2' minlength='2' pattern='^[A-j]\d+$' required>
      <button type="submit">Izstreli</button>
  </form>

<% end %>