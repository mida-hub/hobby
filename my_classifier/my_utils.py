import numpy as np
import pandas as pd
import yaml
from sklearn.preprocessing import Imputer
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from datetime import datetime
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score # 正解率
from sklearn.metrics import precision_score # 適合率
from sklearn.metrics import recall_score # 再現率
from sklearn.metrics import f1_score # F値
from sklearn.metrics import roc_auc_score # auc
from operator import itemgetter

class MyUtils:
    def __init__(self, filepath_yml, obj_type, metrics):
        self.filepath_yml = filepath_yml
        self.obj_type = obj_type
        self.metrics  = metrics

        self.IMPUTER_PATH = './model/imputer.pkl'
        self.COLUMNS_PATH = './model/columns.pkl'
        self.SELECTOR_PATH = './model/selector.pkl'

    def get_str_timestamp(self):
        return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    def read_data(self, csvpath):
        df = pd.read_csv(csvpath, header=0, dtype=self.obj_type)

        X = df.iloc[:, 2:]  # 2列目以降が特徴量
        ID = df.iloc[:, [0]]  # 第0列はPK（Loan_ID）なのでIDとしてセット
        y = df.iloc[:, [1]]  # 1列目が正解データ

        # 最初から0/1バイナリの場合はコメントアウト
        # class_mapping = {'N': 1, 'Y': 0}
        # y.loc[:, y_label] = y[y_label].map(class_mapping)

        return ID, X, y.as_matrix().ravel()

    def train_data__preprocessing_with_imputer(self, X, ohe_columns):

        # one-hotエンコーディング
        # カテゴリ変数に適用する
        X = pd.get_dummies(X
                           ,dummy_na=True
                           ,columns=ohe_columns
                           )

        # 数値型の欠損値を平均値で補完するための計算
        imp = Imputer(missing_values='NaN'
                      ,strategy='mean'
                      ,axis=0
                      )
        imp.fit(X)

        # NaN値を平均値に補完
        X_columns = X.columns.values
        X = pd.DataFrame(imp.transform(X),
                             columns=X_columns)

        # カラム、imputerの保存
        joblib.dump(X_columns, self.COLUMNS_PATH)
        joblib.dump(imp, self.IMPUTER_PATH)

        return X

    def get_train_test_split(self, X, y, test_size, random_state=1):
        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    def get_p_select_n(self, X, y, clf, param_key):
        select_n = range(1, X.shape[1] + 1)
        param_grid = {param_key: select_n}

        gs = GridSearchCV(estimator=clf,
                          param_grid=param_grid,
                          scoring=self.metrics,
                          cv=3,
                          return_train_score=False
                          )

        gs = gs.fit(X, y)

        # 探索した結果のベストスコアとパラメータの取得
        print('Best Score:', gs.best_score_)
        print('Best Params:', gs.best_params_)
        return gs.best_params_[param_key]

    def select_n__gridsearch_with_rfe(self, X, y):
        clf = Pipeline([('scl', self.get_standard_scaler()),
                        ('rfe', self.get_rfe(self.get_est_randomforest_classifier())),
                        ('est', self.get_est_logistic_regression())])

        return self.get_p_select_n(X, y, clf, 'rfe__n_features_to_select')

    def select_n__gridsearch_with_pca(self, X, y):
        clf = Pipeline([('scl', self.get_standard_scaler()),
                        ('pca', self.get_pca()),
                        ('est', self.get_est_logistic_regression())])

        return self.get_p_select_n(X, y, clf, 'pca__n_components')

    def train_data__preprocessing_with_rfe(self, X, y, select_n):
        selector = self.get_rfe(self.get_est_randomforest_classifier(),
                               n_features_to_select=select_n
                               )
        selector.fit(X, y)

        # selectorの保存
        joblib.dump(selector, self.SELECTOR_PATH)

        return X.loc[:, X.columns.values[selector.support_]]

    def train_data__preprocessing_with_pca(self, X, y, select_n):
        selector = self.get_pca(n_components=select_n)
        selector.fit(X, y)
        return pd.DataFrame(selector.transform(X)), selector

    def get_standard_scaler(self):
        return StandardScaler()

    def get_pca(self, n_components=None, random_state=1):
        return PCA(n_components=n_components,
                   random_state=random_state
                   )

    def get_rfe(self, est, n_features_to_select=None, step=.05):
        return RFE(est,
                   n_features_to_select=n_features_to_select,
                   step=step
                   )

    def get_est_logistic_regression(self, random_state=1, C=1.0, penalty='l2'):
        return LogisticRegression(random_state=random_state,
                                  C=C,
                                  penalty=penalty)

    def get_est_randomforest_classifier(self, random_state=1, n_estimators=10, max_depth=None, max_features='auto'):
        return RandomForestClassifier(random_state=random_state,
                                      n_estimators=n_estimators,
                                      max_depth=max_depth,
                                      max_features=max_features)

    def get_est_gradientboosting_classifier(self, random_state=1, n_estimators=100, learning_rate=0.1, max_depth=3, max_features=None):
        return GradientBoostingClassifier(random_state=random_state,
                                          n_estimators=n_estimators,
                                          learning_rate=learning_rate,
                                          max_depth=max_depth,
                                          max_features=max_features)

    def get_est_decisiontree_classifier(self, random_state=1, criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1):
        return DecisionTreeClassifier(random_state=random_state,
                                      criterion=criterion,
                                      max_depth=max_depth,
                                      min_samples_split=min_samples_split,
                                      min_samples_leaf=min_samples_leaf)

    def get_pipeline(self, clf, param=None):

        if clf == 'Logistic':
            C = 1.0
            penalty = 'l2'
            if param:
                penalty = param['penalty']
                C = param['C']

            est = self.get_est_logistic_regression(C=C,
                                                   penalty=penalty)

        if clf == 'R-forest':
            n_estimators = 10
            max_depth = None
            max_features = 'auto'
            if param:
                n_estimators = param['n_estimators']
                max_depth = param['max_depth']
                max_features = param['max_features']
            est = self.get_est_randomforest_classifier(n_estimators=n_estimators,
                                                       max_depth=max_depth,
                                                       max_features=max_features)

        if clf == 'G-boost':
            n_estimators = 100
            learning_rate = 0.1
            max_depth = 3
            max_features = None
            if param:
                n_estimators = param['n_estimators']
                max_depth = param['max_depth']
                max_features = param['max_features']
                learning_rate = param['learning_rate']
            est = self.get_est_gradientboosting_classifier(n_estimators=n_estimators,
                                                           learning_rate=learning_rate,
                                                           max_depth=max_depth,
                                                           max_features=max_features)

        if clf == 'D-tree':
            criterion = 'gini'
            max_depth = None
            min_samples_split = 2
            min_samples_leaf = 1
            if param:
                criterion = param['criterion']
                max_depth = param['max_depth']
                min_samples_split = param['min_samples_split']
                min_samples_leaf = param['min_samples_leaf']

            est = self.get_est_decisiontree_classifier(criterion=criterion,
                                                       max_depth=max_depth,
                                                       min_samples_split=min_samples_split,
                                                       min_samples_leaf=min_samples_leaf)

        return Pipeline([('scl', self.get_standard_scaler()),
                         ('est', est)])

    def clf__grid_search(self, X, y):

        f = open(self.filepath_yml)
        yml = yaml.load(f)
        f.close()

        clf_list = {}
        param_list = {}

        for clf in yml['clf_list']:
            param_list[clf] = yml['clf_list'][clf][0]
            clf_list[clf] = self.get_pipeline(clf)

        for est_name in clf_list:
            clf = clf_list[est_name]
            param_grid = param_list[est_name]

            gs = GridSearchCV(estimator=clf,
                              param_grid=param_grid,
                              scoring=self.metrics,
                              cv=3,
                              return_train_score=False
                              )

            gs = gs.fit(X, y)

            # 探索した結果のベストスコアとパラメータの取得
            print(est_name)
            print('Best Score:', gs.best_score_)
            print('Best Params:', gs.best_params_)
            print(self.get_str_timestamp())
        return

    def model_validation(self, X, y):
        est_result = []
        model_name= ''

        X_train, X_test, y_train, y_test = self.get_train_test_split(X, y, test_size=0.2)

        f = open(self.filepath_yml)
        yml = yaml.load(f)
        f.close()

        clf_list = {}
        for clf in yml['clf_val']:
            param = yml['clf_val'][clf][0]
            clf_list[clf] = self.get_pipeline(clf, param)

        train_score = 0.0
        test_score = 0.0

        print('metrics: ' + self.metrics)
        for pipe_name, pipeline in clf_list.items():
            pipeline.fit(X_train, y_train)

            if self.metrics == 'accuracy':
                train_score = accuracy_score(y_train, pipeline.predict(X_train))
                test_score = accuracy_score(y_test, pipeline.predict(X_test))
            elif self.metrics == 'precision':
                train_score = precision_score(y_train, pipeline.predict(X_train))
                test_score = precision_score(y_test, pipeline.predict(X_test))
            elif self.metrics == 'recall':
                train_score = recall_score(y_train, pipeline.predict(X_train))
                test_score = recall_score(y_test, pipeline.predict(X_test))
            elif self.metrics == 'f1':
                train_score = f1_score(y_train, pipeline.predict(X_train))
                test_score = f1_score(y_test, pipeline.predict(X_test))
            elif self.metrics == 'auc':
                train_score = roc_auc_score(y_train, pipeline.predict(X_train))
                test_score = roc_auc_score(y_test, pipeline.predict(X_test))

            print('%s-train: %.6f' % (pipe_name, train_score))
            print('%s-test : %.6f' % (pipe_name, test_score))
            est_result.append([pipe_name, test_score])

        # テストデータの指標の降順でセット
        est_result_sorted = sorted(est_result, key=itemgetter(1), reverse=True)

        print('--ranking')
        for est_name, score in est_result_sorted:
            if best_est_name == '':
                best_est_name = est_name
            print('%s-test: %.6f' % (est_name, score))

        clf = clf_list[best_est_name]

        # モデルを保存する
        joblib.dump(clf, './model/'+ best_est_name + '.pkl')

        return clf, best_est_name

    def score_data__preprocessing(self, X, ohe_columns, selector_method):

        # カラム, 数値処理, 次元削減
        X_columns = joblib.load(self.COLUMNS_PATH)
        imp = joblib.load(self.IMPUTER_PATH)
        selector = joblib.load(self.SELECTOR_PATH)

        # one-hotエンコーディング
        # カテゴリ変数に適用する
        X_score = pd.get_dummies(X,
                                 dummy_na=True,
                                 columns=ohe_columns)

        cols_model = set(X_columns)
        cols_score = set(X_score.columns.values)

        # モデルにはあったがスコアにはないデータ項目
        diff_m = cols_model - cols_score
        # print('モデルのみに存在する項目: %s' % diff_m)

        # スコアにはあるがモデルになかったデータ項目
        diff_s = cols_score - cols_model
        # print('スコアのみに存在する項目: %s' % diff_s)

        # 空データでモデルデータのカラム
        df_cols_m = pd.DataFrame(None,
                                 columns=X_columns,
                                 dtype=float)

        X_score = pd.concat([df_cols_m, X_score])

        # スコアデータのみに登場するデータを削除
        X_score = X_score.drop(list(diff_s), axis=1)

        # モデルデータのみに登場するデータを0埋め
        X_score.loc[:, list(diff_m)] = X_score.loc[:, list(diff_m)].fillna(0, axis=1)

        # モデリング時点のone-hotエンコーディング後の並び順にする
        X_score = X_score.reindex(X_columns, axis=1)

        # 数値型カラムの補完
        X_score = pd.DataFrame(imp.transform(X_score),
                               columns=X_columns)

        if selector_method == 'RFE':
            X_score = X_score.loc[:, X_columns[selector.support_]]
        elif selector_method == 'PCA':
            X_score = pd.DataFrame(selector.transform(X_score))

        return X_score

    def predict_to_csv(self, ID_score, X_score, est_name):
        print('load model : ./model/'+ est_name + '.pkl')
        clf = joblib.load('./model/'+ est_name + '.pkl')

        score = pd.DataFrame(clf.predict_proba(X_score)[:, 1], columns=['pred_score'])
        print('pred_score_to_csv')
        ID_score.join(score).to_csv('./data/score_pred_by_' + est_name + '.csv', index=False)

        return