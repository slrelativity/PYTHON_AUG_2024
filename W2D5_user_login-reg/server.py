from flask_app import app
# ALWAYS IMPORT THE CONTROLLERS HERE!!!!
from flask_app.controllers import users_controller


if __name__ == "__main__":
    app.run(debug=True)