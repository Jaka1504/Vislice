<!DOCTYPE html>
<html>

<body>

  <h1>Stanje igre:</h1>

  <p>
    Trenutno uganjeni del gesla: {{igra.pravilni_del_gesla()}}
  </p>

  <p>
    Nepravilne črke: {{igra.nepravilni_ugibi()}}
  </p>

  <p>
    Stopnja obešenosti:
  </p>
  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="stanje {{igra.stevilo_napak()}}">

  <form action="/igra/{{id_igre}}" method="post">
    Ugibana črka: <input name="crka" type="text">
    <button type="submit">Ugibaj</button>
  </form>

</body>

</html>