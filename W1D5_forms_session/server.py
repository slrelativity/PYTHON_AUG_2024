from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# secret key to store session
app.secret_key = "SHHH NO SECRETS ON GITHUB!!"

# DISPLAYS THE FORM
@app.route('/')
def index():
    return render_template("index.html")

# FORM SUBMIT IS AN ACTION
@app.route("/create_spaceship", methods=['post'])
def create_spaceship_action():
    print("=== inside form submit ===")
    print(f"\n-----\n{request.form}\n-----\n")
    print(request.form['spaceship_name'])
    print(request.form['fuel_level'])
    print(request.form['number_of_astronauts'])
    print("================")
    print("CHARGING YOUR CREDIT CARD!!!")
    print("================")
    # ! NEVER EVER EVER EVER EVER EVER RENDER ON A POST

    # CREATE SESSION DICT
    session['spaceship_name'] = request.form['spaceship_name']
    session['fuel_level'] = request.form['fuel_level']
    session['number_of_astronauts'] = request.form['number_of_astronauts']
    return redirect("/display")

@app.route("/display")
def display():
    print("======>>> inside /display <<<======")
    print(f"\n-----\n{session}\n-----\n")
    print({session['spaceship_name']})
    print({session['fuel_level']})
    print({session['number_of_astronauts']})
    print("======>>> inside /display <<<======")
    return render_template("display.html")

@app.route("/clear")
def clear_session() :
    # session.pop("spaceship_name")
    # del session['spaceship_name']
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)