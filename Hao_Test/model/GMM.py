# 作者：hao.ren3
# 时间：2019/10/8 15:02
# IDE：PyCharm
"""
https://mp.weixin.qq.com/s/tZXa9GsqkT49YK7bZ83TuA
"""

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
# import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from sklearn.datasets.samples_generator import make_blobs

#产生实验数据
X, y_true = make_blobs(n_samples=700, centers=4,
                       cluster_std=0.5, random_state=2019)
X = X[:, ::-1] #方便画图
gmm = GMM(n_components=4).fit(X)
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.show()
# print(np.shape(X))
# print(X)
# print(np.shape(X))
# print(X)
