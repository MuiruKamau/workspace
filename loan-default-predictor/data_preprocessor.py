import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle

def preprocess_data(df):
    # Handle missing values
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    numeric_imputer = SimpleImputer(strategy='median')
    df[numeric_columns] = numeric_imputer.fit_transform(df[numeric_columns])

    categorical_imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_columns] = categorical_imputer.fit_transform(df[categorical_columns])

    # Encode categorical variables
    label_encoders = {}
    for col in categorical_columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

    # Scale numeric features
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    # Save encoders and scaler
    with open('label_encoders.pkl', 'wb') as f:
        pickle.dump(label_encoders, f)
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    return df

def preprocess_user_input(user_input):
    # Load encoders and scaler
    with open('label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    # Encode categorical variables
    for col, le in label_encoders.items():
        if col in user_input:
            user_input[col] = le.transform([str(user_input[col])])[0]

    # Scale numeric features
    numeric_columns = user_input.select_dtypes(include=[np.number]).columns
    user_input[numeric_columns] = scaler.transform(user_input[numeric_columns].values.reshape(1, -1))

    return user_input