import bottle
import model


vislice = model.Vislice()


@bottle.get("/img/<file>")
def staticne_slike(file):
    return bottle.static_file(file, root="img")


@bottle.get("/")
def osnovna_stran():
    return bottle.template("index")


bottle.run(reloader=True, debug=True)