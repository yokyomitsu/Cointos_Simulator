import numpy as np

class CoinTossSimulator:
    def __init__(self, n_tosses, n_simulations):
        self.n_tosses = n_tosses
        self.n_simulations = n_simulations

    def simulate(self):
        return np.random.binomial(self.n_tosses, 0.5, self.n_simulations)
    
# for test method.
def main():
    n_tosses = 10
    n_simulations = 100

    # run a simulation
    simulator = CoinTossSimulator(n_tosses, n_simulations)
    results = simulator.simulate()

    # print the result（debug）
    print(f"Number of tosses per simulation: {n_tosses}")
    print(f"Number of simulations: {n_simulations}")
    print(f"Simulation results (first 10): {results[:10]}")
    print(f"Mean of results: {results.mean()}")
    print(f"Standard deviation of results: {results.std()}")

if __name__ == "__main__":
    main()