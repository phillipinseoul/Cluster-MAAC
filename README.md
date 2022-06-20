# C-MAAC: Cluster-based Multi-Actor Attention Critic for Reinforcement Learning
Project for KAIST CS470: Introduction to Artifical Intelligence (Spring 22') by Hyuncheol Park, Taeyeong Lee, Yuseung Lee and Jongjun Park. This work is an extension of the [original MAAC (Iqbal et al., ICML 2019)](https://arxiv.org/abs/1810.02912) and the baseline codes for MAAC was forked from the [official repository](https://github.com/shariqiqbal2810/MAAC).

Abstract: Multi-Actor-Attention-Critic (MAAC) proposed an efficient form of an actor-critic algorithm for multi-agent environments by integrating it with the attention mechanism from [10]. In this paper, we test MAAC on two MPE environments Simple Tag and Simple Spread, then propose an extension of this method, C-MAAC, by introducing a new component Cluster Critic into the original critic pipeline. The experimental results show that our method fails to achieve superior results compared to the original MAAC, but we provide an analysis of the possible ways to improve the performance. Code is available at https://github.com/CS470RL/maac-MPE.

## Requirements
#### 1. Install the packages in requirement.txt
```shell
pip install -r requirements.txt 
```

#### 2. Install OpenAI Baselines
* From https://github.com/openai/baselines
* Since Baselines automatically installs gym==0.15.7, you may need to uninstall this version and reinstall gym==0.9.4.
```shell
git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .
```

#### 3. Install Multi-Agent Particle Environment
* From https://github.com/shariqiqbal2810/multiagent-particle-envs
```shell
git clone https://github.com/shariqiqbal2810/multiagent-particle-envs.git
cd multi-agents-envs
pip install -e .
```

## How to Run 

#### Warning! Running on SSH Server without GUI
* Write 'xvfb-run -a' before your commands.
```shell
xvfb-run -a python run_simple_tag.py ex --clst_ratio 0.5 --use_gpu
```

#### 1. Run Simple Tag 
* Environment: [Simple Tag (PettingZoo)](https://www.pettingzoo.ml/mpe/simple_tag)
```shell
python run_simple_tag.py test_1
```
* Experiment 1. Good=10, Adversary=5, Landmark=0
* Experiment 2. Good=5, Adversary=10, Landmark=0

#### 2. Run Simple Adversary 
* [Simple Adversary (PettingZoo)](https://www.pettingzoo.ml/mpe/simple_adversary)
```shell
python run_simple_adversary.py test_1
```
* Experiment 1. Good=10, Adversary=5, Landmarks=3
* Experiment 2. Good=5, Adversary=10, Landmarks=3
