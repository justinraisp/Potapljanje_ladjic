% import model 
% rebase('base.tpl')

<table>
<tr>
    <td>
        <h2>{{igra.izpisi_plosco()}}</h2>
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
    Vnesi vrstico (A-J) in stolpec (0-9), primer B4:  <input type='text' name='lokacija' />
    <div name="gumbi">
      <button type="submit">Izstreli</button>
    </div>
  </form>

% end

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>


<script>
document.addEventListener('DOMContentLoaded', function () {

//For Each element As HtmlElement In Document.GetElementsByTagName("input")
//    If element.GetAttribute("value") = "Log in" Then
//        element.InvokeMember("click")
//    End If
//Next  


    //var obrazec = document.GetElementsByTagName('input');
    var gumb = document.getElementsByName('gumbi')[0];

    $(gumb).click(function(event) {
        var lokacija = document.getElementsByName('lokacija')[0];

// imeReg isto za ime kot za priimek
        var lokacijaReg = /^[0-9][aAbBcCdDeEfFgGhHiIjJ]/;

        var odg = '';
        var uspesno = true;
        if(lokacijaReg.test(lokacija) === false)
        {
            odg = 'Neveljaven vnos.';
            alert(odg);
            event.preventDefault();
        }
    });
});
</script>