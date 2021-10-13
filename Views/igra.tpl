% import model 
% rebase('base.tpl')
% igra.ustvari_plosco()

<table>
<tr>
    <td>
        <h2>{{igra.izpisi_plosco().split(',')}}</h2>
    </td>
</tr>

</table>

% if igra.preveri_konec_igre():
<h1>ZMAGA</h1>

  <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% else:

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

  <form action='/igra/' method='post'>
    Lokacija: <input type='text' name='lokacija' />
    <button type="submit">Izstreli</button>
  </form>


% end