from my_utils import MyUtils
import warnings
warnings.filterwarnings('ignore')

# #####################################################
# # スコアデータ前処理
# def preprocessing_score(X, ohe_columns, columns_path, rfepca, imputer_path, selector_path):
#
#     # モデルを復元
#     # カラム, 数値処理, 次元削減
#     X_columns = joblib.load(columns_path)
#     imp = joblib.load(imputer_path)
#     selector = joblib.load(selector_path)
#
#     # one-hotエンコーディング
#     # カテゴリ変数に適用する
#     X_s = pd.get_dummies(X,
#                            dummy_na=True,
#                            columns=ohe_columns)
#
#     cols_model = set(X_columns)
#     cols_score = set(X_s.columns.values)
#
#     # モデルにはあったがスコアにはないデータ項目
#     diff_m = cols_model - cols_score
#     # print('モデルのみに存在する項目: %s' % diff_m)
#
#     # スコアにはあるがモデルになかったデータ項目
#     diff_s = cols_score - cols_model
#     # print('スコアのみに存在する項目: %s' % diff_s)
#
#     # 空データでモデルデータのカラム
#     df_cols_m = pd.DataFrame(None,
#                              columns=X_columns,
#                              dtype=float)
#     X_s = pd.concat([df_cols_m, X_s])
#     # print(X_s.head())
#     # print('-' * 50)
#
#     # スコアデータのみに登場するデータを削除
#     X_s = X_s.drop(list(diff_s), axis=1)
#     # print(X_s.head())
#     # print('-' * 50)
#
#     # モデルデータのみに登場するデータを0埋め
#     X_s.loc[:, list(diff_m)] = X_s.loc[:, list(diff_m)].fillna(0, axis=1)
#     # print(X_s.head())
#     # print('-' * 50)
#
#     # モデリング時点のone-hotエンコーディング後の並び順にする
#     X_s = X_s.reindex(X_columns, axis=1)
#
#     # 数値型カラムの補完
#     X_s = pd.DataFrame(imp.transform(X_s),
#                         columns=X_columns)
#
#     # print(X_s.head())
#     # print('-' * 50)
#
#     # print(rfepca)
#     if rfepca == 'RFE':
#         X_fin_s = X_s.loc[:, X_columns[selector.support_]]
#     elif rfepca == 'PCA':
#         X_fin_s = pd.DataFrame(selector.transform(X_s))
#
#     # print(X_fin_s.head())
#     # print('-' * 50)
#
#     return X_fin_s
#
# #####################################################
# # スコアリング
# def scoring(X_s, ID_s, best_model, best_name=""):
#     # モデルを復元
#     if best_name != "" :
#         print('load model : ./model/'+ best_name + '.pkl')
#         best_model = joblib.load('./model/'+ best_name + '.pkl')
#     elif (best_model is None) and (best_name == ""):
#         print('Please input best_name because best_model is None!')
#         return
#
#     score = pd.DataFrame(best_model.predict_proba(X_s)[:, 1], columns=['pred_score'])
#     print('pred_score_to_csv')
#     ID_s.join(score).to_csv('./data/my_classifier_with_pred_' + best_name + '.csv', index=False)
#
#     return
#
# #####################################################


# train
TRAIN_PATH = './data/final_hr_analysis_train.csv'
# score
SCORE_PATH = './data/final_hr_analysis_test.csv'

# csv読み込み時のオブジェクト指定
OBJ_TYPE =   {
                'sales': object,
                'salary': object
              }

# one-hotエンコード用
OHE_COLUMNS = [
                 'sales',
                 'salary'
               ]

# 評価指標を選択
# metrics
# accuracy, precision, recall, f1, auc
metrics = 'accuracy'
# metrics = 'precision'
# metrics = 'recall'
# metrics = 'f1'
# metrics = 'auc'

selector_method = 'RFE'
# selector_method = 'PCA'

myutils = MyUtils('./param_clf.yml', OBJ_TYPE, metrics)

print(myutils.get_str_timestamp())

# mode = 'train'
mode = 'score'

if mode == 'train':

    # データ読み込み
    _, X, y = myutils.read_data(TRAIN_PATH)

    # 前処理
    X = myutils.train_data__preprocessing_with_imputer(X, OHE_COLUMNS)

    # 初回探索
    # 次元数選択
    # X_train, X_test, y_train, y_test = myutils.get_train_test_split(X, y, test_size=0.2)
    # select_n = myutils.select_n__gridsearch_with_rfe(X_train, y_train)
    select_n = 16

    # 特徴量選択
    if selector_method == 'RFE':
        X = myutils.train_data__preprocessing_with_rfe(X, y, select_n)

    # 初回探索
    # 推定器パラメータグリッドサーチ
    # myutils.clf__grid_search(X, y)

    # model validation
    # clf, best_est_name = myutils.model_validation(X, y)

if mode == 'score':
    est_name = 'R-forest'

    ID, X, _ = myutils.read_data(SCORE_PATH)
    X = myutils.score_data__preprocessing(X, OHE_COLUMNS, selector_method)
    myutils.predict_to_csv(ID, X, est_name)

print(myutils.get_str_timestamp())
