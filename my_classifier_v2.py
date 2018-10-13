import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from operator import itemgetter
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score # 正解率
from sklearn.metrics import precision_score # 適合率
from sklearn.metrics import recall_score # 再現率
from sklearn.metrics import f1_score # F値
from sklearn.metrics import roc_auc_score # auc
from sklearn.externals import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

# 訓練データ読み込み
def read_train(csvpath, y_label, type):

    df = pd.read_csv(csvpath, header=0, dtype=type)

    X  = df.iloc[:, 2:]            # 2列目以降が特徴量
    ID = df.iloc[:, [0]]           # 第0列はPK（Loan_ID）なのでIDとしてセット
    y  = df.iloc[:, [1]]           # 1列目が正解データ

    # 最初から0/1バイナリの場合はコメントアウト
    class_mapping = {'N': 1, 'Y': 0}
    y_new = y.copy()
    y_new.loc[:, y_label] = y_new[y_label].map(class_mapping)

    # print('-'*50)
    # print(X.head())
    # print(y.head())
    # print(df.describe())
    # df.hist(bins=50, figsize=(10, 10))
    # print(df.corr())
    # 属性間の相関を見るときに指定する
    # attributes = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
    # scatter_matrix(df[attributes], figsize=(10, 10))
    # plt.show()
    # print(y_new.head())
    # print(y_new[y_label].value_counts())
    # print('-'*50)

    return X, y_new

#####################################################
# スコアデータ読み込み
def read_score(csvpath, type):

    df = pd.read_csv(csvpath, header=0, dtype=type)
    # print(df.head())

    # ID = df.iloc[:, [0]]              # 第0列はPKなのでIDとしてセット
    # X = df.drop(ID_label, axis=1)     # IDは特徴ベクトルから削除

    X  = df.iloc[:, 2:]            # 2列目以降が特徴量
    ID = df.iloc[:, [0]]           # 第0列はPK（Loan_ID）なのでIDとしてセット
    y  = df.iloc[:, [1]]           # 1列目が正解データ

    # print(X.head())
    # print('-'*50)

    return X, ID

#####################################################
# 訓練データ前処理
def preprocessing_train(X, y_new, ohe_columns, columns_path, rfepca, imputer_path, selector_path, select_n):

    # one-hotエンコーディング
    # カテゴリ変数に適用する
    X_new = pd.get_dummies(X,
                           dummy_na=True,
                           columns=ohe_columns)

    # print(X_new.head())
    # print(X_new.shape)
    # print(X_new.describe())
    # print('-' * 50)

    # 数値型の欠損値を平均値で補完するための計算
    imp = Imputer(missing_values='NaN',
                  strategy='mean',
                  axis=0
                  )
    imp.fit(X_new)

    # NaN値を平均値に補完
    X_new_columns = X_new.columns.values
    X_new = pd.DataFrame(imp.transform(X_new),
                         columns=X_new_columns)

    # print(X_new.head())
    # print('-' * 50)

    # print(rfepca)
    if rfepca == 'RFE':
        selector = RFE(RandomForestClassifier(random_state=1),
                       n_features_to_select=select_n,
                       step=.05)
        selector.fit(X_new, y_new.as_matrix().ravel())
        X_fin = X_new.loc[:, X_new_columns[selector.support_]]
    elif rfepca == 'PCA':
        selector = PCA(n_components=select_n, random_state=1)
        selector.fit(X_new, y_new.as_matrix().ravel())
        X_fin = pd.DataFrame(selector.transform(X_new))

    # 前処理モデルを保存する
    joblib.dump(X_new_columns, columns_path)
    joblib.dump(imp, imputer_path)
    joblib.dump(selector, selector_path)

    # print('X_fin shape:(%i,%i)' % X_fin.shape)
    # print(X_fin.head())

    # print("主成分の分散説明率")
    # print(pca.explained_variance_ratio_)
    # print("固有ベクトル")
    # print(pca.components_)

    return X_fin, y_new.as_matrix().ravel()

