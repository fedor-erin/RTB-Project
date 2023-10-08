Test Assignment
==============================

End-to-end ML pipeline for RTB task.

Project Structure
------------

    ├── data
    │   ├── predictions    <- Saved model predictions as NumPy arrays
    │   ├── processed      <- The final, canonical data sets for modeling
    │   └── raw            <- The original, immutable data dump
    │
    ├── models             <- Trained and serialized models (sklearn pipelines)
    │
    ├── notebooks          <- Jupyter notebooks with exploration
    │   ├── eda.ipynb       - Exploratory Data Analysis
    │   ├── modelling.ipynb - Sandbox for testing pipeline and analysing predictions
    │
    ├── reports            <- Models parameters and validation metrics for pipeline runs
    │
    ├── src                <- Source code for use in this project
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── config.py      <- Config file with namings/parameters
    │   │
    │   ├── data           <- Scripts to generate datasets
    │   │   └── make_dataset.py
    │   │   └── preprocessing.py
    │   │
    │   ├── models         <- Scripts to train models and make predictions
    │   │   ├── make_predicting.py
    │   │   ├── make_training.py
    │   │   ├── pipeline.py
    │   │   └── utils.py
    │   │
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make dataset` or `make training`
    ├── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io 
    ├── .gitignore    
    ├── README.md
    └── requirements.txt

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
