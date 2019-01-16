from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/story')
def hello_worlds():
    return render_template("story.html")

@app.route('/schedule')
def hello_schedule():
    return render_template("schedule.html")


@app.route('/registry')
def hello_registry():
    return render_template("registry.html")

@app.route('/fun')
def hello_fun():
    return render_template("fun.html")

@app.route('/rsvp')
def hello_rsvp():
    return render_template("rsvp.html")


@app.route('/accomodations')
def hello_hotel():
    return render_template("accomodations.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
