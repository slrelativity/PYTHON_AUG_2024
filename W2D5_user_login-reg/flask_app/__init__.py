from flask import Flask
app = Flask(__name__)
# for session we need a sercet key
app.secret_key = "wesirduhfguiawer39iouaqr345weghtu9iqa"
DATABASE="users_login-reg"