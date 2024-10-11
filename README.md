# Optimization Algorithms Comparison Exercise

## Problem Statement

Welcome to your first optimization task as part of the ML team! In this exercise, you will compare the performance of different optimization algorithms on a set of benchmark functions. Your goal is to test various algorithms on well-known mathematical functions, and determine which algorithm consistently performs the best in minimizing these functions.

### Overview

You are provided with a set of 12 optimization test functions, each of which represents a different type of challenge (e.g., unimodal, multimodal, separable, non-separable). Your task is to implement and compare the performance of several optimization algorithms, drawn from different Python libraries, to minimize these functions.

### Task Breakdown

1. **Test Functions**: The test functions you need to work on are:
   - **Sphere**
   - **Rosenbrock**
   - **Ackley**
   - **Rastrigin**
   - **Griewank**
   - **Schwefel**
   - **Levy**
   - **Beale**
   - **Booth**
   - **Himmelblau**
   - **Easom**
   - **Michalewicz**

   Each function has a specific mathematical form that defines the optimization problem. For each function, you will evaluate the algorithm's ability to minimize it, across different dimensions (number of variables).

2. **Algorithms**: You need to use more than one of the following optimization algorithms:
   - **Pymoo Algorithms**:
     - Genetic Algorithm (GA)
     - Differential Evolution (DE)
     - Particle Swarm Optimization (PSO)
     - Covariance Matrix Adaptation Evolution Strategy (CMAES)
   - **SciPy Algorithms**:
     - Nelder-Mead
     - BFGS
     - Powell
     - Simulated Annealing (`dual_annealing` from SciPy)
   - **Nevergrad Algorithms**:
     - OnePlusOne
     - NGOpt
   - **Optuna**:
     - Tree-structured Parzen Estimator (TPE)

3. **Objective**: For each algorithm, you need to:
   - **Implement the algorithm** using existing implementations in the libraries mentioned.
   - **Run the algorithm** on each test function with a fixed number of dimensions (let's say **5**).
   - **Compare results**: Determine which algorithm produces the best minimum value for each function.
   - **Track performance**: Count how many times each algorithm outperforms the others across all test cases.

4. **Comparison Criteria**:
   - **Best Solution**: For each function, the algorithm that finds the lowest function value (global minimum) should be considered the winner.
   - **Consistency**: Determine which algorithm consistently performs well across the different test functions.

### Instructions

1. **Implement the Test Functions**: Start by implementing each of the 12 test functions in Python. These functions will take an input vector and return the corresponding objective value.

2. **Implement the Algorithms**: Use the following libraries to implement or wrap the optimization algorithms:
   - **Pymoo**: Provides several evolutionary and swarm-based algorithms.
   - **SciPy**: Provides general-purpose optimization methods, including `dual_annealing` for Simulated Annealing.
   - **Nevergrad**: Offers evolutionary algorithms such as `OnePlusOne` and more sophisticated methods like `NGOpt`.
   - **Optuna**: A library focused on hyperparameter optimization but can be used for general-purpose optimization via the TPE method.

3. **Run Comparisons**:
   - Use a consistent setup for all algorithms: number of generations, population sizes, and stopping criteria.
   - For each function, track the minimum value returned by each algorithm.
   - For each function, determine which algorithm found the best solution and track the number of times each algorithm "won".

4. **Report the Results**:
   - Print the winning algorithm for each function.
   - Display the overall performance, showing how many times each algorithm won across all functions.

### Requirements

- Use Python 3 and install the following libraries:
  - `pymoo`
  - `scipy`
  - `nevergrad`
  - `optuna`
  
  Install via pip if necessary:
  ```bash
  pip install pymoo scipy nevergrad optuna
