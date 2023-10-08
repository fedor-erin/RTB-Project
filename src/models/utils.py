import glob
import os
import numpy as np
import yaml
import pickle

from sklearn.pipeline import Pipeline


def save_model(pipeline: Pipeline, version: str) -> None:
    """
    Save model/pipeline into pickle file
    """
    model_path = os.path.join('models/', f'pipeline_{version}.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(pipeline, f)


def load_model() -> Pipeline:
    """
    Load the latest version of the model
    """
    list_of_models = glob.glob('models/*')
    latest_model = max(list_of_models, key=os.path.getmtime)
    with open(latest_model, 'rb') as f:
        model = pickle.load(f)
    return model


def save_report(pipeline: Pipeline, metrics: dict, version: str) -> None:
    """
    Save model parameters and cross-validation metrics into YAML file
    """
    report_path = os.path.join('reports/', f'report_{version}.yaml')
    report = {
        'model_params': {k: v for k, v in pipeline.get_params().items() if k.startswith('classifier_')},
        'metrics_cross_val': metrics,
    }
    with open(report_path, 'w') as f:
        yaml.dump(report, f, allow_unicode=True, default_flow_style=False)


def save_predictions(predictions: np.array, version: str) -> None:
    """
    Save model predictions for test data
    """
    preds_path = os.path.join('data/predictions/', f'predictions_{version}.npy')
    with open(preds_path, 'wb') as f:
        np.save(f, predictions)
