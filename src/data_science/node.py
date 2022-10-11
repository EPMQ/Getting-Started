import numpy as np
import pandas as pd

def nearest_neighbour(X_train, X_test):
  return np.sum((X_train_numpy[:, None, :] - X_test_numpy[None, :, :]) ** 2, axis=-1).argmin(axis=0)


def make_predictions(input_path: str, output_path: str) -> None:
    """Uses 1-nearest neighbour classifier to create predictions.

    Args:
        input_path: Path to directory containing features and target training and test sets.
        output_path: Path to directory where the predictions should be stored.
    """

    # TODO:
    # Step 1: Convert the training and test feature sets to numpy
    
    
    # Step 2: Call the nearest neighbour function with the numpy-converted training and test feature sets
    

    # Step 3: Use the result from the previous steps to select the respective rows from the training target set (tip: use .iloc[] function)

    
    # Step 4: Assign the index of test feature set to the result of the previous step.


    # Step 4: Store the result of the previous step in a `y_pred.csv` file inside `output_path`
    
    
# Do not edit!
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Data Science node.')
    parser.add_argument('input_path', type=str, help='Path to directory containing features and target sets')
    parser.add_argument('output_path', type=str, help='Path to directory where the predictions should be stored')

    args = parser.parse_args()
    make_predictions(input_path=args.input_path, output_path=args.output_path)
    
