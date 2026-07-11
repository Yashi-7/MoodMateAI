from flask import Flask, request, jsonify
import pickle
from preprocess import preprocess_text
from recommendation import emotion_data
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

emotion_map = {
    0: "sadness",
    1: "anger",
    2: "love",
    3: "surprise",
    4: "fear",
    5: "joy"
}

@app.route("/")
def home():
    return "MoodMate AI Backend is Running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    text = data["text"]

    text = preprocess_text(text)

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    probabilities = model.predict_proba(text_vector)[0]

    confidence = max(probabilities) * 100


    if confidence >= 80:
        confidence_message = "Very confident"

    elif confidence >= 60:
        confidence_message = "Moderately confident"

    else:
        confidence_message = "Low confidence"


    emotion = emotion_map[prediction]


    return jsonify({

        "emotion": emotion,

        "emoji": emotion_data[emotion]["emoji"],

        "confidence": round(confidence,2),

        "confidence_message": confidence_message,

        "quote": emotion_data[emotion]["quote"],

        "songs": emotion_data[emotion]["songs"]

    })


if __name__ == "__main__":
    app.run(debug=True)