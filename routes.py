from flask import Flask,redirect, render_template,url_for, request
import os
app = Flask(__name__, template_folder='static/templates')

@app.route('/')
def home():
    return redirect(url_for("create"))

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        print("Heading: {}".format(request.form['Heading']))
        print("Sub-Heading: {}".format(request.form['sub-heading']))
        print("Category: {}".format(request.form['category']))
        print("Content: {}".format(request.form['content']))
    return render_template("create.html")

if __name__ == '__main__':
    app.static_folder = 'static' # Allows absolute paths to folders inside static
    env_port = int(os.environ.get('PORT', 5000)) # Grabs port from Heroku Dynamo environment variables, else sets to 5000
    app.run(host="0.0.0.0", port=env_port)
