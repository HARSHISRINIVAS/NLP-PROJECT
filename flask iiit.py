from  flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("PYTHON IIIT.py")
if __name__ == '__main__':
    app.run(debug= True,port=5000)
