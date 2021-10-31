%rebase('base.tpl', title='Potapljanje_ladjic')
%import model

<h1 text-align='left'> Statistika preteklih iger </h1>

<table style='width:100%'>


<tr>
    <td>
       <h3 class='podatki'>Število iger:</h3>
    </td>
    <td>
        <h3 class='statistika'>{{slovar_statistik['Stevilo iger']}}</h3>
    </td>
</tr>


<tr>
    <td>
       <h3 class='podatki'>Odstotek zmag:</h3>
    </td>
    <td>
        <h3 class='statistika'>{{slovar_statistik['Odstotek zmag']}} %</h3>
    </td>
</tr>


<tr>
    <td>
       <h3 class='podatki'>Število strelov:</h3>
    </td>
    <td>
        <h3 class='statistika'>{{slovar_statistik['Stevilo strelov']}} </h3>
    </td>
</tr>


<tr>
    <td>
       <h3 class='podatki'>Število zadetih strelov:</h3>
    </td>
    <td>
        <h3 class='statistika'>{{slovar_statistik['Stevilo zadetih strelov']}}</h3> 
    </td>
</tr>




<% if slovar_statistik['Stevilo strelov'] != 0:%>
<tr>
    <td>
       <h3 class='podatki'>Najbolj natančna končana igra:</h3>
    </td>
    <td>
        <h3 class='statistika'>{{slovar_statistik['Najboljsa natancnost igre']}} %</h3>
    </td>
</tr>


<tr>
    <td>
       <h3 class='podatki'>Povprečna natančnost:</h3>
    </td>
    <td>
        <h3 class='statistika'>{{model.odstotek(slovar_statistik['Stevilo zadetih strelov'],slovar_statistik['Stevilo strelov'])}} % </h3>
    </td>
</tr>
<%end%>

</table>