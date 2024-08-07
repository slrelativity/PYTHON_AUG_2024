from flask import Flask, render_template, redirect, request
app = Flask(__name__)

# bring in the model to talk to it
from dog_model import Dog

# ============ READ ALL ==========
@app.route("/")
def index():
    all_dogs = Dog.get_all()
    return render_template("dashboard.html", 
                           all_dogs=all_dogs)

# ============ CREATE PAGE (VIEW) ========
# /tablename/?id/action
@app.route("/dogs/create_page")
def create_dog_page() :
    return render_template("dog_new.html")

# ----------- CREATE METHOD (ACTION) ---------
@app.route("/dogs/create", methods=['post'])
def create_dog_form() :
    # print(">>>>>>>>>> inside submit create form <<<<<<")
    # print(request.form)
    Dog.create(request.form)
    return redirect("/")

# ----------- READ ONE PAGE --------------
# /tablename/id/action
@app.route("/dogs/<int:id>")
def one_dog_page(id):
    this_dog = Dog.get_one(id)
    return render_template("dog_show_one.html",
                           this_dog=this_dog)


# ------------ EDIT PAGE - UPDATE -----------------
# /tablename/id/action
@app.route("/dogs/<int:id>/update")
def update_dog_page(id):
    this_dog = Dog.get_one(id)
    return render_template("dog_update.html",
                           this_dog=this_dog)

# ------------ UPDATE ACTION form ------------
@app.route("/dogs/<int:id>/update_action", methods=['post'])
def update_dog_action(id):
    # prepare the data dict
    data = {
        **request.form,
        'id': id,
    }
    Dog.update(data)
    return redirect(f"/dogs/{id}")

            
if __name__ == "__main__":
    app.run(debug=True)