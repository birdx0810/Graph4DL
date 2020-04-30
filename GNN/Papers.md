# Graph Neural Network Papers

## The Graph Neural Network Model
###### GraphNetworks
>  Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, Gabriele Monfardini  
>  Paper: [Link](https://ieeexplore.ieee.org/document/4700287)  

### Introduction
- The GNN is designed specifically to handle graph-structured data, such as social networks, molecular structures, knowledge graphs, etc.
- A node is naturally defined by its features and related nodes in the graph.

> The objective of a GNN is to learn the state embedding $\mathbf{h}_v \in \mathbb{R}^s$ which encodes the information of the neighbourhood for each node.

- Each node in the graph has an input features $\mathbf{x}_v$ (edges may also have features).
- The state embedding $\mathbf{h}_v$ is used to produce an output $\mathbf{o}_v$, such as the distribution of the predicted node label.

**Note**:
- The Vanilla GNN only deals with undirected homogeneous graph.


### Methodology
![](https://i.imgur.com/zm73JNO.png =480x)

***Local***
$$
\begin{aligned}
\mathbf{h}_v &= f(\mathbf{x}_v, \mathbf{x}_{e[v]}, \mathbf{h}_{n[v]},\mathbf{x}_{n[v]}) \\
\mathbf{o}_v &= g(\mathbf{h}_v, \mathbf{x}_v)
\end{aligned}
$$

- $f$ is the *local transition function*
- $g$ is the *local output function*
- $n[v]$ is the neighbour set of node $v$
- $e[v]$ is the set of edges of node $v$
- $\mathbf{x}_v$ are the features of node $v$
- $\mathbf{x}_{e[v]}$ are the features of the edges
- $\mathbf{h}_{n[v]}$ are the states of each neighbour node
- $\mathbf{x}_{n[v]}$ are the features of each neighbour node

***Global***
$$
\begin{aligned}
\mathbf{H}^{t+1} &= F(\mathbf{H}^t, \mathbf{X}) \\
\mathbf{O} &= G(\mathbf{H}, \mathbf{X}_N)
\end{aligned}
$$

- $F$ is the *global transition function*
    - stacked version of $f$
- $G$ is the *global output function*
    - stacked version of $g$
- $\mathbf{H}$ is the matrix constructed by stacking all states
- $\mathbf{O}$ is the matrix constructed by stacking all outputs
- $\mathbf{X}$ is the matrix constructed by stacking all features
- $\mathbf{X}_N$ is the matrix constructed by stacking all node features

The objective function for a GNN could be written as
$$
\text{loss} = \sum_{i=1}^N(\mathbf{t}_i - \mathbf{o}_i)
$$
Where,
- $N$ is the number of supervised nodes
- $\mathbf{t}_v$ is the target information of a specific node
- The states $\mathbf{h}_v^t$ are iteratively updated by $f$ until time step $T$. We could then obtain an approximate fixed point solution $\mathbf{H}(T)\approx\mathbf{H}$ from $F$ by [Banach’s fixed point theorem](https://en.wikipedia.org/wiki/Banach_fixed-point_theorem).
- The gradient of weights $\mathbf{W}$ are computed by the loss, and updated according to the gradient computed at the last step $T$.

### Limitations
- The model needs T steps of computation to approximate the fixed point.
- Vanilla GNN uses the same parameters in the iteration.
- Edge could not be effectively modeled in vanilla GNN.

## Graph Convolutional Networks
###### GraphNetworks
> Thomas N. Kipf, Max Welling (9 Sep 2016)  
> Paper: [Link](https://arxiv.org/abs/1609.02907)  

## GraphSAGE
###### GraphNetworks
> William L. Hamilton, Rex Ying, Jure Leskovec (7 Jun 2017)  
> Stanford: [Link](http://snap.stanford.edu/graphsage/)  

### Graph Attention Networks
###### GraphNetworks
> Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Liò, Yoshua Bengio (30 Oct 2017)  
> Paper: [Link](https://arxiv.org/abs/1710.10903)  

## Meta-GNN
###### GraphNetworks
> Fan Zhou, Chengtai Cao, Kunpeng Zhang, Goce Trajcevski, Ting Zhong, Ji Geng  (23 May 2019)  
> Paper: [Link](https://arxiv.org/abs/1905.09718)  

## Graph Transformer Networks
###### GraphNetworks
> Seongjun Yun, Minbyul Jeong, Raehyun Kim, Jaewoo Kang, Hyunwoo J. Kim (6 Nov 2019)  
> Paper: [Link](https://arxiv.org/abs/1911.06455)  

## DeepWalk
###### Graph Embeddings
> Bryan Perozzi, Rami Al-Rfou, Steven Skiena (27 Jun 2014)  
> Paper: [Link](https://arxiv.org/abs/1403.6652)  

The skip-gram of graph networks.

## LINE
###### Graph Embeddings
> Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, Qiaozhu Mei (12 Mar 2015)  
> Paper: [Link](https://arxiv.org/abs/1503.03578)  


## Node2Vec
###### Graph Embeddings
> Aditya Grover, Jure Leskovec (3 Jul 2016)  
> Stanford: [Link](https://snap.stanford.edu/node2vec/)  

## Graph2Vec
###### ???
> Annamalai Narayanan, Mahinthan Chandramohan, Rajasekar Venkatesan, Lihui Chen, Yang Liu, Shantanu Jaiswal  
> Paper: [Link](https://arxiv.org/abs/1707.05005)  


## References
Papers
: [THUNLP's Must Read GNN Papers](https://github.com/thunlp/GNNPapers)
Tutorials
: [SNAP WWW-18 Tutorial on Representation Learning on Networks](http://snap.stanford.edu/proj/embeddings-www/)