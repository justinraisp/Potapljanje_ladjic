<!DOCTYPE html>
<html>

<head>
<link href="https://fonts.googleapis.com/css2?family=Bangers&display=swap" rel="stylesheet">
<title>Potapljanje ladjic</title>
<style type='text/css'>
    h1 {color: black; }
    body {background-color: white; }

</style>
<style>
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
  background-color: hsl(30, 100%, 50%);
  padding: .4em 1em;
  outline: none;
  border: none;
  text-decoration: none;
  cursor: pointer;
  border-radius:.2em;
  color: #333;
}

.btn:hover, .btn:focus {
  background-color: hsl(30, 100%, 40%);
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