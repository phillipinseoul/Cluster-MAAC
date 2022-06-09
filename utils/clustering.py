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

    cluster_list = {clst : sorted(agentList) for clst, agentList in cluster_list.items()}

    return cluster_list

'''make cluster list by role'''

def init_cluster_list(env, n_good, n_adv , n_obs = 2):
    cluster_lists = []
    obs = env.reset()
    agent_list = []
    for rolloutNum, arr in enumerate(obs):
        good_agents={}
        adv_agents={}

        for agentNum, agent_obs in enumerate(arr):
        # for idx in range(1,nagents):
            myX = agent_obs[2] # my pos X
            myY = agent_obs[3] # my pos Y
                
            if env.agent_types[agentNum] == 'agent':
                good_agents[agentNum] = (myX, myY)
            else:
                adv_agents[agentNum] = (myX, myY)
        
        agent_list.append((good_agents, adv_agents))

    for rolloutNum, (good_agents, adv_agents) in enumerate(agent_list):
        good_cluster = cluster_agents(good_agents.keys(), list(good_agents.values()), n_good // 3)
        adv_cluster = cluster_agents(adv_agents.keys(), list(adv_agents.values()), n_adv // 3)

        ''' add if there ere  exists empty list in clusterlist'''
        # merge good/adv clusters into one list
        idx = 0
        tmp = dict()
        for clst, agentList in adv_cluster.items():
            tmp[idx] = agentList
            idx += 1
        for clst, agentList in good_cluster.items():
            tmp[idx] = agentList
            idx += 1
        cluster_lists.append(tmp)
      
    return cluster_lists

# init_cluster_lists for COLLABORATIVE environments
def init_cluster_list_collab(env, n_agents, n_obs = 2):
    cluster_lists = []
    obs = env.reset()

    agent_list = []
    for rolloutNum, arr in enumerate(obs):
        tot_agents = {}

        for agentNum, agent_obs in enumerate(arr):
        # for idx in range(1,nagents):
            myX = agent_obs[2] # my pos X
            myY = agent_obs[3] # my pos Y
            tot_agents[agentNum] = (myX, myY)
        agent_list.append(tot_agents)

    for rolloutNum, agents in enumerate(agent_list):
        cluster = cluster_agents(agents.keys(), list(agents.values()), n_agents // 3)

        ''' add if there ere  exists empty list in clusterlist'''
        # merge good/adv clusters into one list
        idx = 0
        tmp = dict()
        for clst, agentList in cluster.items():
            tmp[idx] = agentList
            idx += 1
        cluster_lists.append(tmp)
      
    return cluster_lists