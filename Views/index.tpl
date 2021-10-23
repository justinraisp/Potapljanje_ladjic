% rebase('base.tpl')
<!DOCTYPE html>
<html>      
    <head>
        <meta charset='utf-8'>
        <title>Potapljanje ladjic</title>
    </head>
    <body>
        <div class='splash-container'>
            <h1 class='splash-title'>Potapljanje ladjic</h1>

            <div>
            <!--<form action="/registracija/" method="get">
                <button type="submit" class='btn splash-btn'>Registracija</button>
                </form>
            <br>
            <form action="/prijava/" method="get">
                <button type="submit" class='btn splash-btn'>Prijava</button>
                </form>
                -->
            <br>
            <form action="/nova-igra/" method="post">
                <button type="submit" class='btn splash-btn'>Nova igra</button>
            <!--</form>
               <form action="/statistika/" method="get">
                <button type="submit" class='btn splash-btn'>Ogled statistike preteklih iger</button>
            </form>
            -->
            </div>
        </div>

        <img src='/img/battleship-large.svg' class='splash-battleship-image'>
    </body>


</html>