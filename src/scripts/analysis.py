import pandas as pd
import os

def analyze_gapminder(input_file, output_file):
    """
    Analyze the Gapminder dataset and save the summary.
    """
    data = pd.read_csv(input_file)
    summary = data.groupby("continent")[["life_expectancy", "gdp_per_capita", "population"]].mean().reset_index()
    summary.to_csv(output_file, index=False)
    print(f"Analysis summary saved to {output_file}")

if __name__ == "__main__":
    input_file = "data/processed/cleaned_gapminder.csv"
    output_file = "results/tables/continent_summary.csv"
    os.makedirs("results", exist_ok=True)
    analyze_gapminder(input_file, output_file)
