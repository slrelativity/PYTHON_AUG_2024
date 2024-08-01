from flask import Flask, render_template 
app = Flask(__name__)


@app.route('/') 
def hello_world():
    return '<h2>Hello World!</h2><p> this is cool 😎 </p>'

@app.route("/cool")
def cool_route():
    print("I'm in the cool route!")
    return "this stuff is very cool!!!"

@app.route("/hello/<name>")
def greeting(name):
    print("hello " + name)
    return "hello " + name

@app.route("/hello/<name>/<int:times>")
def greeting_times(name, times):
    return f"you say hello to {name} for {times} times <br>" * times

@app.route("/hello/template")
def hello_template():
    return render_template("hello.jinja")


if __name__=="__main__":
    app.run(debug=True)