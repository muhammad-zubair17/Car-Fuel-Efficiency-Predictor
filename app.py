from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
