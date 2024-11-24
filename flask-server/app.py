from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Member", "Member2", "Member3"]}


if __name__ == '__main__':
    app.run(debug= True)