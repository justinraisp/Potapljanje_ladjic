%rebase('base.tpl', title='Potapljanje_ladjic')

<h2> Statistika preteklih iger </h2>

<table>
<tr>
    <td>
       Odstotek zmag:
    </td>
    <td>
        {{slovar_statistik['Odstotek zmag']}} %
    </td>
</tr>


<tr>
    <td>
       Najbolj natancna igra:
    </td>
    <td>
        {{slovar_statistik['Najboljsa natancnost igre']}} %
    </td>
</tr>


<tr>
    <td>
       Povprecna natancnost:
    </td>
    <td>
        {{slovar_statistik['Povprecna natancnost']}} %
    </td>
</tr>


</table>