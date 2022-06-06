# Python/Docker exercise

The goal of this exercise is to familiarize oneself with orchestrating a ML pipeline using docker containers, similarly to how kubeflow operates.

For the purpose of this exercise, we will use Kedro's [iris dataset example](https://kedro.readthedocs.io/en/stable/02_get_started/05_example_project.html).

## Pre-requisites
This exercise assumes you are familiarized with docker and pipeline concepts. Also, it assumes you have docker and python installed on your machine.



## Installing iris dataset example project


1. Clone this repository: `git clone https://github.com/ArthurMatta/python-docker-exercise.git`
2. Move to the new folder created for this repository: `cd python-docker-exercise`
3. Install the base requirements: `pip install -r requirements.txt`
4. Initialize the iris dataset example: `kedro new --config=kedro.config.yaml --starter=pandas-iris`
   

## Exercise

The purpose of this exercise is to closely familiarize onself with docker, pipeline concepts, and kubeflow-like workflow.

The objective of this exercise is to, using the iris dataset example project, adapt it so that each node is executed as a docker container.

To avoid mixing projects, it's recommended that you create a different folder for this exercise. Your folder structure should look similar to this:
```
iris/
| - ...
exercise/
| - src/
| - - data_engineering/
| - - - node.py
| - - - Dockerfile
| - - - requirements.txt
| - - data_science/
| - - - node.py
| - - - Dockerfile
| - - - requirements.txt
| - data/
| - - 01_raw/
| - - - iris.csv
| - - 02_intermediate/
| - - 03_final/
```

This exercise consists mainly in creating 2 docker containers to be execute sequentially. The containers must be an adaptation from the 2 parts of the pipeline defined by the iris dataset project. Each container should perform the following operations:

1. Data Engineering
   - Mount a volume binding local folder `data/` to a container folder `data/`
    - Copy local folder `src/data_engineering/` to container folder `src/`
    - Install the requirements `pip install -r src/requirements.txt`
    - Run the python script `src/node.py` (containing the adapted split_data function from `iris/src/iris/pipelines/data_engineering/nodes.py`). The script should receive 3 command line arguments (tip: check the [argparse](https://docs.python.org/3/library/argparse.html) library): input_file, output_folder, split_ratio.
      - *input_file* [string]: path to the iris.csv file (should be `data/01_raw/iris.csv`)
      - *output_folder* [string]: path to the output folder (should be `data/02_intermediate/`) where the 4 output files (train_x.csv, train_y.csv, test_x.csv, and test_y.csv) will be stored.
      - *split_ratio* [float]: split ratio parameter used to split the input data (should be a value between 0.0 and 1.0 and with 1 decimal place).
       - Example of command: `python src/node.py --input_file data/01_raw/iris.csv --output_folder data/02_intermediate --split_ratio 0.2`
  
2. Data Science
    - Mount a volume binding local folder `data/` to a container folder `data/`
    - Copy local folder `src/data_science/` to container folder `src/`
    - Install the requirements `pip install -r src/requirements.txt`
    - Run the python script `src/node.py` (containing the adapted split_data function from `iris/src/iris/pipelines/data_science/nodes.py`). **For the purpose of this exercise it's enough to adapt only the `train_model` function**. The script should receive 4 command line arguments: input_folder, output_file, num_train_iter, and learning_rate.
      - *input_folder* [string]: path to the folder where the outputs from previous container were stored (should be `data/02_intermediate/`)
      - *output_file* [string]: path to the file to save the output from the script. (should be `data/03_final/models.csv`) **Note that the output must be converted to a csv file**.
      - *num_train_iter* [integer]: number of training iterations parameter (e.g. 10000).
      - *learning_rate* [float]: model learning rate parameter (should be a value value between 0 an 1 with up to 3 decimal places, e.g. 0.01).
       - Example of command: `python src/node.py --input_folder data/02_intermediate --output_file data/03_final/models.csv --num_train_iter 10000 --learning_rate 0.01`


