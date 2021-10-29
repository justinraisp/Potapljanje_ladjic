<!DOCTYPE html>
<html>

<head>
<link href="https://fonts.googleapis.com/css2?family=Bangers&display=swap" rel="stylesheet">
<title>Potapljanje ladjic</title>
<style>


aside {
  width: 30%;
  float: right;
  padding: 25px;
  margin-right: 20%;
  margin-top: 20px;
}

table {
    font-size: 15px;

    border: 1px solid black;
}

td {
    width: 3.5%;
    border-top-style: dotted;
    border-right-style: solid;
    border-bottom-style: dotted;
    border-left-style: solid;
    text-align: center;
    border-color: #d9d9d9;
}

h1 {
  font-size: 2.3rem;
  font-family: 'Fantasy';
  margin-left: 1%;
}

h2 {
    font-family: 'Fantasy';
}

body {
    margin: 0;
    background-color: #f3f3f3;
    overflow-x: hidden;
}

*, *::before, *::after {
    font-family: 'Montserrat', sans-serif;
    box-sizing: border-box;
}

.splash-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 66vh;
}

.splash-title {
    font-family: 'Bangers', cursive;
    font-size: 8rem;
}

.splash-izpis {
  font-family: 'Fantasy';
  font-size: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: red;
}

.splash-podatki {
  font-family: 'Fantasy';
  margin-left: 1%;
  font-size: 1.3rem;
  padding: 15px;
}

.splash-statistika {
  font-family: 'Fantasy';
  left: 10vw;
  font-size: 2rem;
  padding: 20px;
}

.splash-battleship-image {
  position: absolute;
  bottom: 5vh;
  left: 15vw;
  right: 10vw;
  width: 60%;
  transform: rotateY(180deg);
  pointer-events: none;
  opacity: .40;
}

.btn {
  background-color: hsl(60, 100%, 50%);
  padding: .4em 1em;
  outline: none;
  border: none;
  text-decoration: none;
  cursor: pointer;
  border-radius:.2em;
  color: #333;
}

.btn:hover, .btn:focus {
  background-color: hsl(60, 100%, 40%);
}

.splash-btn {
  font-size: 2rem;
  margin-left: 2rem;
}

</style>
</head>

<body>
    {{!base}}
</body>

</html>