#####################################################
# スコアデータ前処理
def preprocessing_score(X, ohe_columns, columns_path, rfepca, imputer_path, selector_path):

    # モデルを復元
    # カラム, 数値処理, 次元削減
    X_columns = joblib.load(columns_path)
    imp = joblib.load(imputer_path)
    selector = joblib.load(selector_path)

    # one-hotエンコーディング
    # カテゴリ変数に適用する
    X_s = pd.get_dummies(X,
                           dummy_na=True,
                           columns=ohe_columns)

    cols_model = set(X_columns)
    cols_score = set(X_s.columns.values)

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
    X_s = pd.concat([df_cols_m, X_s])
    # print(X_s.head())
    # print('-' * 50)

    # スコアデータのみに登場するデータを削除
    X_s = X_s.drop(list(diff_s), axis=1)
    # print(X_s.head())
    # print('-' * 50)

    # モデルデータのみに登場するデータを0埋め
    X_s.loc[:, list(diff_m)] = X_s.loc[:, list(diff_m)].fillna(0, axis=1)
    # print(X_s.head())
    # print('-' * 50)

    # モデリング時点のone-hotエンコーディング後の並び順にする
    X_s = X_s.reindex(X_columns, axis=1)

    # 数値型カラムの補完
    X_s = pd.DataFrame(imp.transform(X_s),
                        columns=X_columns)

    # print(X_s.head())
    # print('-' * 50)

    # print(rfepca)
    if rfepca == 'RFE':
        X_fin_s = X_s.loc[:, X_columns[selector.support_]]
    elif rfepca == 'PCA':
        X_fin_s = pd.DataFrame(selector.transform(X_s))

    # print(X_fin_s.head())
    # print('-' * 50)

    return X_fin_s

#####################################################
# グリッドサーチSelect_n
def gridSearchFunction_Select_n(X, y, ohe_columns, metrics):
    y = y.as_matrix().ravel()

    # one-hotエンコーディング
    # カテゴリ変数に適用する
    X_new = pd.get_dummies(X,
                           dummy_na=True,
                           columns=ohe_columns)

    # print(X_new.head())
    # print(X_new.shape)
    # print(X_new.describe())
    # print('-' * 50)

    # 数値型の欠損値を平均値で補完するための計算
    imp = Imputer(missing_values='NaN',
                  strategy='mean',
                  axis=0
                  )
    imp.fit(X_new)

    # NaN値を平均値に補完
    X_new_columns = X_new.columns.values
    X = pd.DataFrame(imp.transform(X_new),
                         columns=X_new_columns)

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=1)


    clf_list = {
        # ロジスティック
        'Logistic_rfe':
            Pipeline([('scl', StandardScaler()),
                      ('rfe', RFE(RandomForestClassifier(random_state=1),step=.05)),
                      ('est', LogisticRegression(random_state=1))]),
        # ロジスティック
        'Logistic_pca':
            Pipeline([('scl', StandardScaler()),
                      ('pca', PCA(random_state=1)),
                      ('est', LogisticRegression(random_state=1))])
    }

    select_n = range(1, X_new.shape[1] + 1)

    param_list = {
        # ロジスティック
        'Logistic_rfe':{'rfe__n_features_to_select':select_n},
        # ロジスティック
        'Logistic_pca':{'pca__n_components':select_n}
    }

    for est_name in clf_list:
        clf = clf_list[est_name]
        param_grid = param_list[est_name]

        gs = GridSearchCV(estimator=clf,
                           param_grid=param_grid,
                           scoring=metrics,
                           cv=3,
                           return_train_score=False
                            )

        gs = gs.fit(X_train, y_train)

        # 探索した結果のベストスコアとパラメータの取得
        print(est_name)
        print('Best Score:', gs.best_score_)
        print('Best Params', gs.best_params_)
        # print(pd.DataFrame(gs.cv_results_))

    return

