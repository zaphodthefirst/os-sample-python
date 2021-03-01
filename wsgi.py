from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Go Fuck yourself Sandiego!"

if __name__ == "__main__":
    application.run()
