from flask import Flask, render_template, request
app = Flask(__name__)

gas=0
ldr=0
humidity = 0
temperature = 0

@app.route('/')
def hello():
    global gas,ldr,humidity, temperature
    # gas = 10
    # ldr = 300
    # humidity = 20
    # temperature = 50
    return render_template("home.html", gas=gas, ldr=ldr, humidity=humidity, temperature=temperature)

@app.route('/s')
def sensor_vals():
    global gas,ldr,humidity, temperature
    # gas = 10
    # ldr = 300
    # humidity = 20
    # temperature = 50
    return render_template("s.html", gas=gas, ldr=ldr, humidity=humidity, temperature=temperature)

@app.route('/sensorvalue', methods=["POST"])
def sensorvalue_handler():
    global gas,ldr,humidity, temperature
    gas = request.form["gas"]
    ldr = request.form["ldr"]
    humidity = request.form["humidity"]
    temperature = request.form["temperature"]
    # SAVE TO DB

    return "SUCCESS"

if __name__ == '__main__':
    app.run()