#####################################################
# グリッドサーチ
def gridSearchFunction(X, y, metrics):

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=1)


    clf_list = {
        # # K近傍法
        # 'Knn':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', KNeighborsClassifier())]),
        # ロジスティック
        'Logistic':
            Pipeline([('scl', StandardScaler()),
                      ('est', LogisticRegression(random_state=1))]),
        # # SVC
        # 'svc':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', SVC(random_state=1))]),
        # # L-SVC
        # 'L-svc':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', LinearSVC(random_state=1))]),
        # ランダムフォレスト
        'R-forest':
            Pipeline([('scl', StandardScaler()),
                      ('est', RandomForestClassifier(random_state=1))]),
        # # ブースティング
        'G-boost':
            Pipeline([('scl', StandardScaler()),
                      ('est', GradientBoostingClassifier(random_state=1))]),
        # 決定木
        'D-tree':
            Pipeline([('scl', StandardScaler()),
                      ('est', DecisionTreeClassifier(random_state=1))]),
        # # パーセプトロン
        # 'Mlp':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', MLPClassifier(random_state=1))]),
        # XGB
        'xgb':
            Pipeline([('scl', StandardScaler()),
                      ('est', XGBClassifier(random_state=1))])
    }


    param_list = {
        # # K近傍法
        # 'Knn':{'est__n_neighbors': range(10, 101, 10),
        #         'est__weights': ["uniform", "distance"]},
        # ロジスティック
        'Logistic':{'est__penalty': ["l1", "l2"],
                  'est__C': [0.1, 1, 10]},
        # # SVC
        # 'svc':{'est__degree': [1, 2, 3, 5, 7],
        #         'est__C': [0.1, 1, 10]},
        # # L-SVC
        # 'L-svc':{'est__loss': ["hinge", "squared_hinge"],
        #          'est__C': [0.1, 1, 10]},
        # ランダムフォレスト
        'R-forest':{'est__n_estimators': [10, 20, 30],
                    'est__max_depth': [3, 5, 7],
                    'est__max_features': np.arange(0.1, 0.5, 0.2),},
        # ブースティング
        'G-boost':{'est__n_estimators': [10, 20, 30],
                    'est__learning_rate': [0.1, 0.5, 1.],
                    'est__max_depth': [3, 5, 7],
                    'est__max_features': np.arange(0.1, 0.5, 0.2)},
        # 決定木
        'D-tree':{'est__criterion': ["gini", "entropy"],
                    'est__max_depth': [3, 5, 7],
                    'est__min_samples_split': [2, 4, 6],
                    'est__min_samples_leaf': [2, 4, 6]
        },
        # # パーセプトロン
        # 'Mlp':{'est__hidden_layer_sizes': [(10, 5), (5, 2), (16, 4, 2)],
        #         'est__max_iter': [1000]
        # },
        # XGB
        'xgb':{'est__max_depth': [2, 4, 6],
               'est__min_child_weight': [1, 2, 3],
               'est__gamma': [0, 3, 10],
               'est__n_estimators': [10, 50, 100]
        }
    }

    for est_name in clf_list:
        clf = clf_list[est_name]
        param_grid = param_list[est_name]

        gs = GridSearchCV(estimator=clf,
                                   param_grid=param_grid,
                                   scoring=metrics,
                                   cv=3,
                                   return_train_score=False
                                   )

        gs = gs.fit(X_train, y_train)

        # 探索した結果のベストスコアとパラメータの取得
        print(est_name)
        print('Best Score:', gs.best_score_)
        print('Best Params', gs.best_params_)

    return

#####################################################
# 推定器
def modelValidation(X, y, metrics, est_choice=""):
    est_result = []
    est_result_sorted = []

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=1)

    # print('X_test shape:(%i,%i)' % X_test.shape)
    # print(len(y_test))

    clf_list = {
        # K近傍法
        # 'Knn':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', KNeighborsClassifier(n_neighbors=10))]),
        # ロジスティック
        'Logistic':
            Pipeline([('scl', StandardScaler()),
                      ('est', LogisticRegression(random_state=1, C=0.1, penalty='l1'))]),
        # # SVC
        # 'svc':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', SVC(random_state=1, C=1, degree=1))]),
        # # L-SVC
        # 'L-svc':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', LinearSVC(C=1.0, class_weight='balanced', random_state=1))]),
        # ランダムフォレスト
        'R-forest':
            Pipeline([('scl', StandardScaler()),
                      ('est', RandomForestClassifier(random_state=1, max_depth=5, max_features=0.3, n_estimators=30))]),
        # ブースティング
        'G-boost':
            Pipeline([('scl', StandardScaler()),
                      ('est', GradientBoostingClassifier(random_state=1, learning_rate=0.1, max_depth=3, max_features=0.3, n_estimators=20))]),
        # 決定木
        'D-tree':
            Pipeline([('scl', StandardScaler()),
                      ('est', DecisionTreeClassifier(random_state=1, max_depth=3, min_samples_leaf=4, min_samples_split=2, criterion='entropy'))]),
        # # パーセプトロン
        # 'Mlp':
        #     Pipeline([('scl', StandardScaler()),
        #               ('est', MLPClassifier(hidden_layer_sizes=(5, 2),
        #                                     max_iter=1000,
        #                                     random_state=1))]),
        # XGB
        'xgb':
            Pipeline([('scl', StandardScaler()),
                      ('est', XGBClassifier(random_state=1, gamma=3, max_depth=2, min_child_weight=1, n_estimators=100))])
    }

    train_score = 0.0
    test_score = 0.0

    print('metrics: ' + metrics)
    for pipe_name, pipeline in clf_list.items():
        pipeline.fit(X_train, y_train)

        if metrics == 'accuracy':
            train_score = accuracy_score(y_train, pipeline.predict(X_train))
            test_score = accuracy_score(y_test, pipeline.predict(X_test))
        elif metrics == 'precision':
            train_score = precision_score(y_train, pipeline.predict(X_train))
            test_score = precision_score(y_test, pipeline.predict(X_test))
        elif metrics == 'recall':
            train_score = recall_score(y_train, pipeline.predict(X_train))
            test_score = recall_score(y_test, pipeline.predict(X_test))
        elif metrics == 'f1':
            train_score = f1_score(y_train, pipeline.predict(X_train))
            test_score = f1_score(y_test, pipeline.predict(X_test))
        elif metrics == 'auc':
            train_score = roc_auc_score(y_train, pipeline.predict(X_train))
            test_score = roc_auc_score(y_test, pipeline.predict(X_test))

        print('%s-train: %.6f' % (pipe_name, train_score))
        print('%s-test : %.6f' % (pipe_name, test_score))
        est_result.append([pipe_name, test_score])

    # テストデータの指標の降順でセット
    est_result_sorted = sorted(est_result, key=itemgetter(1), reverse=True)

    print('--ranking')
    for est, met in est_result_sorted:
        if est_choice == "":
            est_choice = est
        print('%s-test: %.6f' % (est, met))

    clf = clf_list[est_choice]

    # モデルを保存する
    joblib.dump(clf, './model/'+ est_choice + '.pkl')

    return clf, est_choice

