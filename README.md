# Python & Docker exercise

The goal of this exercise is to orchestrate a ML pipeline using docker containers.

For the purpose of this exercise, we will use Kedro's [iris dataset example](https://kedro.readthedocs.io/en/0.17.6/02_get_started/05_example_project.html).

## Pre-requisites
This exercise assumes you are familiarized with docker and pipeline concepts. Also, it assumes you have docker and python installed on your machine.


## Installing iris dataset example project


1. Clone this repository: `git clone https://github.com/EPMQ/Getting-Started.git`
2. Move to the new folder created for this repository: `cd Getting-Started`
3. Change to the exercise directory: `git checkout pydocker`
4. Install the base requirements: `pip install -r requirements.txt`
5. Initialize the iris dataset example: `kedro new --config=kedro.config.yaml --starter=pandas-iris`. After executing this command, a new directory named `iris` is created with the following contents (check by executing `ls iris`):

```
iris         # Parent directory of the template
├── conf            # Project configuration files
├── data            # Local project data (not committed to version control)
├── docs            # Project documentation
├── logs            # Project output logs (not committed to version control)
├── notebooks       # Project related Jupyter notebooks (can be used for experimental code before moving the code to src)
├── README.md       # Project README
├── setup.cfg       # Configuration options for `pytest` when doing `kedro test` and for the `isort` utility when doing `kedro lint`
└── src             # Project source code
```
   
6. Create a new directory to store the source code for this project: `mkdir pydocker`
7. Move to the newly created directory and create `src` and `data` directories: `cd pydocker` and `mkdir src data`
8. Move to the data directory and create `raw`, `intermediate` and `final` directories: `cd data` and `mkdir raw intermediate final`. These directories will hold the data you will use for this exercise.
9. Move out of the `data` directory back into the root of the project: `cd ../..`
10. Copy the contents from `iris/src` to `pydocker/src`: `cp iris/src/* pydocker/src/`
11. You can now delete the iris directory and move back to the pydocker directory: `rm -r iris` and `cd pydocker`
13. Next, we will begin the exercise. Good luck! :)

## Exercise

The objective of this exercise is to adapt the template pipeline from Kedro so that each node is executed in a docker container. The template pipeline consists of 2 nodes: `data engineering` and `data science`. **Therefore, this exercise will consists of 2 docker containers, one for each node**. The subsections bellow describes what is espected from each container.

1. Data Engineering

   The data engineering container will load the raw dataset and perform some pre-processing operations to clean the data and prepare it for the data science phase.
   
   Steps to build this container:
   - Mount a volume binding directory `data/` to a container directory `data/`
   - Copy local folder `src/data_engineering/` to container folder `src/`
   - Install the requirements `pip install -r src/requirements.txt`
   - Run the python script `src/node.py` (containing the adapted split_data function from `iris/src/iris/pipelines/data_engineering/nodes.py`). The script should receive 3 command line arguments (tip: check the [argparse](https://docs.python.org/3/library/argparse.html) library): input_file, output_folder, split_ratio.
      - *input_file* [string]: path to the iris.csv file (should be `data/01_raw/iris.csv`)
      - *output_folder* [string]: path to the output folder (should be `data/02_intermediate/`) where the 4 output files (train_x.csv, train_y.csv, test_x.csv, and test_y.csv) will be stored.
      - *split_ratio* [float]: split ratio parameter used to split the input data (should be a value between 0.0 and 1.0 and with 1 decimal place).
       - Example of command: `python src/node.py --input_file data/01_raw/iris.csv --output_folder data/02_intermediate --split_ratio 0.2`
  
2. Data Science

    The data science container will train a dummy machine learning algorithm and perform some predictions.

    Steps to build this container:
    - Mount a volume binding directory `data/` to a container directory `data/`
    - Copy local directory `src/data_science/` to container directory `src/`
    - Install the requirements `pip install -r src/requirements.txt`
    - Run the python script `src/node.py` (containing the adapted split_data function from `iris/src/iris/pipelines/data_science/nodes.py`). **For the purpose of this exercise it's enough to adapt only the `train_model` function**. The script should receive 4 command line arguments: input_folder, output_file, num_train_iter, and learning_rate.
      - *input_folder* [string]: path to the folder where the outputs from previous container were stored (should be `data/02_intermediate/`)
      - *output_file* [string]: path to the file to save the output from the script. (should be `data/03_final/models.csv`) **Note that the output must be converted to a csv file**.
      - *num_train_iter* [integer]: number of training iterations parameter (e.g. 10000).
      - *learning_rate* [float]: model learning rate parameter (should be a value value between 0 an 1 with up to 3 decimal places, e.g. 0.01).
       - Example of command: `python src/node.py --input_folder data/02_intermediate --output_file data/03_final/models.csv --num_train_iter 10000 --learning_rate 0.01`


