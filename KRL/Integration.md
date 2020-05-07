# Knowledge Integration Papers


## Language Model (RNN) Integration
### Neural Knowledge Language Model
> Sungjin Ahn, Heeyoul Choi, Tanel Pärnamaa, Yoshua Bengio (~~ICLR 2017~~/Rejected)  
> Affiliation: Universite de Montreal  
> Paper: [Link](https://openreview.net/forum?id=BJwFrvOeg)  

### Knowledge-Augmented Language Model
> Angli Liu, Jingfei Du, Veselin Stoyanov (NAACL 2019)  
> Affiliates: Facebook  
> Paper: [Link](https://arxiv.org/abs/1904.04458)  


### Knowledge Graph Language Model
> Robert Logan, Nelson F. Liu, Matthew E. Peters, Matt Gardner, Sameer Singh (ACL 2019)  
> Paper: [Link](https://www.aclweb.org/anthology/P19-1598/)  
> Code: [GitHub](https://github.com/rloganiv/kglm-model)  
> Dataset: [Link](https://rloganiv.github.io/linked-wikitext-2)  

## BERT (Transformer) Integrations
### ERNIE (THU)
> Zhengyan Zhang, Xu Han, Zhiyuan Liu, Xin Jiang, Maosong Sun, Qun Liu (ACL 2019)
> Affiliation: Tsinghua University, Huawei Noah's Ark
> Paper: [Link](https://arxiv.org/abs/1905.07129)
> Code: [GitHub](https://github.com/thunlp/ERNIE)

#### Introduction
Pre-trained language models have been acheiving promising results in recent years, they neglect to incorporate knowledge information for language understanding.

In order to integrate knowledge graphs into word representations, there are **two** challenges: 

1) Structured Knowledge Encodings: How to extract and encode related informative facts. 
    - Named Entity Recognition using TAGME
2) Heterogeneous Information Fusion: How to fuse the knowledge encodings into the word representations.

#### Methodology
![](https://i.imgur.com/McUS2Zf.png)

***Model Architecture***
Consists of a textual encoder (*T-ENCODER*) identical to BERT and a knowledge (*K-ENCODER*). After encoding basic lexical and syntactic information from T-Encoder, the tokens are the used as the token input, along with pre-trained embeddings of TransE as entity input for the K-Encoder.

The token input and entity input first performs self-attention separately and transformed into the same dimension. The entity embeddings are then aligned and concatenated to the first token of the entity mentioned $f(w_i)=e_j$.

After aligning the entities, the knowledge embeddings are then fused into the token embeddings via the equation below:

$$
\mathbf{h}_i = \sigma(\mathbf{W}_{1,1}^{(l)} \tilde{\mathbf{w}}_i^{(l)} + \mathbf{W}_{1,2}^{(l)} \tilde{e}_j^{(l)} + \mathbf{b}_1^{(l)})
$$

Tokens that are not aligned perform the operation below:

$$
\mathbf{h}_i &= \sigma(\mathbf{W}_{1,1}^{(l)} \tilde{\mathbf{w}}_i^{(l)} + \mathbf{b}_1^{(l)})
$$

And finally passes through a linear transformation as the output:

$$
\mathbf{w}_i^{(l)} &= \sigma(\mathbf{W}_2^{(l)} \mathbf{h}_i + \mathbf{b}_2^{(l)}) \\
 \mathbf{e}_j^{(l)} = \sigma(\mathbf{W}_3^{(l)} \mathbf{h}_i + \mathbf{b}_3^{(l)})
$$

***Objective function***
The objective function of ERNIE is very similar to BERT (NSP + MLM), with the addition of the Denoising Entity Autoencoder. The main objective of dEA is to predict appropriate entities to complete the alignments. In simple words, it is just an entity level MLM (see SpanBERT).

### KnowBERT
> Matthew E. Peters, Mark Neumann, Robert L. Logan IV, Roy Schwartz, Vidur Joshi, Sameer Singh, Noah A. Smith (EMNLP 2019)
> Affiliation: AllenAI
> Paper: [Link](https://arxiv.org/abs/1909.04164)
> Code: [GitHub](https://github.com/allenai/kb)


### K-BERT
> Weijie Liu, Peng Zhou, Zhe Zhao, Zhiruo Wang, Qi Ju, Haotang Deng and Ping Wang (Sept 2019)
> Affiliation: Peking University & Tencent
> Paper: [Link](https://arxiv.org/abs/1909.07606)
> Code: [GitHub](https://github.com/autoliuweijie/K-BERT)


### BERT-MK
> Bin He, Di Zhou, Jinghui Xiao, Xin jiang, Qun Liu, Nicholas Jing Yuan, Tong Xu (Nov 2019)
> Affiliation: Huawei Noah's Ark Lab
> Paper: [Link](https://arxiv.org/abs/1912.00147)
> Code: [None](#)



