from flask import Flask, render_template, request
from src.inference import run

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":
        i1=request.form['inp1']
        i2=request.form['inp2']
        i3=request.form['inp3']
        i4=request.form['inp4']

        pred = run([[i1,i2,i3,i4]])
        return render_template("index.html", pred=pred)

    return render_template("index.html")

if __name__ == "__main__":

    app.run(port=5001, debug=True)