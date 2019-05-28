from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import lightgbm as lgb


def offline_cv(df, cat_cols='auto'):
    X, Y = df.drop(['uId', 'age'], axis=1), df.loc[:, 'age']
    X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.1, stratify=Y)

    lgb_train = lgb.Dataset(X_train, Y_train, categorical_feature=cat_cols)
    lgb_val = lgb.Dataset(X_val, Y_val, categorical_feature=cat_cols, reference=lgb_train)

    params = {
        'objective': 'multiclass',
        'num_class': 6,
        'metric': ['multi_logloss', 'multi_error'],
        'num_threads': 12,
    }

    gbm = lgb.train(params, lgb_train, valid_sets=lgb_val, early_stopping_rounds=10, verbose_eval=10)

    f_imp_df = pd.DataFrame({
        'feature': X_train.columns,
        'importance': gbm.feature_importance(),
    }).sort_values(by='importance', ascending=False)

    print(f_imp_df[:20])
