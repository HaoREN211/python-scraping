# 作者：hao.ren3
# 时间：2019/10/8 15:12
# IDE：PyCharm

import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from python_scraping.Hao_Test.tools.ellipse import plot_gmm
from sklearn.datasets.samples_generator import make_blobs

rng = np.random.RandomState(13)

X, y_true = make_blobs(n_samples=700, centers=4,
                       cluster_std=0.5, random_state=2019)
X = X[:, ::-1] #方便画图

X_stretched = np.dot(X, rng.randn(2, 2))
gmm = GMM(n_components=4, covariance_type='full', random_state=42)
plot_gmm(gmm, X_stretched)
