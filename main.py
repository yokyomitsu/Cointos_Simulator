import os
import shutil
import yaml
import pandas as pd
from datetime import datetime
from src.configLoader import YAMLConfigLoader
from src.coinTossSimulator import CoinTossSimulator
from src.resultPlotter import ResultPlotter
import matplotlib.pyplot as plt

def create_results_directory(config_file):
    # Add datetime to directory of results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dir_name = f"results_{timestamp}"

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Copy a setting file into this folder
    shutil.copy(config_file, os.path.join(dir_name, "config.yaml"))

    return dir_name

def main():
    # Load the settings
    config_file = 'config.yaml'
    yaml_loader = YAMLConfigLoader()
    config = yaml_loader.load(config_file)

    n_tosses = config['n_tosses']
    n_simulations = config['n_simulations']

    # Run the simulation
    simulator = CoinTossSimulator(n_tosses, n_simulations)
    results = simulator.simulate()

    # Create the directory to save the results
    results_dir = create_results_directory(config_file)

    # Save the results into csv
    results_file = os.path.join(results_dir, 'results.csv')
    df = pd.DataFrame(results, columns=['Number of Heads'])
    df.to_csv(results_file, index=False)

    print(f"Results saved in {results_dir}")

    plt.figure()
    ResultPlotter.plot(results, n_tosses, compare_normal_distribution=True)

    # Save the image ploted results
    plot_file = os.path.join(results_dir, 'plot.png')
    plt.savefig(plot_file)

    # Turn on if you want to see the result
    # plt.show()

    plt.close()

if __name__ == "__main__":
    main()
