from pycaret.classification import *
from generate_features import df

# initializes the training environment and creates the transformation pipeline
clf = setup(data = df, target = 'Class', train_size = 0.7, silent=True, session_id = 123)

# as we have seen on the jupyter notebook the best model is the Light Gradient Boosting Machine
lgb1 = create_model("lightgbm")
tuned_lgb_random = tune_model(lgb1)
save_model(tuned_lgb_random, '../models/lgbm')
