from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
	return render_template('index.html')


@app.route("/pie")
def pie():
	return render_template('pie.html')


app.run()
