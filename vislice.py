import bottle
import model


vislice = model.Vislice()


@bottle.get("/")
def osnovna_stran():
    return bottle.template("index")


bottle.run(reloader=True, debug=True)