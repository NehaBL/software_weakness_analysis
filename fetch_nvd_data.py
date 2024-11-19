import pandas as pd

# Load data from the CSV file in the data folder
def load_exploit_data():
    file_path = '../data/files_exploits.csv'
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        print(data.head())  # Print the first few rows for verification
        return data
    except FileNotFoundError:
        print("Error: CSV file not found. Make sure it is in the 'data' folder.")

# Example usage
if __name__ == "__main__":
    load_exploit_data()

