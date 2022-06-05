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

'''make cluster list by role'''

def init_cluster_list(env, n_good, n_adv , n_obs = 2):

    cluster_lists = []
    obs = env.reset()

    nagents = len(env.action_space)

    OTHER_OFFSET = 4 + n_obs * 2

    agent_list = []
    for rolloutNum, arr in enumerate(obs):

        good_agents={}
        adv_agents={}

        agent_obs = arr[0]

        for idx in range(1,nagents): # all other agents except me

                relX = agent_obs[OTHER_OFFSET + 2*idx] # other pos X (relative)
                relY = agent_obs[OTHER_OFFSET + 2*idx + 1] # other pos Y (relative)
                    
                if env.agent_types[idx] == 'agent':
                    good_agents[idx] = (relX,relY)
                else:
                    adv_agents[idx] = (relX,relY)
        
        agent_list.append((good_agents, adv_agents))




    for rolloutNum, (good_agents, adv_agents) in enumerate(agent_list):
        good_cluster = cluster_agents(good_agents.keys(),good_agents.values() , n_good)
        adv_cluster = cluster_agents(adv_agents.keys(),adv_agents.values(), n_adv)


        ''' add if there ere  exists empty list in clusterlist'''

        for i in range(n_good):
            if i not in good_cluster.keys():
                good_cluster[i] = []

        for i in range(n_adv):
            if not i in adv_cluster.keys():
                adv_cluster[i] = []



        for k,v in good_cluster.keys():
            good_cluster[n_adv + k] = good_cluster.pop(k) 
        cluster_list =  adv_cluster.update(good_cluster)
        cluster_lists.append(cluster_list)
      
    return cluster_lists
