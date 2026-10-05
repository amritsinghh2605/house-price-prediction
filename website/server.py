from flask import Flask, request, jsonify
import joblib

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return app.send_static_file("index.html")
model = joblib.load("../model/house_price_model.pkl")
for i, name in enumerate(model.feature_names_in_, 1):
    print(i, name)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    bedrooms = float(data["bedrooms"])
    bathrooms = float(data["bathrooms"])
    living_area = float(data["living_area"])
    lot_area = float(data["lot_area"])
    floors = float(data["floors"])

    prediction = model.predict([[
        bedrooms,
        bathrooms,
        living_area,
        lot_area,
        floors
    ]])

    return jsonify({"price": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)