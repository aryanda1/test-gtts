from flask import Flask,request,send_file,jsonify
from flask_cors import CORS
from gtts import gTTS
import os

app = Flask(__name__)
# cors = CORS(app,resources={r'/api/*':{'origins':'https://anime-link-gen.vercel.app'}})
cors = CORS(app,resources={r'/api/*':{'origins':'*'}})

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/convert', methods=['POST'])
def convert_text_to_audio():
    text = request.form['text']

    # Convert text to audio using gTTS with WAV file format
    obj = gTTS(text = text)    
    obj.save('audio.wav')

    # Send the audio file as a response with WAV mimetype
    return send_file('audio.wav', mimetype='audio/wav')

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))
