import flask as f

app = f.Flask(__name__)


@app.route("/")
def root_page():
    return f.render_template("root.html")


@app.route("/link")
def link_page():
    return f.render_template("link.html")


@app.route("/location/href")
def location_href_page():
    return f.render_template("locationhref.html")


@app.route("/location/replace")
def location_replace_page():
    return f.render_template("locationreplace.html")


@app.route('/referer')
def referer_page():
    referer = f.request.headers.get("Referer")
    if referer:
        return f"Referer: {referer}"
    else:
        return "No Referer header was sent."


if __name__ == '__main__':
    app.run()
