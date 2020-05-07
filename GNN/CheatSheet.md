# GNN Cheat Sheet
## Introduction to Graphs
![](https://i.imgur.com/t4sRsd7.png =360x)
- A **graph** is often denoted by $G=(V,E)$
- $V=\{v_1,...,v_n\}$ is the set of **vertices**
    - $d(v)$ is the number of edges connected (**degree**) of vertice $v$, 
- $E = \{e_1,...,e_m\}$ is the set of **edges**
    - each edge $e$ has two **endpoints** $e=u,v$ joined by $e$
    - $u$ is then a **neighbour** of $v$, and $u, v \in V$
    - edges could be directed or undirected

Adjacent Matrix
: a.k.a connection matrix, denoted by $A_{ij} \in \mathbb{R}^{n \times n}$, represents if there is a connection between the vertices $i$ and $j$.
The matrix should be symmetric when $G$ is an undirected graph.

$$
A_{ij} = 
\begin{cases}
1 \ \text{ if } \{v_i, v_j\} \in E \text{ and } i \neq j \\
0 \ \text{ otherwise}
\end{cases}
$$

Degree Matrix
: is a diagonal matrix, denoted as $D_{ii} = d(v_i) \in \mathbb{R}^{n \times n}$, that shows the degree of each node.

***Other Algebraic Representations of Graphs***
- Laplacian matrix
- Symmetric normalized Laplacian
- Random walk normalized Laplacian
- Incidence matrix