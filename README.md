# Python & Docker exercise

The goal of this exercise is to orchestrate a ML pipeline using docker containers.

## Pre-requisites
This exercise assumes you are familiarized with docker and pipeline concepts. Also, it assumes you have docker and python installed on your machine.

## Exercise

The objective of this exercise is to adapt a dummy ML pipeline so that each node is executed in a docker container. The pipeline consists of 2 nodes: `data engineering` and `data science`. **Therefore, this exercise will consists of 2 docker containers, one for each node**. The subsections bellow describes what is espected from each container.

1. Data Engineering

   The data engineering container will load the raw dataset and split the data into feature and target training and test sets.
   
   Steps to execute this node:
   The [src/data_engineering/node.py](https://github.com/EPMQ/Getting-Started/blob/pydocker/src/data_engineering/node.py) file contains a template of the function with step by step instructions of what should be done by that node.
   
   Steps to build this container:
   - Mount a volume binding local directory `data/` to a container directory `data/`
   - Copy local directory `src/data_engineering/` to container directory `src/`
   - Install the requirements `pip install -r src/requirements.txt`
   - Run the python script `src/node.py`. The script should receive 3 command line arguments: input_path, output_path, train_fraction.
      - *input_path* [string]: path to the iris.csv file (should be `data/raw/iris.csv`)
      - *output_path* [string]: path to the output folder (should be `data/intermediate/`) where the 4 output files (X_train.csv, X_test.csv, Y_train.csv, and Y_test.csv) will be stored.
      - *train_fraction* [float]: Fraction of the dataset allocated to the training set (should be a value between 0.0 and 1.0 and with 1 decimal place).
      - Example of command: `python src/node.py data/raw/iris.csv data/intermediate 0.8`
  
2. Data Science

    The data science container will train a dummy machine learning algorithm and perform some predictions.
    
    Steps to execute this node:
    The [src/data_science/node.py](https://github.com/EPMQ/Getting-Started/blob/pydocker/src/data_science/node.py) file contains a template of the function with step by step instructions of what should be done by that node.

    Steps to build this container:
    - Mount a volume binding directory `data/` to a container directory `data/`
    - Copy local directory `src/data_science/` to container directory `src/`
    - Install the requirements `pip install -r src/requirements.txt`
    - Run the python script `src/node.py`. The script should receive 2 command line arguments: input_path, output_path, num_train_iter, and learning_rate.
      - *input_path* [string]: Path to directory containing features and target training and test sets. (should be `data/intermediate/`)
      - *output_path* [string]: Path to directory where the predictions should be stored. (should be `data/final`)
       - Example of command: `python src/node.py data/intermediate data/final`
