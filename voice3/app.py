from flask import Flask, jsonify
from flask import render_template, request, make_response
from utils import make_audio

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/make", methods=['POST'])  
def make():
    text   = request.form.get("text")
    rate   = request.form.get("rate", type=int)
    volume = request.form.get("volume", type=int)

    try: id = make_audio(text, rate, volume)
    except: return jsonify({"code": 400}), 400
    return jsonify({"code": 200, "id": id}), 200

@app.route("/audio/<id>.mp3")     
def get_audio(id):
    with open("audios/{}.mp3".format(id), "rb") as f:
        audio = f.read()

    response = make_response(audio)
    response.content_type = "audio/mpeg"

    return response

if __name__ == "__main__":
    app.run(debug=True)

