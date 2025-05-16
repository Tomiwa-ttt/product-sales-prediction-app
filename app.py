from flask import Flask, request, jsonify
import joblib

# Save the trained model
joblib.dump(model, 'sales_prediction_model.pkl')

# Create Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('sales_prediction_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    ad_spend = data.get('Advertising Spend', 0)
    prediction = model.predict([[ad_spend]])
    result = {'Predicted Units Sold': int(prediction[0])}
    return jsonify(result)

# Run the app (this only works locally, not in Colab)
# app.run(debug=True)
