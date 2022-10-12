import pandas as pd


def split_data(input_path: str, output_path: str, train_fraction: float) -> None:
    """Splits data into features and target training and test sets.

    Args:
        input_path: Path to csv file containing features and target.
        output_path: Path to directory where the training and test sets should be stored
        train_fraction: Fraction of the dataset allocated to the training set.
    """

    # TODO:
    # Step 1: Read data from csv file (using Pandas)
    
    
    # Step 2: Split the data into training and test sets. Use argument `train_fraction` to define the size of the training set.
    
    
    # Step 3: Split the training data into features and targets (X_train and Y_train respectively). The target column is `species`.
    
    
    # Step 4: Repeat Step 3 to the test data.
    
    
    # Step 5: Save X_train, X_test, Y_train, Y_test to output_path as ´X_train.csv´, `X_test.csv`, `Y_train.csv`, and `Y_test.csv` respectively.
    
    
    
# Do not edit!
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Data Engineering node.')
    parser.add_argument('input_path', type=str, help='Path to csv file containing features and target')
    parser.add_argument('output_path', type=str, help='Path to directory where the training and test sets should be stored')
    parser.add_argument('train_fraction', type=float, help='Fraction of the dataset allocated to the training set')

    args = parser.parse_args()
    split_data(input_path=args.input_path, output_path=args.output_path, train_fraction=args.train_fraction)
