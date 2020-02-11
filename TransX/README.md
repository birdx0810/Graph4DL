# Translation Models for Knowledge Representation Learning
> Code: [THUNLP TensorFlow](https://github.com/thunlp/TensorFlow-TransX)

### TransE: Translating Embeddings for Modeling Multi-relational Data
> 2013  
> Paper: [Link](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data)

**TL;DR:**
- Sum of head vector $h$ and relation vector $r$ should be as close as possible to tail vector $t$
- Loss function: Max-margin with negative sampling
  - $L(h,r,t) = max(0, d_{pos} - d_{neg} + margin)$
  - $d = || h + r - t ||$
- Only practical for one-to-one relationships

**Objective Function**: $|| h + r - t ||^2_{l_{1/2}} \quad r \in R^k$

### TransH: Knowledge Graph Embedding by Translating on Hyperplanes
> 2014  
> Paper: [Link](https://www.aaai.org/ocs/index.php/AAAI/AAAI14/paper/view/8531/8546)

**TL;DR:**
- Project $h$ and $t$ to hyperplane, creating a new vector $h_\perp$ and $t_\perp$ which has a relation vector $d_r$
- $h_\perp + d_r \approx t_\perp$
- The loss function and training method are similar to TransE, only projected into a new hyperplane
- Do not take into account different aspects of entities

**Objective Function**: $|| (h-w^\intercal_rhw_r) + d_r - (t-w^\intercal_rtw_r) ||^2_{l_{1/2}} \quad r, w_r \in R^k$

### TransR: Learning Entity and Relation Embeddings for Knowledge Graph Completion
> 2015  
> Paper: [Link](https://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9571/9523)

**TL;DR:**
- Model entities into **entity space** and **multiple relation spaces**
- Entities are projected into $r$-relation space as $h_r$ and $t_r$ via operation $M_r$
- $h_r + r \approx t_r$
- The loss function and training method are similar to TransE, only projected to a new $r$-relation space
- Doesn't take into context that different types of entities need to be projected differently. Requires more parameters.

**Objective Function**: $|| M_rh + r - M_rt ||^2_{l_{1/2}} \quad r \in R^k, M_r \in R^{k \times k}$

**Note**:
- CTransR is a variant of TransR
  - cluster diverse head-tail entity pairs into groups and learn distinct relation vectors for each group

### TransD: Knowledge Graph Embedding via Dynamic Mapping Matrix
> 2015  
> Paper: [Link](https://www.aclweb.org/anthology/P15-1067/)

**TL:DR:**
- Uses two vectors to represent entity and relation:
  - Meaning representation of entity and relation
  - Projection vector for constructing mapping matrices
- Mapping matrices are defined as $M_{rn} = r_p n_p^T +I$, where $n$ could be head or tail node and $I$ is the identity matrix.
- The projection and training are similar to TransR
- TransE is a special case of TransD when $m=n$ and all projection vectors are set $0$

**Objective Function**: $|| (w_rw^\intercal_r + I)h + r - (w_rw^\intercal_r + I)t ||^2_{l_{1/2}} \quad r, w_r \in R^k$

### TransW
> 2019
> Paper: [Link](https://arxiv.org/abs/1909.03794)

**TL;DR:**
- Each entity/relation is represented in the form of a linear combination of word embeddings
- $w_{hi}, w_{ri}, w_{ti}$ are the $i$-th connection vector
- Includes bias parameters for head, relation, and tail
- Loss function:
    - $L = \sum_{\xi \in \Delta} \sum_{\xi' \in \Delta'} [ \gamma + f_r (\xi') - f_r (\xi)]_+$ 

**Objective Function**: $|| (\sum h_i \circ w_{hi} +b_h) + \sum r_i \circ w_{ri} - (\sum t_i \circ w_{ti} +b_t) ||^2_{l_{1/2}} \quad w_{ri} \in R^k$