from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    from waitress import serve
    # serve(app, host="0.0.0.0", port=5050)
    app.run(host="0.0.0.0", port=5050, debug=True)
