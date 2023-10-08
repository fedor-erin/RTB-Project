# columns names
CATEGORICAL_FEATURES = [
    'campaignId',
    'platform',
    'softwareVersion',
    'sourceGameId',
    'country',
    'connectionType',
    'deviceType',
]
NUMERICAL_FEATURES = [
    'startCount',
    'viewCount',
    'clickCount',
    'installCount',
    'startCount1d',
    'startCount7d',
    'fromLastStart',  # new feature
]
TARGET = 'install'

# hyperparameters
RANDOM_SEED = 100
