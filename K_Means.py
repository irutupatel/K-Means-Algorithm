from math import sqrt
import sys


def euclidean_distance(pointA, pointB):
    distance = float(0.0)
    for index in range(len(pointA)):
        distance += (pointA[index] - pointB[index])**2
    return sqrt(distance)


def get_centroid(points):
    centroid = [0]*len(points[0])
    for point in points:
        for whichDimension, value in enumerate(point):
            centroid[whichDimension] += value/len(points)
    return centroid


def cluster_associated_datapoints(datapoints, cluster_ids, interested_cluster_id):
    """
    Get datapoints belonging to each cluster for calculating new centroid for that cluster

    :param datapoints: Both parameters are of same size
    :param cluster_ids:
    :return:
    """
    associated_datapoints = list()
    whichDatapoints = [whichIndex for whichIndex, cluster_id in enumerate(cluster_ids) if cluster_id == interested_cluster_id]
    for whichDatapoint in whichDatapoints:
        associated_datapoints.append(datapoints[whichDatapoint])
    return associated_datapoints


def k_means(datapoints, clusters):
    """
    :param datapoints: [[8.98320053625, -2.08946304844],
                        [2.61615632899, 9.46426282022],
                        [1.60822068547, 8.29785986996],
                        [8.64957587261, -0.882595891607]]
    :param clusters: [[3.35228193353, 6.27493570626],
                        [6.76656276363, 6.54028732984]]

    :return: list returning cluster IDs for given points: [1,0,1,1]
    """

    stopping_condition_being_met = False

    while not stopping_condition_being_met:
        at_least_one_centroid_changed = False

        # Store distance of each point with its closest cluster; same size as len(datapoints) for exact mapping
        euclidean_distances = [float("inf")]*len(datapoints)

        # Store cluster ID of the closest cluster; same size as len(datapoints) for exact mapping
        cluster_ids = [0]*len(datapoints)

        # Step 1: Assign closest cluster to each point based on euclidean distances
        for whichDatapoint, datapoint in enumerate(datapoints):
            for whichCluster, clusterPoint in enumerate(clusters):
                distance = euclidean_distance(pointA=datapoint, pointB=clusterPoint)
                if distance < euclidean_distances[whichDatapoint]:
                    # Updating closest distance, and new cluster ID
                    euclidean_distances[whichDatapoint] = distance
                    cluster_ids[whichDatapoint] = whichCluster
                    # TODO: For efficiency, store cluster_to_datapoints_mapping right here,
                    #  to be used for calculating new centroid; finding mean of datapoints belonging to each cluster.
                    #  Hint: Could eliminate using cluster_associated_datapoints function by doing that here

        # Step 2: Finding new centroids; updating clusters
        for whichCluster_id in range(len(clusters)):
            # Get data points belonging to each cluster for calculating new centroid for that cluster
            points_in_cluster = cluster_associated_datapoints(datapoints=datapoints, cluster_ids=cluster_ids, interested_cluster_id=whichCluster_id)
            if len(points_in_cluster) == 1:
                new_centroid = points_in_cluster[0]
            else:
                new_centroid = get_centroid(points=points_in_cluster)
            old_centroid = clusters[whichCluster_id]
            clusters[whichCluster_id] = new_centroid
            if old_centroid != new_centroid:
                at_least_one_centroid_changed = True

        if not at_least_one_centroid_changed:
            stopping_condition_being_met = True

    return cluster_ids


def getInput():
    datapoints = [[8.98320053625, -2.08946304844], [2.61615632899, 9.46426282022], [1.60822068547, 8.29785986996],
                  [8.64957587261, -0.882595891607], [1.01364234605, 10.0300852081], [1.49172651098, 8.68816850944],
                  [7.95531802235, -1.96381815529], [0.527763520075, 9.22731148332], [6.91660822453, -3.2344537134],
                  [6.48286208351, -0.605353440895]]
    clusters = [[3.35228193353, 6.27493570626], [6.76656276363, 6.54028732984]]

    return datapoints, clusters


def getHackerrankInput():
    datapoints = list()
    clusters = list()
    firstline = True
    whichDatapoint = 0
    numberOfDatapoints = 0
    for line in sys.stdin.readlines():
        if firstline:
            numberOfDatapoints = int(line.strip().split()[0])
            firstline = False
        else:
            datapoint = list()
            cordinates = line.strip().split()
            for cordinate in cordinates:
                datapoint.append(float(cordinate))
            if whichDatapoint < numberOfDatapoints:
                datapoints.append(datapoint)
            else:
                clusters.append(datapoint)
            whichDatapoint += 1

    return datapoints, clusters


if __name__ == '__main__':

    # datapoints, clusters = getHackerrankInput()
    datapoints, clusters = getInput()
    cluster_ids = k_means(datapoints, clusters)
    for id in cluster_ids:
        print(id)