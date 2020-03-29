import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

n = 50

x0 = np.linspace(0, 2 * np.pi, num=n)
# print(x0)
y_org = np.sin(x0)
# print(y_org)
# sin波に誤差を付与する 乱数は0〜1の分布 -> -0.1〜0.1の分布に変換
y0 = np.sin(x0) + (np.random.rand(n)/5 - 0.5/5)
# print(y0)

# フレーム化
x = pd.DataFrame(x0, columns=['x'])
y = pd.DataFrame(y0, columns=['y'])

# 訓練とテストに分割
X_train,X_test,y_train,y_test = train_test_split(x, y,
                                                 test_size=0.20,
                                                 random_state=1)

# 整形
y_train = y_train.as_matrix().ravel()
y_test = y_test.as_matrix().ravel()

# 標準化、多項式基底、推定器をセット
pipe = Pipeline([('sc', StandardScaler()),
                 ('pl', PolynomialFeatures(degree=3)),
                 ('es', Ridge(alpha=0.1))
                 ])

# 学習
pipe.fit(X_train, y_train)

# 寄与率
print(r2_score(y_test, pipe.predict(X_test)))

# 誤差を付与した散布図
plt.scatter(x0, y0, label='data')
# sin波
plt.plot(x0, y_org, label='sin')
# 回帰
plt.plot(x0, pipe.predict(pd.DataFrame(x0)), label='predict')
# ラベル表示
plt.legend()
# グラフ表示
plt.show()