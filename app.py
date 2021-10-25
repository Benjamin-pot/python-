from flask import Flask, render_template, request
app=Flask(__name__)

app.key_list = []

@app.route("/", methods=["GET"])
def index():   
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    key = request.form["key"]
    app.key_list.append(key)
    return render_template("index.html",Key=app.key_list)

@app.route('/tools', methods=["POST"])
def tools():
    tool = request.form["button"]

    if tool == 'clear':
        app.key_list = []
    return render_template("index.html",Key=app.key_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)