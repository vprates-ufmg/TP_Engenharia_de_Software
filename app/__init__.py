from quart import Quart

app = Quart(__name__)

nomes = ["Joao", "Pedro", "Antonio"]

@app.route("/prof")
def list_teachers():
    return nomes

@app.route("/prof/<name>")
def retorna_re(name):
    if name in nomes:
        return "Achou"
    else:
        return app.redirect("/prof")

if __name__ == "__main__":
    app.run(debug=True)