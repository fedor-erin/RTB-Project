from datetime import datetime
from typing import Tuple
import pandas as pd
from logging import Logger

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

from utils import save_model, save_report
from src.config import CATEGORICAL_FEATURES, NUMERICAL_FEATURES, TARGET, RANDOM_SEED


def build_pipeline() -> Pipeline:
    """
    Build a basic pipeline of a scaler, one-hot encoder and a classifier model
    """
    num_transformer = StandardScaler()
    cat_transformer = OneHotEncoder(handle_unknown='ignore')
    preprocessor = ColumnTransformer(transformers=[('scaler', num_transformer, NUMERICAL_FEATURES),
                                                   ('ohe', cat_transformer, CATEGORICAL_FEATURES)])
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', LogisticRegression(random_state=RANDOM_SEED))])
    return pipeline


def cross_validation_scores(pipeline: Pipeline,
                            X: pd.DataFrame,
                            y: pd.Series,
                            cv: int) -> dict:
    """
    Get cross validation scores for 3 metrics: ROC AUC, Brier score, Log Loss
    """
    params = {'estimator': pipeline,
              'X': X,
              'y': y,
              'cv': cv}

    roc_auc = cross_val_score(**params, scoring='roc_auc')
    roc_auc_cv = f"{roc_auc.mean():.3f} (+-{roc_auc.std():.3f})"

    brier = -cross_val_score(**params, scoring='neg_brier_score')
    brier_cv = f"{brier.mean():.3f} (+-{brier.std():.3f})"

    log_loss = -cross_val_score(**params, scoring='neg_log_loss')
    log_loss_cv = f"{log_loss.mean():.3f} (+-{log_loss.std():.3f})"

    return {
        'roc_auc': roc_auc_cv,
        'brier': brier_cv,
        'log_loss': log_loss_cv,
    }


def train_pipeline(train_df: pd.DataFrame,
                   logger: Logger) -> Tuple[Pipeline, dict]:
    """
    Train a model pipeline, report metrics, save it
    """
    X, y = train_df[CATEGORICAL_FEATURES + NUMERICAL_FEATURES], train_df[TARGET]
    logger.info(f'Dataset with a shape {X.shape} is ready')

    logger.info('Defining pipeline...')
    pipeline = build_pipeline()

    logger.info('Training pipeline...')
    pipeline.fit(X, y)

    logger.info('Cross validation...')
    metrics = cross_validation_scores(pipeline, X, y, cv=3)

    logger.info('Saving model...')
    version = datetime.now().strftime('%Y%m%d')
    save_model(pipeline, version, logger)

    logger.info('Saving validation and model parameters report...')
    save_report(pipeline, metrics, version, logger)

    return pipeline, metrics
