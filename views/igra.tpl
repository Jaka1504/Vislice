<!DOCTYPE html>
<html>

<body>

  <h1>Stanje igre:</h1>
  
  <p>Trenutno uganjeni del gesla: {{igra.pravilni_del_gesla()}}</p>
  
  <p>Nepravilne črke: {{igra.nepravilni_ugibi()}}</p>

  %if igra.zmaga():
    <p>Čestitke, uganili ste pravilno besedo!</p>
  %elif igra.poraz():
    <p>Oh, ne! Izgubili ste. Pravilna beseda je bila {{igra.geslo}}.</p>
    <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="stanje {{igra.stevilo_napak()}}">
  %else:
    <p>Stopnja obešenosti:</p>
    <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="stanje {{igra.stevilo_napak()}}">
  %end

  %if not igra.zmaga() and not igra.poraz():
  <form action="/igra/{{id_igre}}" method="post">
    Ugibana črka: <input name="crka" type="text" autofocus>
    <button type="submit">Ugibaj</button>
  </form>
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
  %else:
  <form action="/igra/" method="post">
    <button type="submit" autofocus>Nova igra</button>
  </form>
  %end

  
</body>

</html>