import pandas as pd
import os

def preprocess_gapminder(input_file, output_file):
    """
    Load, clean, and save the Gapminder dataset.
    """
    data = pd.read_csv(input_file)
    data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]  # Clean column names
    data = data.dropna()  # Remove rows with missing values
    data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    input_file = "data/raw/gapminder-FiveYearData_20241206.csv"
    output_file = "data/processed/cleaned_gapminder.csv"
    os.makedirs("data", exist_ok=True)
    preprocess_gapminder(input_file, output_file)

