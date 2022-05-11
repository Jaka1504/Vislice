<!DOCTYPE html>
<html>

<body>

  <h1>Stanje igre:</h1>

  <img src="img/10.jpg" alt="obesanje">

  <p>
    Trenutno uganjeni del gesla: {{igra.pravilni_del_gesla()}}
  </p>

  <p>
    Nepravilne črke: {{igra.nepravilni_ugibi()}}
  </p>

  <p>
    Stopnja obešenosti:
  </p>
  <img src="img/{{igra.stevilo_napak()}}.jpg" alt="stanje {{igra.stevilo_napak()}}">

</body>

</html>