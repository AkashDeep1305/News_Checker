from flask import Flask, request, jsonify
import tensorflow as tf
import pickle
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = tf.keras.models.load_model("backend/news_model.h5")
vectorizer = pickle.load(open("backend/vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Convert text to numerical format
    transformed_text = vectorizer.transform([text]).toarray()
    prediction = model.predict(transformed_text)

    # Return result
    result = "Real" if prediction[0][0] > 0.6 else "Fake"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=False, port=50)
