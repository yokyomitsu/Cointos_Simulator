import numpy as np
import matplotlib.pyplot as plt

class ResultPlotter:
    @staticmethod
    def plot(results, n_tosses, compare_normal_distribution=False):
        # Plot a histgram
        plt.hist(results, bins=np.arange(n_tosses+2)-0.5, density=True, alpha=0.75, color='blue')
        
        # Get the range of the data
        data_min = np.min(results)
        data_max = np.max(results)

        if compare_normal_distribution:
            # Compare an actual data with the theoretical normal distribution.
            mu = n_tosses * 0.5  # Averages
            sigma = np.sqrt(n_tosses * 0.5 * 0.5)  # Standard deviation
            x = np.arange(0, n_tosses+1, 0.1)
            y = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
            plt.plot(x, y, 'r-', lw=2, label='Normal Distribution')

        plt.title(f"Coin Toss Simulation: {len(results)} simulations, {n_tosses} tosses per set")
        plt.xlabel('Number of Heads')
        plt.ylabel('Probability')
        plt.legend()
        plt.grid(True)
        
        # Set the x-axis range to fit min and max of the data
        plt.xlim(data_min - 1, data_max + 1)
