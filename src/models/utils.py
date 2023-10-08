from os import path
import numpy as np
import yaml
import joblib

from sklearn.pipeline import Pipeline

def save_model(pipeline: Pipeline, version: str) -> None:
    """
    Save model/pipeline into pickle file
    """
    model_path = path.join('models/', f'pipeline_{version}.pkl')
    joblib.dump(pipeline, model_path)

def save_report(pipeline: Pipeline, metrics: dict, version: str) -> None:
    """
    Save model parameters and cross-validation metrics into YAML file
    """
    report_path = path.join('reports/', f'report_{version}.yaml')
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
    preds_path = path.join('data/predictions/', f'predictions_{version}.npy')
    with open(preds_path, 'wb') as f:
        np.save(f, predictions)
