# Product Sales Prediction Web App (Python & Flask)

A simple machine learning-powered web app that predicts product sales based on advertising spend.

## Features
- Train and deploy a linear regression model.
- Build a Flask REST API for prediction serving.
- Frontend UI with HTML to input advertising spend and get predictions.
- Visualization of actual vs predicted sales.
- Ready for deployment on Render, Replit, or Railway.

## Files
- `dummy_sales_data.csv` - Sample dataset.
- `app.py` - Flask API code.
- `index.html` - Simple frontend UI.
- `sales_prediction_model.pkl` - Trained model.
- `sales_prediction_plot.png` - Model performance visualization.

## Technologies
Python, Flask, Scikit-learn, Pandas, Matplotlib, HTML

## Demo
API endpoint: `/predict` (accepts POST with JSON `{ "Advertising Spend": 500 }`)
