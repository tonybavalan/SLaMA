import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Function to preprocess data
def preprocess_data(df):
    # Replace missing values, encode categorical variables, etc.
    # For demonstration, let's assume no preprocessing is needed
    return df

# Function to train a machine learning model
def train_model(X_train, y_train, model_type):
    if model_type == 'Random Forest':
        clf = RandomForestClassifier()
    elif model_type == 'Gradient Boosting':
        clf = GradientBoostingClassifier()
    elif model_type == 'Logistic Regression':
        clf = LogisticRegression()
    clf.fit(X_train, y_train)
    return clf

# Function to visualize data with Matplotlib (scatter plot)
def visualize_data_matplotlib_scatter(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Matplotlib Scatter Plot')
    st.pyplot()

# Function to visualize data with Seaborn (scatter plot)
def visualize_data_seaborn_scatter(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column)
    plt.title('Seaborn Scatter Plot')
    st.pyplot()

# Function to visualize data with Plotly (scatter plot)
def visualize_data_plotly_scatter(df, x_column, y_column):
    fig = px.scatter(df, x=x_column, y=y_column)
    st.plotly_chart(fig)

# Function to visualize data with Plotly (pie chart)
def visualize_data_plotly_pie(df, column):
    fig = px.pie(df, names=column, values=df[column].value_counts())
    st.plotly_chart(fig)

# Function to visualize data with Plotly (bar plot)
def visualize_data_plotly_bar(df, x_column, y_column):
    fig = px.bar(df, x=x_column, y=y_column)
    st.plotly_chart(fig)

# Streamlit app
st.title('Dynamic Data Analysis with Machine Learning')

# File upload
file = st.file_uploader("Upload file", type=["xlsx", "xls", "csv"])
if file is not None:
    # Read the appropriate file format
    if file.type == "text/csv":
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Data preprocessing
    if st.checkbox("Perform Data Preprocessing"):
        df = preprocess_data(df)
        st.write("Data Preprocessing Completed.")
        st.write(df)

    # Feature selection
    st.subheader("Feature Selection")
    if len(df.columns) > 1:
        x_column = st.selectbox('Select X-axis column:', df.columns)
        y_column = st.selectbox('Select Y-axis column:', df.columns)

        # Visualization options based on data types
        st.subheader("Select Visualization Type")
        visualization_type = st.selectbox("Select Visualization Type", ["Matplotlib", "Seaborn", "Plotly Scatter", "Plotly Pie", "Plotly Bar"])

        # Visualize data based on selected visualization type
        if visualization_type == "Matplotlib":
            visualize_data_matplotlib_scatter(df, x_column, y_column)
        elif visualization_type == "Seaborn":
            visualize_data_seaborn_scatter(df, x_column, y_column)
        elif visualization_type == "Plotly Scatter":
            visualize_data_plotly_scatter(df, x_column, y_column)
        elif visualization_type == "Plotly Pie":
            visualize_data_plotly_pie(df, x_column)
        elif visualization_type == "Plotly Bar":
            visualize_data_plotly_bar(df, x_column, y_column)

    # Machine learning model training
    if st.checkbox("Train Machine Learning Model"):
        target_column = st.selectbox('Select target column:', df.columns)
        if target_column:
            X = df.drop(target_column, axis=1)
            y = df[target_column]
            
            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Select the machine learning model
            model_type = st.selectbox('Select model type:', ['Random Forest', 'Gradient Boosting', 'Logistic Regression'])
            
            # Train the model
            model = train_model(X_train, y_train, model_type)
            
            # Make predictions on the test set
            y_pred = model.predict(X_test)
            
            # Evaluate the model's performance
            accuracy = accuracy_score(y_test, y_pred)
            st.write(f'Model Accuracy: {accuracy:.2f}')
            st.text('Classification Report:')
            st.text(classification_report(y_test, y_pred))
            
            # Visualize feature importances (if applicable)
            if hasattr(model, 'feature_importances_'):
                st.subheader('Feature Importances')
                feature_importances = pd.Series(model.feature_importances_, index=X.columns)
                fig, ax = plt.subplots()
                feature_importances.nlargest(10).plot(kind='barh')
                st.pyplot(fig)

    # Prediction analysis section
    st.subheader('Prediction Analysis')
    if st.checkbox('Make Predictions on New Data'):
        # User inputs for new data
        input_data = {}
        for column in X.columns:
            input_value = st.text_input(f'Enter value for {column}:', '')
            input_data[column] = input_value
        
        if st.button('Predict'):
            # Convert input data to DataFrame
            input_df = pd.DataFrame([input_data])
            
            # Make prediction
            prediction = model.predict(input_df)
            st.write(f'The predicted value for the target is: {prediction[0]}')
