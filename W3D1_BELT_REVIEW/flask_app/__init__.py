from flask import Flask
app = Flask()
# for session we need a sercet key
app.secret_key = "wesirduhfguiawer39iouaqr345weghtu9iqa"
DATABASE="parties_db"