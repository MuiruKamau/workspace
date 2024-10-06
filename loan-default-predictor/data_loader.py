import pandas as pd

def load_data():
    """
    Load the loan default dataset from CSV file.
    """
    try:
        df = pd.read_csv("Loan_default.csv")
        return df
    except FileNotFoundError as e:
        print(f"Error: {e}. The 'Loan_default.csv' file was not found. Please ensure it's in the correct directory.")
        raise
    except pd.errors.EmptyDataError as e:
        print("Error: The 'Loan_default.csv' file is empty.", e)
        raise ValueError("The 'Loan_default.csv' file is empty.")
    except pd.errors.ParserError as e:
        print("Error: Unable to parse 'Loan_default.csv'. Please check if it's a valid CSV file.", e)
        raise ValueError("Unable to parse 'Loan_default.csv'. Please check if it's a valid CSV file.")