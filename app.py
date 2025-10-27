from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask App
app = Flask(__name__)

# Load model dict and scaler
model_dict = pickle.load(open("model/diabetes_model.pkl", "rb"))
model = model_dict['model']                     # Extract model
threshold = model_dict.get('threshold', 0.5)   # Use stored threshold or default
scaler = pickle.load(open("model/scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        inputs = [float(x) for x in request.form.values()]
        features = np.array(inputs).reshape(1, -1)
        features_scaled = scaler.transform(features)
        
        # Predict probability for positive class
        prob = model.predict_proba(features_scaled)[:, 1][0]
        
        # Determine output and class for styling
        if prob >= threshold:
            output = "Diabetic"
            output_class = "diabetic"
        else:
            output = "Non-Diabetic"
            output_class = "healthy"

        return render_template(
            'result.html',
            prediction_text=f"The patient is likely {output}.",
            output_class=output_class
        )
    except Exception as e:
        return render_template(
            'result.html',
            prediction_text=f"Error: {e}",
            output_class="healthy"
        )

if __name__ == "__main__":
    app.run(debug=True)
