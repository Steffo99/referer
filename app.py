import flask as f

app = f.Flask(__name__)


@app.route("/")
def root_page():
    return '<a href="/referer">Click on me!</a>'


@app.route('/referer')
def referer_page():
    referer = f.request.headers.get("Referer")
    if referer:
        return f"Referer: {referer}"
    else:
        return "No Referer header was sent."


if __name__ == '__main__':
    app.run()
