%rebase('base.tpl', title='Potapljanje_ladjic')
%import model

<h1 font='Fantasy'> Statistika preteklih iger </h1>

<table style='width:40%'>


<tr>
    <td>
       <h2 class='splash-podatki'>Stevilo iger:</h2>
    </td>
    <td>
        <h2 class='splash-statistika'>{{slovar_statistik['Stevilo iger']}}</h2>
    </td>
</tr>


<tr>
    <td>
       <h2 class='splash-podatki'>Odstotek zmag:</h2>
    </td>
    <td>
        <h2 class='splash-statistika'>{{slovar_statistik['Odstotek zmag']}} %</h2>
    </td>
</tr>


<tr>
    <td>
       <h2 class='splash-podatki'>Stevilo strelov:</h2>
    </td>
    <td>
        <h2 class='splash-statistika'>{{slovar_statistik['Stevilo strelov']}} </h2>
    </td>
</tr>


<tr>
    <td>
       <h2 class='splash-podatki'>Stevilo zadetih strelov:</h2>
    </td>
    <td>
        <h2 class='splash-statistika'>{{slovar_statistik['Stevilo zadetih strelov']}}</h2> 
    </td>
</tr>




<% if slovar_statistik['Stevilo strelov'] != 0:%>
<tr>
    <td>
       <h2 class='splash-podatki'>Najbolj natancna koncana igra:</h2>
    </td>
    <td>
        <h2 class='splash-statistika'>{{slovar_statistik['Najboljsa natancnost igre']}} %</h2>
    </td>
</tr>


<tr>
    <td>
       <h2 class='splash-podatki'>Povprecna natancnost:</h2>
    </td>
    <td>
        <h2 class='splash-statistika'>{{model.odstotek(slovar_statistik['Stevilo zadetih strelov'],slovar_statistik['Stevilo strelov'])}} % </h2>
    </td>
</tr>
<%end%>

</table>