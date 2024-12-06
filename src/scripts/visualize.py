import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def visualize_gapminder(input_file, results_dir):
    """
    Generate visualizations for the Gapminder dataset.
    """
    data = pd.read_csv(input_file)
    
    # Life Expectancy Over Time
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="year", y="life_expectancy", hue="continent", marker="o")
    plt.title("Life Expectancy Over Time by Continent")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend(title="Continent")
    life_expectancy_plot = f"{results_dir}/life_expectancy_over_time.png"
    plt.savefig(life_expectancy_plot)
    plt.show()
    print(f"Life expectancy plot saved to {life_expectancy_plot}")
    
    # GDP per Capita Distribution
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x="continent", y="gdp_per_capita")
    plt.title("GDP per Capita Distribution by Continent")
    plt.xlabel("Continent")
    plt.ylabel("GDP per Capita")
    gdp_plot = f"{results_dir}/gdp_per_capita_distribution.png"
    plt.savefig(gdp_plot)
    plt.show()
    print(f"GDP per capita plot saved to {gdp_plot}")

if __name__ == "__main__":
    input_file = "data/processed/cleaned_gapminder.csv"
    results_dir = "results/figures/"
    os.makedirs(results_dir, exist_ok=True)
    visualize_gapminder(input_file, results_dir)

