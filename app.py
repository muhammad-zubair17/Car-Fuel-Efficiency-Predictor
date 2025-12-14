from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle
import os

app = Flask(__name__)
CORS(app)

model = pickle.load(open('car_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    features = np.array([
        float(data['cylinders']),
        float(data['displacement']),
        float(data['horsepower']),
        float(data['weight'])
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return jsonify({'success': True, 'prediction': round(prediction, 2)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



