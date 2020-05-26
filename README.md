# K-Means Algorithm
This assignment aims to familiarize you with the mechanism of two widely-used clustering methods: k-means

k-means is an iterative clustering algorithm that aims to cluster points such that every point is assigned to its nearest cluster. Please use Euclidean distance to compute the distance between any pair of points.

## Model Specification
For k-means, the input shall comprise of N points and k initial cluster centroids. The points and the clusters are 0-indexed separately. In other words, the first point has index 0 and the second point has index 1 and so on. Similarly, the clusters are indexed from 0 to k − 1.

**The following design choice in implementation purely aims to ease auto- grading on HackerRank.** Since we are to use HackerRank for grading, we have to eliminate additional random- ness and generate the deterministic results. We therefore enforce the following rule in this assignment:
- For the k-means algorithm, we assign the points to the smallest indexed cluster in case of ties (i.e., when the distances are same). In other words, you need to break ties by assigning a point to the cluster with the lowest index if there are several equidistant clusters.

## Input Format and Sample
We ensure that the labels for N input points and k cluster are named by **non-negative
integer** following zero-based numbering.

The first line of input will be N and k (space in between). This will be followed by N input points where the points co-ordinates are space separated. The data type of the input points is floating number. The k initial cluster points for k-means method shall follow the input points.

    10 2
    8.98320053625 -2.08946304844 
    2.61615632899 9.46426282022 
    1.60822068547 8.29785986996 
    8.64957587261 -0.882595891607 
    1.01364234605 10.0300852081 
    1.49172651098 8.68816850944 
    7.95531802235 -1.96381815529 
    0.527763520075 9.22731148332 
    6.91660822453 -3.2344537134 
    6.48286208351 -0.605353440895 
    3.35228193353 6.27493570626 
    6.76656276363 6.54028732984 
    
In this example the goal of the clustering task is to find the groups among 10 data points as illustrated in Figure 1. The k value for this example is 2, and we provide two random selected initial points at the end of the input.

## Output Format and Sample
The output is the clustering results on the provided data made by k-means. For each method, print the cluster-id corresponding to each point on separate lines.

As an example, the outputs of the toy example are as follows. For K-Means, the sample output is:

    1 
    0 
    0 
    1 
    0 
    0 
    1 
    0 
    1 
    1
