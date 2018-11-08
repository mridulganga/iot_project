from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/sensorvalue', methods=["POST"])
def sensorvalue_handler():
    gas = request.form["gas"]
    ldr = request.form["ldr"]
    humidity = request.form["humidity"]
    temperature = request.form["temperature"]
    # SAVE TO DB
    return "SUCCESS"

if __name__ == '__main__':
    app.run()