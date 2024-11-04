import os
import pandas as pd
import yaml
import matplotlib.pyplot as plt
from src.resultPlotter import ResultPlotter

# Plot the saved data in a directory
def plot_from_saved_data(directory):
    # Load the result csv
    results_file = os.path.join(directory, 'results.csv')
    if not os.path.exists(results_file):
        print(f"No results found in {directory}")
        return
    
    df = pd.read_csv(results_file)
    results = df['Number of Heads'].values

    # Get the parameter "n_tosses" form 
    config_file = os.path.join(directory, 'config.yaml')
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    n_tosses = config['n_tosses']

    # re-generate a plot from the saved data
    compare_normal_distribution = True
    plt.figure()
    ResultPlotter.plot(results, n_tosses, compare_normal_distribution)

# for test
def main():
    directory = input("Enter the directory of the saved results: ")    
    plot_from_saved_data(directory)

if __name__ == "__main__":
    main()
