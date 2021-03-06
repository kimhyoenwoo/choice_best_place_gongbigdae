# -*- coding: utf-8 -*-
"""KMean_Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zh1gMY7e8huaKuRvQPaaYLdN9dEfXOlo
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler

from google.colab import drive
drive.mount('/content/drive')

#주성분 분석 산출물로 DataFrame 추출
df_new = pd.read_csv('/content/new_data.csv')
# df_new.iloc[120:150,]
df_new.iloc[128,6]=0
data_points = df_new[['ratio','bus_all']]
#표준화 

sclaer = StandardScaler()
sclaer.fit(data_points)
data_points_scaled = sclaer.transform(data_points)

data_points=data_points_scaled

# list(np.round(df_new['ratio'],5)
# list(np.round(df_new['ratio'],5))

#Kmeans 실시.

kmeans_1 = KMeans(n_clusters = 1).fit(data_points) # 클러스터 1
kmeans_2 = KMeans(n_clusters = 2).fit(data_points) # 클러스터 2 

kmeans_2_new = KMeans(init='k-means++').fit(data_points)

kmeans_3 = KMeans(n_clusters = 3).fit(data_points) # 클러스터 3 
kmeans_4 = KMeans(n_clusters = 4).fit(data_points) # 클러스터 4 
kmeans_5 = KMeans(n_clusters = 5).fit(data_points) # 클러스터 5 
# for i in range(6,11):
#   kmeans_i = KMeans(n_clusters = i).fit(data_points)
#   print(kmeans_i)
kmeans_6 = KMeans(n_clusters = 6).fit(data_points) # 클러스터 6 
kmeans_7 = KMeans(n_clusters = 7).fit(data_points) # 클러스터 7
kmeans_8 = KMeans(n_clusters = 8).fit(data_points) # 클러스터 8 
kmeans_9 = KMeans(n_clusters = 9).fit(data_points) # 클러스터 9 
kmeans_10 = KMeans(n_clusters = 10).fit(data_points) # 클러스터 10

#Kmeans의 클러스터 개별 값
kmeans_1.labels_

kmeans_2_new.labels_

#KMeans Cluster의 Centroid값만 추출
# kmeans.cluster_centers_



#본 데이터 셋에 Cluster 값을 추가.
df_new['cluster_id'] = kmeans_2.labels_
df_new_2 = df_new.copy()
df_new['cluster_id'] = kmeans_2_new.labels_
df_new_2_new = df_new.copy()
df_new['cluster_id']= kmeans_3.labels_
df_new_3 = df_new.copy()
df_new['cluster_id']= kmeans_4.labels_
df_new_4 = df_new.copy()
df_new['cluster_id']= kmeans_5.labels_
df_new_5 = df_new.copy()

df_new['cluster_id']= kmeans_10.labels_
df_new_10 = df_new.copy()

df_new_2_new

# abc = pd.DataFrame(data_points)
# abc.columns = ['ratio_1','bus_all_1']
# abc = pd.concat([df_new_2,abc],axis=1)
# abc = abc.drop(['ratio','bus_all'],axis=1)
# df_new_2 = abc

# KMeans Cluster 시각화
# fig, ax = plt.subplots()
sns.lmplot('bus_all', 'ratio', data=df_new_2, fit_reg=False,  
           scatter_kws={"s": 10}, # marker size
           hue="cluster_id") # color
# plt.xlim(0,2500)
# ax.set_xlim(0.2)
plt.title('kmean clustering_2')
# plt.savefig('군집.png')

# KMeans Cluster 시각화
# fig, ax = plt.subplots()
sns.lmplot('bus_all', 'ratio', data=df_new_2_new, fit_reg=False,  
           scatter_kws={"s": 10}, # marker size
           hue="cluster_id") # color
# plt.xlim(0,2500)
# ax.set_xlim(0.2)
plt.title('kmean clustering_2')
# plt.savefig('군집.png')

# KMeans Cluster 시각화
# fig, ax = plt.subplots()
sns.lmplot('bus_all', 'ratio', data=df_new_2, fit_reg=False,  
           scatter_kws={"s": 10}, # marker size
           hue="cluster_id") # color
plt.xlim(0,2500)
# ax.set_xlim(0.2)
plt.title('kmean clustering_2')
# plt.savefig('군집.png')

# KMeans Cluster 시각화
sns.lmplot('bus_all', 'ratio', data=df_new_10, fit_reg=False,  
           scatter_kws={"s": 10}, # marker size
           hue="cluster_id") # color
plt.xlim(0,2000000)
plt.ylim(0,100)
plt.title('kmean clustering_10')
# plt.savefig('군집.png')

#Data의 Cluster값을 개별로 확인
# pd.DataFrame(df_new_2[df_new_2.cluster_id == 0])
pd.DataFrame(df_new_2[df_new_2.cluster_id == 1])

# data2 = pd.DataFrame(df2[df2.cluster_id == 1])
#df5 = df4.loc[data1,:]

print(kmeans_1.inertia_)
print(kmeans_2.inertia_)
print(kmeans_3.inertia_)
print(kmeans_4.inertia_)
print(kmeans_5.inertia_)
print(kmeans_6.inertia_)
print(kmeans_7.inertia_)
print(kmeans_8.inertia_)
print(kmeans_9.inertia_)
print(kmeans_10.inertia_)

df_new_2.groupby('cluster_id').median()

df_new_3.groupby('cluster_id').median()

df_new_4.groupby('cluster_id').median()

df_new_4.groupby('cluster_id').median()

df_new_2_new.groupby('cluster_id').median() ###############

pd.DataFrame(df_new_2_new[df_new_2_new.cluster_id == 1]) #####

pd.DataFrame(df_new_2_new[df_new_2_new.cluster_id == 1])##

pd.DataFrame(df_new_2_new[df_new_2_new.cluster_id == 5])

pd.DataFrame(df_new_2_new[df_new_2_new.cluster_id == 4])######

pd.DataFrame(df_new_2_new[df_new_2_new.cluster_id == 6])##

pd.DataFrame(df_new_2_new[df_new_2_new.cluster_id == 3])#####

pd.DataFrame(df_new_2_new[df_new_2_new.cluster_id == 7])

df_new_5.groupby('cluster_id').median()

pd.DataFrame(df_new_5[df_new_5.cluster_id == 2])

pd.DataFrame(df_new_5[df_new_5.cluster_id == 1])

pd.DataFrame(df_new_5[df_new_5.cluster_id == 4])

df_new_10.groupby('cluster_id').median()

pd.DataFrame(df_new_10[df_new_10.cluster_id == 2])

"""추가적으로 보면 좋을 것들."""

# data1.describe()

"""# 새 섹션"""

# data2.describe()

# data1.columns

# list = data1['택스_승차합', '택시_하차합', 'BUS_정류장_개수', 'BUS_탑승', 'BUS_하차',
#        'BUS_환승', '고령인구 발생량', '고령인구 도착량']

# for i in list :
#   Q1 = data1[i].quantile(0.25)
#   Q3 = data1[i].Quantile(0.75)
#   IQR = Q3 - Q1

# data2 = data1[ (data1[a] < Q1-1.5*IQR) | (data1[a] > Q3 + 1.5 * IQR)].index
# data1.drop(data2,inplace = True)
# data1

a=pd.Series(data2['BUS_하차']).sort_values(ascending=False)
b=a.reset_index()
#1451.250000 0.25
#104624.000000 0.75

# b[b.BUS_하차>1451] & b[b.BUS_하차<104624]
#(b['BUS_하차']>1451 and b['BUS_하차']<104624)
c= b[b['BUS_하차']>1451]
c

#df5.to_csv('주요_법정동.csv', index=False, encoding='cp949')
data2.shape
