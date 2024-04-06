import pandas as pd
import streamlit as st
import sqlalchemy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import plotly.graph_objs as go

# Function to retrieve data from the database
def retrieve_data(uri, query):
    try:
        engine = sqlalchemy.create_engine(uri)
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        return None

# Function for data preprocessing
def preprocess_data(df):
    # Assuming 'target_column' is the last column in the dataframe
    # Separate features and target
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Convert scaled features back to DataFrame
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
    
    return X_scaled_df, y

# Function for data visualization
def visualize_data(df):
    st.subheader("Data Visualization")
    # Interactive 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=df[df.columns[0]],
        y=df[df.columns[1]],
        z=df[df.columns[2]],
        mode='markers',
        marker=dict(
            size=5,
            color=df[df.columns[-1]], # set color to an array/list of desired values
            colorscale='Viridis',   # choose a colorscale
            opacity=0.8
        )
    )])
    st.plotly_chart(fig)

# Function to train a machine learning model
def train_model(X_train, y_train, model_type, **kwargs):
    if model_type == 'Logistic Regression':
        model = LogisticRegression(**kwargs)
    elif model_type == 'Random Forest':
        model = RandomForestClassifier(**kwargs)
    elif model_type == 'SVM':
        model = SVC(**kwargs)
    model.fit(X_train, y_train)
    return model

# Function for prediction analysis
def predict(model, X_test):
    return model.predict(X_test)

# Main function
def main():
    st.title("Dynamic Data Analysis with Database Integration")

    # Database connection
    uri = st.text_input("Enter database URI:")
    query = st.text_area("Enter SQL query to fetch data:")

    if st.button("Fetch Data"):
        if uri and query:
            df = retrieve_data(uri, query)
            if df is not None:
                st.write(df.head())

                # Data preprocessing
                X, y = preprocess_data(df)

                # Data visualization
                visualize_data(pd.concat([X, y], axis=1))

                # Select target column
                target_column = y.name

                # Select features
                features = X.columns.tolist()

                # Splitting data into features and target
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Model selection
                model_type = st.selectbox("Select model type:", ["Logistic Regression", "Random Forest", "SVM"])

                # Model parameters
                if model_type == 'Random Forest':
                    n_estimators = st.slider("Number of estimators:", min_value=10, max_value=100, value=50)
                    max_depth = st.slider("Max depth:", min_value=1, max_value=20, value=10)
                    model = train_model(X_train, y_train, model_type, n_estimators=n_estimators, max_depth=max_depth)
                elif model_type == 'SVM':
                    C = st.slider("C (Regularization parameter):", min_value=0.01, max_value=10.0, value=1.0)
                    kernel = st.selectbox("Kernel type:", ["linear", "poly", "rbf", "sigmoid"])
                    model = train_model(X_train, y_train, model_type, C=C, kernel=kernel)
                else:
                    model = train_model(X_train, y_train, model_type)

                # Model evaluation
                y_pred = predict(model, X_test)
                accuracy = accuracy_score(y_test, y_pred)
                st.write(f"Model Accuracy: {accuracy:.2f}")

                # Confusion matrix
                cm = confusion_matrix(y_test, y_pred)
                st.write("Confusion Matrix:")
                st.write(cm)

if __name__ == "__main__":
    main()
