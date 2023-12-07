from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/pie")
def pie():
    return render_template('pie.html')


if __name__ == "__main__":
    app.run(debug=True)
