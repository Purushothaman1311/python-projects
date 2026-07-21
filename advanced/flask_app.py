from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return "<h2>Contact Page</h2><p>Email: example@gmail.com</p>"

if __name__ == "__main__":
    app.run(debug=True)
