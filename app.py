from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelos entrenados
classification_model = joblib.load("src/classification_model.pkl")
regression_model = joblib.load("src/regression_model.pkl")

@app.route("/predict_risk", methods=["POST"])
def predict_risk():
    data = request.get_json()

    # Convertir datos a arreglo numpy
    features = np.array([list(data.values())]).astype(float)

    # Predicción con modelo de clasificación
    prediction = classification_model.predict(features)[0]

    return jsonify({"riesgo_predicho": str(prediction)})

@app.route("/predict_recovery", methods=["POST"])
def predict_recovery():
    data = request.get_json()

    # Convertir datos a arreglo numpy
    features = np.array([list(data.values())]).astype(float)

    # Predicción con modelo de regresión
    prediction = regression_model.predict(features)[0]

    return jsonify({"recuperacion_esperada": float(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
