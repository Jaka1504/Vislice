import bottle
import model


vislice = model.Vislice()


@bottle.get("/img/<file>")
def staticne_slike(file):
    return bottle.static_file(file, root="img")


@bottle.get("/")
def osnovna_stran():
    return bottle.template("index")


@bottle.post("/igra/")
def nova_igra():
    novi_id = vislice.nova_igra()
    bottle.redirect(f"/igra/{novi_id}")


@bottle.get("/igra/<id_igre:int>")
def pokazi_igro(id_igre):
    return bottle.template("igra", igra=vislice.igre[id_igre][0], id_igre=id_igre)


@bottle.post("/igra/<id_igre:int>")
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode("crka").upper()
    vislice.ugibaj(id_igre, crka)
    return pokazi_igro(id_igre)


# to naj bo na dnu
bottle.run(reloader=True, debug=True)