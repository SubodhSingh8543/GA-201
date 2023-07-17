from flask import Flask

app = Flask(__name__)

@app.route("/double/<int:num>")
def double(num):
    return int(num * 2)

if __name__ == "__main__":
    app.run()