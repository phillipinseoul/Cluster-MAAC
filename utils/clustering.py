'''TODO: clustering the agents based on the position'''
from sklearn.cluster import KMeans
from collections import defaultdict


def cluster_agents(agents, positions, n_label):
    '''
    - input: 
        agents: list of agents indices
        positions: current position of each agent
    - output:
        cluster_list: dictionary of key=cluster index, value=list of agents
        (e.g., cluster_list = {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8]})
    '''

    kmeans = KMeans(n_clusters=n_label)
    kmeans.fit(positions)

    cluster_list = defaultdict(list)
    for label , index in zip(kmeans.labels_, agents):
        cluster_list[label].append(index)

    cluster_list = dict(map(lambda kv: (kv[0], kv[1].sort()), cluster_list.iteritems()))

    return cluster_list
