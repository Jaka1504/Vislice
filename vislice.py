import bottle
import model

SKRIVNOST = "A ma kdo kakšno kreativno idejo?"

vislice = model.Vislice()
vislice.nalozi_iz_datoteke()


@bottle.get("/img/<file>")
def staticne_slike(file):
    return bottle.static_file(file, root="img")


@bottle.get("/")
def osnovna_stran():
    return bottle.template("index")


@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNOST)
    return bottle.template("igra", igra=vislice.igre[id_igre][0], id_igre=id_igre)


@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNOST)
    crka = bottle.request.forms.getunicode("crka").upper()
    vislice.ugibaj(id_igre, crka)
    vislice.zapisi_igre_v_datoteko()
    return pokazi_igro()


@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    vislice.zapisi_igre_v_datoteko()
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNOST, path="/")
    bottle.redirect("/igra/")


# to naj bo na dnu
bottle.run(reloader=True, debug=True)