# Test Assignment

End-to-end ML pipeline for RTB task. Fedor Erin, Oct 2023.

## Setup
1) Put the raw data `training_data.csv.gz` and `test_data.csv.gz` into `data/raw` project local folder:

<p align="center"><img src="imgs/data_layout.png" width="200"></p>

2) Run the master script to consequently initialize Airflow, build Docker image and start all components as containers:

```bash
sh run.sh
```

3) Visit `http://localhost:8080/` and log in using the credentials: `user=airflow` and `password=airflow`. 
There are two DAGs, for train and predict:

<p align="center"><img src="imgs/dags.png" width="400"></p>

4) Run the training DAG first:

<p align="center"><img src="imgs/train_dag.png" width="500"></p>

- As a result, it creates in the project the following files:
  - `data/processed/train_df.csv` - processed dataset for train
  - `models/pipeline_*.pkl` - trained model/pipeline
  - `reports/report_*.yaml` - cross-validation metrics and model parameters
   

5) Next, run the predicting DAG:

<p align="center"><img src="imgs/predict_dag.png" width="500"></p>

- As a result, it creates the following files:
  - `data/processed/test_df.csv` - processed dataset for test
  - `data/predictions/predictions_*.npy` - probability predictions for test data

6) Check out the tasks (containers) logs, if needed, as well as intermediate and resulting files.

## Project Structure

    ├── airflow               <- Airflow folder
    │   ├──dags               <- DAGs folder
    │   |   ├── pipeline      <- Job Dockerfile and pipelines DAG files
    │   |   |   └── Dockerfile 
    │   |   |   └── predict_pipeline.py
    │   |   |   └── train_pipeline.py
    │   ├──config            
    │   ├──logs               <- Airflow auxiliary directories
    │   └──plugins   
    │
    ├── data
    │   ├── predictions       <- Saved model predictions as NumPy arrays
    │   ├── processed         <- The final, canonical data sets for modeling
    │   └── raw               <- The original, immutable data dump
    │
    ├── imgs                  <- Images for README
    │    
    ├── models                <- Trained and serialized models (sklearn pipelines)
    │
    ├── notebooks             <- Jupyter notebooks with exploration
    │   └── eda.ipynb         <- Exploratory Data Analysis│
    │
    ├── reports               <- YAML reports with models parameters and validation metrics
    │
    ├── src                   <- Source code for use in this project
    │   ├── __init__.py       <- Makes src a Python module
    │   ├── config.py         <- Config file with namings/parameters
    │   │
    │   ├── data              <- Scripts to generate datasets
    │   │   └── make_dataset.py
    │   │   └── preprocessing.py
    │   │
    │   ├── models            <- Scripts to train models and make predictions
    │   │   ├── make_predicting.py
    │   │   ├── make_training.py
    │   │   ├── pipeline.py
    │   │   └── utils.py
    │   │
    ├── LICENSE
    ├── .env                  <- Environment variables
    ├── .gitignore
    ├── README.md
    ├── run.sh                <- Master script to run the project
    ├── .flake8               <- Style checker config
    ├── requirements.txt      <- Packages required for pipeline
    └── docker-compose.yaml   <- Airflow services for pipeline


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
