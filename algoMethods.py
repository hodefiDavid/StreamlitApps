import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sklearn.datasets
from sklearn.cluster import KMeans
import math


# based on https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203
def how_many_cluster_we_need():
    f_path = "C:\\Users\\david\\Documents\\אריאל\\תשפג חורף\\שיטות לגילוי התקפות סייבר\\New folder\\מטלה 1\\conn_attack.csv"
    df = pd.read_csv(f_path, names=["record ID", "duration_", "src_bytes", "dst_bytes"], header=None)
    B = df[["src_bytes", "dst_bytes"]].values
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(B)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


# how_many_cluster_we_need()

def in_range_of_cluster(centroids, dot, distance) -> bool:
    arr = []
    arr.append(math.dist(centroids[0], dot))
    arr.append(math.dist(centroids[1], dot))
    arr.append(math.dist(centroids[2], dot))
    arr.append(math.dist(centroids[3], dot))
    arr.sort()
    if arr[0] > distance:
        return False
    else:
        return True


# given that we have 4 cluster as the elbo method suggested
# we now want to know what is the best distance between the cluster to the rest

def dist_from_cluster_we_need():
    f_path = "C:\\Users\\david\\Documents\\אריאל\\תשפג חורף\\שיטות לגילוי התקפות סייבר\\New folder\\מטלה 1\\conn_attack.csv"
    df = pd.read_csv(f_path, names=["record ID", "duration_", "src_bytes", "dst_bytes"], header=None)
    B = df[["src_bytes", "dst_bytes"]].values
    kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(B)
    centroids = kmeans.cluster_centers_

    collec_data = {}

    # 1/4 of the data
    for distance in range(1000, 10000, 500):
        for i in range(50000):

            if in_range_of_cluster(centroids, B[i], distance):
                if collec_data.get(distance) is None:
                    collec_data[distance] = 1
                else:
                    collec_data[distance] += 1

    print(collec_data)
    lists = sorted(collec_data.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    plt.plot(x, y)
    plt.title('dist_from_cluster_we_need')
    plt.xlabel('distance')
    plt.ylabel('number of correct defined (50000 over all)')
    plt.show()


# dist_from_cluster_we_need()
# according to the result we should defind the distance 4000

# second method mad

def mad_avg():
    f_path = "C:\\Users\\david\\Documents\\אריאל\\תשפג חורף\\שיטות לגילוי התקפות סייבר\\New folder\\מטלה 1\\conn_attack.csv"
    df = pd.read_csv(f_path, names=["record ID", "duration_", "src_bytes", "dst_bytes"], header=None)
    Y = df["src_bytes"].values
    X = df["dst_bytes"].values
    arrY = np.array(Y)
    arrX = np.array(X)
    avgy = np.mean(arrY)
    avgx = np.mean(arrX)
    medy = np.median(arrY)
    medx = np.median(arrX)
    print(avgy, "avgy")
    print(avgx, "avgx")
    print(medx, "medx")
    print(medy, "medy")

    collec_dataY = {}
    collec_dataX = {}

    # 1/4 of the data
    for distance in range(0, 300, 20):
        for i in range(50000):
            if abs(Y[i] - avgy) < distance or abs(Y[i] - medy) < distance:
                if collec_dataY.get(distance) is None:
                    collec_dataY[distance] = 1
                else:
                    collec_dataY[distance] += 1

    for distance in range(100, 3000, 100):
        for i in range(50000):
            if abs(X[i] - avgy) < distance or abs(X[i] - medx) < distance:
                if collec_dataX.get(distance) is None:
                    collec_dataX[distance] = 1
                else:
                    collec_dataX[distance] += 1

    print(collec_dataX)
    print(collec_dataY)
    lists = sorted(collec_dataY.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    plt.plot(x, y)
    plt.title('MAD - Y src ')
    plt.xlabel('distance')
    plt.ylabel('number of correct defined (50000 over all)')
    plt.show()

    lists = sorted(collec_dataX.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    plt.plot(x, y)
    plt.title('MAD - X dst')
    plt.xlabel('distance')
    plt.ylabel('number of correct defined (50000 over all)')
    plt.show()


# mad_avg()


f_path = "C:\\Users\\david\\Documents\\אריאל\\תשפג חורף\\שיטות לגילוי התקפות סייבר\\New folder\\מטלה 1\\conn_attack.csv"
df = pd.read_csv(f_path, names=["record ID", "duration_", "src_bytes", "dst_bytes"], header=None)
B = df[["src_bytes", "dst_bytes"]].values
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(B)
centroids = kmeans.cluster_centers_
print("[", int(centroids[0][0]), ",", int(centroids[0][1]), "]")
print("[", int(centroids[1][0]), ",", int(centroids[1][1]), "]")
print("[", int(centroids[2][0]), ",", int(centroids[2][1]), "]")
print("[", int(centroids[3][0]), ",", int(centroids[3][1]), "]")
