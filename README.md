## result: for itai 

sum_of_non_anomaly =  255648

non_anomaly_predicted =  214185

non_anomaly_predicted_wrong =  41463

sum_of_anomaly =  1022

anomaly_predicted =  1022

anomaly_predicted_wrong =  0

#### accuracy = (non_anomaly_predicted + anomaly_predicted) / (sum_of_non_anomaly + sum_of_anomaly)
#### accuracy = (214185 + 1022) / (255648 + 1022)
#### accuracy = 83.84 % 

#### recall = anomaly_predicted / sum_of_anomaly
#### recall = 1022 / 1022
#### recall = 100 %

### Confution matrix and accuracy

|  | non_anomaly_predicted |anomaly_predicted |
| --- | --- | --- |
| actual non anomaly | 214185 | 41463 |
| actual anomaly | 0 | 1022 |


# StreamlitApps AnomalyDetection

## in this project we got dataset of anomaly files and then by using clustring k ml approch and midean aproch we mange to clasifed correctly 84 precent of the data that we got, you can read more about it down below.

![image](https://user-images.githubusercontent.com/73063199/210398975-0a764957-33ea-4519-8515-fc4256a49b95.png)

# Summary and results

1.	Data exploration- what have you learned ?
We learned how to read a dataset. We first read the different fields in the dataset (record ID, Duration_, src_bytes, dst_bytes) and explored the impact of each field on the results and the connections between the fields with some help of matplotlib ans seaborn libraries that visualize the data for us. We focused on a train set from the dataset and learn from it about the system. Then by using some ML algorithms we finally predicted the test set with some good results.
2.	Which algorithms group are suitable for this task and why?
K-Means Algorithm, the cluster and unsupervised group. The number of clusters identified from data by algorithm is represented by 'K' in K-means. In this algorithm, the data points are assigned to a cluster in such a manner that the sum of the squared distance between the data points and centroid would be minimum. We used this algorithm because we saw the scatters of the data in the graph and then we understand that k-cluster will give us some good results. In addition we add a MAD algorithm in order to get robust ML solution.
3.	Please create a report that will explain how you solved the problem?
a.	What is the approach you tried? Why them?
We used the K-means algorithm and median algorithms (MAD) that shows us the center points of the dataset in order to see which data are close to the norm and which is anomalous in a way that can recognize anomalous points with a good results. The cluster algorithm allow us to fins the norm points and from the other side the anomalous ones.
b.	How do you know the algorithm is good?
Based on the check we did in the notebook the results of the algorithm is around 83% which is high and cluster to the optimal solution.
4.	 What is the accuracy and recall of the algorithm the team developed? Show the confusion matrix. Will be ranked based on the results of the entire class
The accuracy of the algorithm is 83.4% as we calculated in the notebook where we found 214185 out of 256670 right predictions.
The recall of the algorithm is 83% if we consider non anomalous as Positive
and could be 100% if we consider anomalous as Positive (because there's no anomalous in the true csv file of the task).
