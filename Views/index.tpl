% rebase('base.tpl')
<!DOCTYPE html>
<html>      
    <head>
        <meta charset='utf-8'>
        <title>Potapljanje ladjic</title>
    </head>
    <body>
        <div class='container'>
            <h1 class='title'>Potapljanje ladjic</h1>

            <div>
            <br>
                <form action="/nova-igra/" method="post">
                    <button type="submit" class='btn splash-btn'>Nova igra</button>
                </form>

                <br>
                <br>
                
                <form action="/statistika/" method="get">
                    <button type="submit" class='btn splash-btn'>Ogled statistike preteklih iger</button>
                </form>

            </div>
        </div>

        <img src='/img/battleship-large.svg' class='battleship-image'>
    </body>

</html>