#####################################################
# スコアリング
def scoring(X_s, ID_s, best_model, best_name=""):
    # モデルを復元
    if best_name != "" :
        print('load model : ./model/'+ best_name + '.pkl')
        best_model = joblib.load('./model/'+ best_name + '.pkl')
    elif (best_model is None) and (best_name == ""):
        print('Please input best_name because best_model is None!')
        return

    score = pd.DataFrame(best_model.predict_proba(X_s)[:, 1], columns=['pred_score'])
    print('pred_score_to_csv')
    ID_s.join(score).to_csv('./data/my_classifier_with_pred_' + best_name + '.csv', index=False)

    return

#####################################################
# train
train_path = './data/final_hr_analysis_train.csv'
# score
score_path = './data/final_hr_analysis_test.csv'
# X columns
columns_path = './model/my_columns.pkl'
# Imputer
imputer_path = './model/my_imputer.pkl'
# RFE/PCA
selector_path = './model/my_selector.pkl'

# 評価指標を選択
# metrics
# accuracy, precision, recall, f1, auc
metrics = 'accuracy'
# metrics = 'precision'
# metrics = 'recall'
# metrics = 'f1'
# metrics = 'auc'

# RFE/PCA
rfepca = 'RFE'
# rfepca = 'PCA'

# 次元数
select_n = 6

# 正解値ラベル
y_label = 'left'

# モデル
best_model = None

# csv読み込み時のオブジェクト指定
obj_type = {
    'sales': object,
    'salary': object
}

# one-hotエンコード用
ohe_columns = ['sales',
               'salary']

# データ読み込み
# input : csvパス, yラベル, オブジェクト型

train_flag = True
# train_flag = False
if train_flag:
    X, y = read_train(train_path, y_label, obj_type)

grids_select_n_flag = True
# grids_select_n_flag = False
if grids_select_n_flag:
    # グリッドサーチPCA
    gridSearchFunction_Select_n(X, y, ohe_columns, metrics)

# preprocess_flag = True
preprocess_flag = False
if preprocess_flag:
    # 前処理をして返却する
    # input : X, y, one-hotエンコードカラム, columnsパス, RFE/PCAフラグ, imputerパス, selectorパス
    X, y = preprocessing_train(X, y, ohe_columns, columns_path, rfepca, imputer_path, selector_path, select_n)

    # grids_flag = True
    grids_flag = False
    if grids_flag:
        # グリッドサーチ
        gridSearchFunction(X, y, metrics)


# best_flag = True
best_flag = False
if best_flag:
    # ベストモデルを決定
    # input : X, y, metrics, モデル名（手動選択の場合は入力）
    # 評価指標を選択
    # accuracy, precision, recall, f1, auc
    est_choice = ""
    best_model, best_name = modelValidation(X, y, metrics, est_choice)

# score_flag = True
score_flag = False
if score_flag:
    # スコア用データ
    # データ読み込み
    # input : csvパス, IDラベル, オブジェクト型
    X_s, ID_s = read_score(score_path, obj_type)

    # 前処理をして返却する
    # input : X_s, one-hotエンコードカラム, columnsパス, RFE/PCAフラグ, imputerパス, selectorパス
    X_s = preprocessing_score(X_s, ohe_columns, columns_path, rfepca, imputer_path, selector_path)

    # スコアリング
    # input : X_s, ID, best_model
    # 連続実行しない場合はbest_nameを手動入力
    # best_name = ""
    scoring(X_s, ID_s, best_model, best_name)
