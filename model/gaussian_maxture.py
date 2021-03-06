# -*- coding: utf-8 -*-
"""Gaussian Maxture.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LOrJN4M69zR9LsBTF4MTmRQh20eFfLuG
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('/content/drive/MyDrive/공빅데_대전_87조/코드 /New_data_1.csv',sep=',',encoding = 'UTF-8')
data.columns

feature_names = ['bus_stop_num', 'bus_all', 'old_all', 'taxi_all', 'ratio']

from google.colab import drive
drive.mount('/content/drive')

from sklearn.mixture import GaussianMixture
DF = data[['bus_stop_num', 'bus_all', 'old_all', 'taxi_all']]

gmm = GaussianMixture(n_components=3, random_state=42)
gmm_labels = gmm.fit_predict(DF)

# 보다 편리한 데이타 Handling을 위해 DataFrame으로 변환


#DF1 = data[['택스_승차합', '택시_하차합', 'BUS_정류장_개수', 'BUS_탑승', 'BUS_하차','BUS_환승','고령인구 발생량','고령인구 도착량']]
# GMM 후 클러스터링 레이블을 따로 설정
DF['gmm_cluster'] = gmm_labels

# 실제 레이블과 GMM 클러스터링 후 레이블과 비교해보기(두 레이블 수치가 동일해야 똑같은 레이블 의미 아님!)
print(DF.groupby('gmm_cluster')['gmm_cluster'].value_counts())

from sklearn.mixture import GaussianMixture as GMM
import matplotlib.pyplot as plt

b = np.log(DF)

k= np.arange(1,10,1)
clfs= [GMM(n,covariance_type='full').fit(b) for n in k]
aics= [clf.aic(b) for clf in clfs]
bics= [clf.bic(b) for clf in clfs]
plt.plot(k,bics,color='orange',marker='.',label='BIC')
plt.plot(k,aics,color='g',label='AIC')
plt.legend()
plt.show()

DF

def visualize_cluster_plot(clusterobj, dataframe, label_name, iscenter=True):
    if iscenter :
        centers = clusterobj.cluster_centers_
        
    unique_labels = np.unique(dataframe[label_name].values)
    markers=['o', 's', '^', 'x', '*', '8', 's', 'p']
    isNoise=False

    for label in unique_labels:
        label_cluster = dataframe[dataframe[label_name]==label]
        if label == -1:
            cluster_legend = 'Noise'
            isNoise=True
        else :
            cluster_legend = 'Cluster '+str(label)
        
        plt.scatter(x=label_cluster['bus_all'], y=label_cluster['ratio'], s=70,\
                    edgecolor='k', marker=markers[label], label=cluster_legend)
        
        if iscenter:
            center_x_y = centers[label]
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=250, color='white',
                        alpha=0.9, edgecolor='k', marker=markers[label])
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k',\
                        edgecolor='k', marker='$%d$' % label)
    if isNoise:
        legend_loc='upper center'
    else: legend_loc='upper right'
    
    plt.legend(loc=legend_loc)
    plt.show()

gmm = GaussianMixture(n_components=8, random_state=0)
gmm_label = gmm.fit(DF).predict(DF)
DF['gmm_label'] = gmm_label 

visualize_cluster_plot(gmm , DF , 'gmm_label' , iscenter=False)

# DF['gmm_cluster'].tolist()
DF.groupby('gmm_label').median() # ratio가 높고, bus_all이 높은 클러스터 10개 이상 뽑기 / 겹치는 법정동 리스트 뽑기

DF.groupby('gmm_label').mean()

# pd.DataFrame(DF[gmm.fit(DF).predict(DF)==2])

cluster = pd.merge(DF[gmm.fit(DF).predict(DF)==2], data, how='inner')
rst = pd.DataFrame(cluster)
rst

cluster = pd.merge(DF[gmm.fit(DF).predict(DF)==4], data, how='inner')
rst = pd.DataFrame(cluster)
rst

cluster = pd.merge(DF[gmm.fit(DF).predict(DF)==1], data, how='inner')
rst = pd.concat([rst, cluster])
rst

cluster = pd.merge(DF[gmm.fit(DF).predict(DF)==5], data, how='inner')
rst = pd.concat([rst, cluster])
rst

rst.to_csv('gmm_result_for_4cluster.csv')

# from sklearn.preprocessing import StandardScaler
# x_1 = StandardScaler().fit_transform(x)

# from sklearn.decomposition import PCA
# pca = PCA(n_components=2)
# principalComponents = pca.fit_transform(DF1)
# principalDf1 = pd.DataFrame(data = principalComponents, columns = ['pca1', 'pca2'])

# principalDf1

# pd.concat([DF,principalDf1], axis = 1)

# gmm = GaussianMixture(n_components=3, random_state=0)
# gmm_label = gmm.fit(DF).predict(DF)
# DF['gmm_label'] = gmm_label 

# visualize_cluster_plot(gmm , DF , 'gmm_label' , iscenter=False)

