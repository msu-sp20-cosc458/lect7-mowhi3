import flask
import random
import os

app = flask.Flask(__name__)

@app.route("/")
def index(): 
    ran_num = random.randint(1, 100)
    return "<h1>" + str(ran_num) + "</h1>"
app.run(
    port=int(os.getenv("PORT", 8080)),
    host=os.getenv("IP", "0.0.0.0"),
    debug=True
)