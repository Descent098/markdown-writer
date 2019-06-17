from flask import Flask,redirect, render_template,url_for
import os
app = Flask(__name__, template_folder='static/templates')

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.static_folder = 'static' # Allows absolute paths to folders inside static
    env_port = int(os.environ.get('PORT', 5000)) # Grabs port from Heroku Dynamo environment variables, else sets to 5000
    app.run(host="0.0.0.0", port=env_port)
