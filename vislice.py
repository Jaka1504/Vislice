import model, bottle


vislice = model.Vislice()


@bottle.get("/")
def osnovna_stran():
    return "index.tpl"


bottle.run(reloader=True, debug=True)