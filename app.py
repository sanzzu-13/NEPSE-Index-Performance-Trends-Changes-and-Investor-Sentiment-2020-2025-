from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Example: adjust based on how many inputs your model needs
            features = [float(request.form[f"feature{i}"]) for i in range(1, 5)]
            prediction = model.predict([features])[0]
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
