## Chart Type Prediction with Random Forest

**README.md**

This project implements a Random Forest classifier to predict the most suitable chart type (bar chart, line graph, pie chart, or scatter chart) based on user data.

## Key Features

* Leverages a Random Forest model for accurate chart type classification.
* Handles categorical features using LabelEncoder.
* Evaluates model performance using accuracy score.
* Generates predictions for individual data points.

## Prerequisites

* Python 3.x
* Libraries: pandas, sklearn

## Installation

1. Install required libraries using pip:

   ```bash
   pip install pandas sklearn
   ```

## Usage

1. Update the `train_predict` function calls by replacing the placeholder file paths with the actual paths to your training and test data (CSV files).
2. Run the script from the command line:

   ```bash
   python chart_prediction.py
   ```

## Code Structure

* **Import Libraries:** Imports necessary libraries: pandas, `train_test_split` from sklearn, LabelEncoder, RandomForestClassifier, and accuracy_score (all from sklearn).
* **`train_predict()` Function:**
    * Loads training and test data from CSV files using pandas.
    * Encodes categorical features using LabelEncoder.
    * Separates features and target variable from the encoded data.
    * Optionally performs a train-test split for model evaluation.
    * Creates and trains a Random Forest classifier model.
    * Evaluates model accuracy on the testing set (if a train-test split was performed).
    * Encodes categorical features in the test data.
    * Predicts chart types for each row in the test data using the trained model.
    * Prints the predicted chart types.
* **Example Usage:** Demonstrates how to use the `train_predict` function with sample file paths.

## Additional Notes

* Consider exploring hyperparameter tuning and feature engineering techniques for further model improvement.
* Depending on your specific use case, you might want to explore different evaluation metrics beyond accuracy score.
