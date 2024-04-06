import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_predict(train_data_path, test_data_path):
  """
  Trains a Random Forest classifier model to predict chart type based on user data.

  Args:
      train_data_path: Path to the CSV file containing training data.
      test_data_path: Path to the CSV file containing test data.

  Returns:
      None
  """

  # Load training and test data
  data_train = pd.read_csv(train_data_path)
  data_test = pd.read_csv(test_data_path)

  # Now encode categorical features using LabelEncoder
  # Encode categorical features using LabelEncoder
  encoder = LabelEncoder()

  # Encode categorical variables
  for column in data_train.select_dtypes(include=['object']).columns:
    data_train[column] = encoder.fit_transform(data_train[column])

  # Separate features and target variable from encoded data
  features = data_train.drop('ChartType', axis=1)
  target = data_train['ChartType']

  # Train-Test Split (optional, you can use all data for training here)
  X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

  # Create and train the Random Forest classifier model
  model = RandomForestClassifier()
  model.fit(X_train, y_train)

  # Evaluate model accuracy on the testing set (if using train-test split)
  if X_test is not None and y_test is not None:
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy on Testing Set: {accuracy:.2f}")

  # Encode categorical features using LabelEncoder
  encoder = LabelEncoder()

  # Encode categorical variables
  for column in data_test.select_dtypes(include=['object']).columns:
    data_test[column] = encoder.fit_transform(data_test[column])
  
  # predicted_chart_type = model.predict(data_test)[3]


  chart_types = {
    0: 'Bar Chart',
    1: 'Line Graph',
    2: 'Pie Chart',
    3: 'Scatter Chart'
  }

  # Predict the chart type for each row in the test data
  for index, row in data_test.iterrows():
    prediction = model.predict(data_test)[index]
    print(f"Predicted Chart Type: {chart_types[prediction]}")

  # Print predicted chart type for the pair
  # predicted_chart = chart_types[predicted_chart_type]

  # Print the predicted chart type for the first data point in the test data
  # You can modify this loop to print predictions for all test data points
  # print(f"Predicted Chart Type for First Data Point in Test Data: {predicted_chart}")

# Example usage (replace paths with your actual file paths)
train_predict('user_train.csv', 'user_test.csv')
train_predict('user_train_2.csv', 'user_test_2.csv')
train_predict('user_train_3.csv', 'user_test_3.csv')
