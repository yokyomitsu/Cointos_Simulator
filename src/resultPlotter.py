import numpy as np
import matplotlib.pyplot as plt

class ResultPlotter:
    @staticmethod
    def plot(results, n_tosses, compare_normal_distribution=False):
        # Plot a histogram of the results
        plt.hist(results, bins=np.arange(n_tosses + 2) - 0.5, density=True, alpha=0.75, color='blue')
        
        # Get the range of the actual data
        data_min = np.min(results)
        data_max = np.max(results)
        
        # Initialize plot limits based on actual data
        x_min, x_max = data_min - 1, data_max + 1

        if compare_normal_distribution:
            # Compute parameters of the theoretical normal distribution
            mu = n_tosses * 0.5  # Average
            sigma = np.sqrt(n_tosses * 0.5 * 0.5)  # Standard deviation

            # Generate the normal distribution curve
            x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)  # Capture most of the normal curve
            y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
            plt.plot(x, y, 'r-', lw=2, label='Normal Distribution')

            # Adjust x-axis limits to fit both data and theoretical distribution
            x_min = min(x_min, mu - 3 * sigma)
            x_max = max(x_max, mu + 3 * sigma)

        plt.title(f"Coin Toss Simulation: {len(results)} simulations, {n_tosses} tosses per set")
        plt.xlabel('Number of Heads')
        plt.ylabel('Probability')
        plt.legend()
        plt.grid(True)

        # Set the x-axis range to cover both actual data and theoretical distribution
        plt.xlim(x_min, x_max)


