# Translation Models for Knowledge Representation Learning
> Code: [THUNLP TensorFlow](https://github.com/thunlp/TensorFlow-TransX)

Knowledge graphs (e.g. FreeBase, WikiData, GeneOntology, MeSH etc.) are known for being helpful for AI and NLP tasks, yet there is still a big issue in the completion and coverage of these KGs. Hence, many research have placed efforts in unsupervised extraction of implicit relation facts without requiring extra knowledge, a.k.a **Link Prediction** and **Knowledge Graph Completion**.

### TransE: Translating Embeddings for Modeling Multi-relational Data
> Antoine Bordes, Nicolas Usunier, Alberto Garcia-Duran, Jason Weston, Oksana Yakhnenko (NIPS 2013)  
> Paper: [Link](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data)

**Multi-relational data**  
- ..refers to directed graphs whose nodes correspond to *entities* and *edges of the form (head, relation, tail).  
- Modeling multi-relational data refers to the extraction of local and global connectivity patterns between entities and generalize the observed relationship between a specific entity and all others.
- The *notion of locality* of relational data may involve relationships and entities of different types at the same time.
- Recent approaches have focused on increasing the expressivity and universality of the model with the expense of higher complexity, and thus overfitting.

**Relations as translations**
- Relationships are represented as *translations in the embedding space*.
- Hierarchical relationships are extremely common in KBs and translations are the natural transformations for representing them.
- Another motivation comes from word2vec, where 1-to-1 relationships between entities are extracted and represented into word embeddings, which could also probably be done in KBs.
- Hence, we attempt to use a low-dimensional vector to represent key relationships between entities in KBs.

Contribution:
- Easy to train
- Reduced parameters (Low dimensional)
- Scalable

#### Methodology
Proposed an **energy-based model** for learning low-dimensional embeddings of entities.
- *Energy-based models* capture dependencies by associating a *scalar energy* (a measure of compatibility) to each configuration of the variables.
- *Learning* consists in finding an energy function that associates low energies to correct values of the remaining variables, and higher energies to incorrect values.
- The loss function to measure the quality of the available energy functions is minimized during learning.
  - Here, a margin-based ranking criterion is used.

$$
\mathcal{L} = \sum_{(h,r,t)\in S}\sum_{(h',r',t')\in S'_{(h,r,t)}}\Big[ max(0, \gamma + d(h+r, t) - d(h'+r, t')) \Big]
$$

Where, 
- $d(h+r, t)$ is the energy of a triplet, where $d()$ is the dissimilarity measure ($L_1$ or $L_2$-norm).
  - if $d(h+r, t) < d(h'+r, t')$, then the loss is $0$
  - if $d(h+r, t) > d(h'+r, t')$, then the loss is $> 0$
- $d(h'+r, t')$ is the a corrupted triplet, where the head or tail is a false entity.
- $\gamma > 0$ is the margin threshold

If we consider $d$ as the squared euclidean distance for our dissimilarity function:
$$
d(h+r, t) = ||h||^2_2 + ||r||^2_2 + ||t||^2_2 - ||2(h^\intercal t+r^\intercal (t-h))
$$
Where, 
- $||h||^2_2=||t||^2_2=1$

The model has lesser parameters compared to [Neural Tensor Models](https://papers.nips.cc/paper/5028-reasoning-with-neural-tensor-networks-for-knowledge-base-completion.pdf).

![](https://i.imgur.com/eBbKAAc.png)

**Hyperparameters**:
- $k$ is the embedding size
- Optimizer: SGD

| | Wordnet | FB15k | FB1M |
| - | - | - | - |
| $k$ | 20 | 50 | 50 |
| lr | 0.01 | 0.01 | 0.01 |
| $\gamma$ | 2 | 1 | 1 |
| $d()$ | $L_1$ | $L_1$ | $L_2$ |
| Epochs | 1000(max) | 1000(max) | 1000(max) | 

![](https://i.imgur.com/3y95eBR.png)
**Training Procedure**
1. Normalize relationship and entity vectors
2. Sample positive triplets $p$ and sample negative triplets $n$ for each triplet
3. Calculate loss and update gradient

#### Evaluation
Evaluated on link prediction and predicting new relationships.

![](https://i.imgur.com/x3CoB2J.png)

**TL;DR:**
- Sum of head vector $h$ and relation vector $r$ should be as close as possible to tail vector $t$
  - $h + r \approx t$, where $t$ is the nearest neighbor of $h + r$
- Loss function: Max-margin with negative sampling
  - $L(h,r,t) = max(0, d_{pos} - d_{neg} + margin)$
  - $d = || h + r - t ||$
- Only practical for one-to-one relationships

**Objective Function**: $|| h + r - t ||^2_{l_{1/2}} \quad r \in R^k$

Reference: 
- [Pierre-Yves Vandenbussche's Website](http://pyvandenbussche.info/2017/translating-embeddings-transe/)
- [How to use TransE effectively](http://www.ccri.com/2018/06/27/use-transe-effectively/)
- [Raúl Gómez on Ranking Loss](https://gombru.github.io/2019/04/03/ranking_loss/)

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