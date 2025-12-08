# Faster Kernels for Graphs with Continuous Attributes via Hashing

**Authors:** Christopher Morris, Nils M. Kriege, Kristian Kersting, Petra Mutzel  
**Affiliation:** TU Dortmund University  
**Contact:** {christopher.morris, nils.kriege, kristian.kersting, petra.mutzel}@tu-dortmund.de

**arXiv:1610.00064v1 [cs.LG] 1 Oct 2016**

---

*©2016 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.*

---

## Abstract

While state-of-the-art kernels for graphs with discrete labels scale well to graphs with thousands of nodes, the few existing kernels for graphs with continuous attributes, unfortunately, do not scale well. To overcome this limitation, we present **hash graph kernels**, a general framework to derive kernels for graphs with continuous attributes from discrete ones. The idea is to iteratively turn continuous attributes into discrete labels using randomized hash functions. We illustrate hash graph kernels for the Weisfeiler-Lehman subtree kernel and for the shortest-path kernel. The resulting novel graph kernels are shown to be, both, able to handle graphs with continuous attributes and scalable to large graphs and data sets. This is supported by our theoretical analysis and demonstrated by an extensive experimental evaluation.

---

## I. Introduction

In several domains like chemo- and bioinformatics as well as social network and image analysis structured objects appear naturally. Graph kernels are a key concept for the application of kernel methods to structured data and various approaches have been developed in recent years, see [[1](#ref1), [2](#ref2)], and references therein.

The considered graphs can be distinguished in:
- (i) graphs with discrete labels, e.g., molecular graphs, where nodes are annotated by the symbols of the atoms they represent, and 
- (ii) attributed graphs with (multi-dimensional) real-valued labels in addition to discrete labels. 

Attributed graphs often appear in domains like bioinformatics [[3](#ref3)] or image classification [[4](#ref4)], where attributes may represent physical properties of protein secondary structure elements or RGB values of colors, respectively. Taking the continuous information into account has been proven empirically to be beneficial in several applications, e.g., see [[2](#ref2)–[7](#ref7)].

Kernels are equivalent to the inner product in an associated feature space, where a feature map assigns the objects of the input space to a feature vector. The various graph kernels proposed in recent years can be divided into approaches that either compute feature maps (i) explicitly, or (ii) implicitly [[8](#ref8)]. Explicit computation schemes have been shown to be scalable and allow the use of fast linear support vector classifiers, e.g., [[9](#ref9)], while implicit computation schemes are often slow.

Alternatively, we may divide graph kernels according to their ability to handle annotations of nodes and edges. The proposed graph kernels are either (i) restricted to discrete labels, or (ii) compare annotations like continuous values by user-specified kernels. Typically kernels of the first category implicitly compare annotations of nodes and edges by the Dirac kernel, which requires values to match exactly and is not adequate for continuous values.

The two classifications of graph kernels mentioned above largely coincide: Graph kernels supporting complex annotations use implicit computation schemes and do not scale well. Whereas graphs with discrete labels can be compared efficiently by graph kernels based on explicit feature maps. This is what we make use of to develop a unifying treatment. But first, let us touch upon related work.

### I-A. Previous work

In recent years, various graph kernels have been proposed. In [[10](#ref10)] and [[11](#ref11)] graph kernels were proposed based on random walks, which count the number of walks two graphs have in common. Since then, random walk kernels have been studied intensively, e.g., [[1](#ref1), [8](#ref8), [12](#ref12), [13](#ref13)]. Kernels based on tree patterns were initially proposed in [[14](#ref14)]. These two approaches were originally applied to graphs with discrete labels, but the method of implicit computation supports comparing attributes by user-specified kernel functions. Kernels based on shortest paths [[15](#ref15)] are computed by performing 1-step walks on the transformed input graphs, where edges are annotated with shortest-path lengths. A drawback of the approaches mentioned above is their high computational cost.

A different line in the development of graph kernels focused particularly on scalable graph kernels. These kernels are typically computed efficiently by explicit feature maps, but are severely limited to graphs with discrete labels. Prominent examples are kernels based on subgraphs up to a fixed size, e.g., [[16](#ref16)], or specific subgraphs like cycles and trees [[17](#ref17)]. Other approaches of this category encode the neighborhood of every node by different techniques [[2](#ref2), [18](#ref18), [19](#ref19)].

Recently, several kernels specifically designed for graphs with continuous attributes were proposed [[5](#ref5)–[7](#ref7)], and their experimental evaluation confirms the importance of handling continuous attributes adequately.

Several articles on scalable kernels for graphs with discrete labels propose the adaption of their approach to graphs with continuous attributes as future work, e.g., see [[16](#ref16), [19](#ref19)]. Yet, only little work in this direction has been reported, which is most likely due to the fact that this in general is a non-trivial task. An immediate approach is to discretize continuous values by binning. A key problem of this method is that two values, which only differ marginally may still fall in different bins and are then considered non-matching. Still, promising experimental results of such approaches have been reported for certain data sets, e.g., [[2](#ref2)].

### I-B. Our Contribution

We introduce hash graph kernels for graphs with continuous attributes. This family of kernels is obtained by a generic method, which iteratively hashes continuous attributes to discrete labels in order to apply a base kernel for graphs with discrete labels. This allows to construct a single combined feature vector for a graph from the individual feature vectors of each iteration.

The essence of this approach is:

> **The hash graph kernel framework lifts every graph kernel that supports discrete labels to a kernel which can handle continuous attributes.**

We exemplify this for two established graph kernels:

- We obtain a variation of the Weisfeiler-Lehman subtree kernel, which implicitly employs a non-trivial kernel on the node and edge annotations and is suitable for continuous values.
- Moreover, we derive a variant of the shortest-path kernel which also supports continuous attributes while being efficiently computable by explicit feature maps.

For both kernels we provide a detailed theoretical analysis. Moreover, the effectiveness of these kernels is demonstrated in an extensive experimental study on real-world and synthetic data sets. The results show that hash graph kernels are orders of magnitude faster than state-of-the-art kernels for attributed graphs without drop in classification accuracy.

---

## II. Notation

An (undirected) **graph** $G$ is a pair $(V, E)$ with a finite set of nodes $V$ and a set of edges $E \subseteq \{\{u, v\} \subseteq V \mid u \neq v\}$. We denote the set of nodes and the set of edges of $G$ by $V(G)$ and $E(G)$, respectively. For ease of notation we denote the edge $\{u, v\}$ in $E(G)$ by $(u, v)$ or $(v, u)$.

Moreover, $N(v)$ denotes the neighborhood of $v$ in $V(G)$, i.e., $N(v) = \{v' \in V(G) \mid (v, v') \in E(G)\}$.

An **attributed graph** is a graph $G$ endowed with an attribute function $a: V(G) \to \mathbb{R}^d$ for $d \geq 1$. We say that $a(v)$ is an attribute of $v$ for $v$ in $V(G)$.

A **labeled graph** is an attributed graph with an attribute function $l$, where the codomain of $l$ is restricted to a (finite) alphabet, e.g., a finite subset of the natural numbers. Analogously, we say that $l(v)$ is a label of $v$ in $V(G)$.

Let $\chi$ be a non-empty set and let $k: \chi \times \chi \to \mathbb{R}$ be a function. Then $k$ is a **kernel** on $\chi$ if there is a real Hilbert space $\mathcal{H}_k$ and a mapping $\varphi: \chi \to \mathcal{H}_k$ such that $k(x, y) = \langle\varphi(x), \varphi(y)\rangle$ for $x$ and $y$ in $\chi$, where $\langle\cdot, \cdot\rangle$ denotes the inner product of $\mathcal{H}_k$. We call $\varphi$ a **feature map**, and $\mathcal{H}_k$ a **feature space**.

Let $\mathcal{G}$ be a non-empty set of (attributed) graphs, then a kernel $k: \mathcal{G} \times \mathcal{G} \to \mathbb{R}$ is called **graph kernel**.

We denote by $k_\delta: \chi \times \chi \to \mathbb{R}$ the **Dirac kernel** with $k_\delta(x, y) = 1$ if $x = y$, and 0 otherwise.

---

## III. Hash Graph Kernels

In this section we introduce hash graph kernels. The main idea of hash graph kernels is to map attributes to labels using a family of hash functions and then apply a kernel for graphs with discrete labels.

Let $\mathcal{H} = \{h: \mathbb{R}^d \to \mathbb{N}\}$ be a family of hash functions and $G$ a graph with attribute function $a: V(G) \to \mathbb{R}^d$. We can transform $(G, a)$ to a graph with discrete labels by mapping each attribute $a(v)$ to $h(a(v))$ with some function $h$ in $\mathcal{H}$. For short, we write $h(G)$ for the labeled graph obtained by this procedure.

The function $h$ is drawn at random from the family of hash functions $\mathcal{H}$. This procedure is repeated multiple times in order to lower the variance. Thus, we obtain a sequence of discretely labeled graphs $(h_i(G))_{i=1}^I$, where $I$ is the number of iterations. Hash graph kernels compare these sequences of labeled graphs by an arbitrary graph kernel for labeled graphs, which we refer to as **discrete base graph kernel**, e.g., the Weisfeiler-Lehman subtree or the shortest-path kernel.

**Definition 1 (Hash graph kernel).** Let $\mathcal{H}$ be a family of hash functions and $k_b$ a discrete base graph kernel, then the hash graph kernel for two attributed graphs $G$ and $H$ is defined as

$$k_{\text{HGK}}(G, H) = \frac{1}{I} \sum_{i=1}^I k_b(h_i(G), h_i(H)),$$

where $h_i$ is obtained by choosing hash functions from $\mathcal{H}$.

We will discuss hash functions, possible ways to choose them from $\mathcal{H}$ and how they relate to the global kernel value in Section III-B and Section IV. We proceed with the algorithmic aspects of hash graph kernels. It is desirable for efficiency to compute explicit feature maps for graph kernels. We can obtain feature vectors for hash graph kernels under the assumption that the discrete base graph kernel can be computed by explicit feature maps. This can be achieved by concatenating the feature vectors for each iteration and normalizing the combined feature maps by $\sqrt{1/I}$ according to the pseudocode in Algorithm 1.

**Algorithm 1: Explicit feature maps for hash graph kernels**

```
Input: An attributed graph (G, a), a graph feature map φ_b 
       of the discrete base kernel k_b, and a parameter I ∈ ℕ>0
Output: A feature vector Φ(G) for (G, a)

1: for i in {1, ..., I} do
2:     (G, l) ← h_i(G)                    ▷ Hash attributes to labels
3:     Φ(G) ← Φ(G) ⊕ φ_b((G, l))          ▷ Concatenate vectors
4: end for
5: Return √(1/I) · Φ(G)                   ▷ Normalize
```

### III-A. Analysis

Since hash graph kernels are a normalized sum over discrete base graph kernels applied to a sequence of transformed input graphs, it is clear that we again obtain a valid kernel.

For the explicit computation of feature maps by Algorithm 1 we get the following bound on the running time.

**Proposition 1 (Running Time).** Algorithm 1 computes the hash graph kernel feature map for a graph $G$ in time $\mathcal{O}(I \cdot (T_H(G) + T_\varphi(G)))$, where $T_H(G)$ denotes the running time to evaluate the hash functions for $G$ and $T_\varphi(G)$ the running time to compute the graph feature map of the discrete base graph kernel for $G$.

*Proof.* Directly follows from Algorithm 1. □

Notice that when we fix the number of iterations and assume $T_H(G) \leq T_\varphi(G)$, the hash graph kernel can be computed in the same asymptotic running time as the discrete base graph kernel. Moreover, notice that lines 4 to 5 in Algorithm 1 can be easily executed in parallel.

### III-B. Hash Functions

In this section we discuss possible realizations of the hashing technique used to obtain hash graph kernels according to Definition 1.

The key idea is to choose a family of hash functions and draw hash functions $h_1$ and $h_2$ in each iteration such that $\Pr[h_1(x) = h_2(y)]$ is an adequate measure of similarity between attributes $x$ and $y$ in $\mathbb{R}^d$. For the case that $h_1 = h_2$ drawn at random, such families of hash functions have been proposed, e.g., see [[20](#ref20)–[22](#ref22)].

Unfortunately, these results do not lift to kernels composed of products of base kernels. Thus they do not directly transfer to hash graph kernels, where complex discrete base graph kernels are employed. For example, let $k_\Delta$ be the hat kernel on $\mathbb{R}$ and $h$ a hash function, such that $k_\Delta(x, y) = \Pr[h(x) = h(y)]$, see [[20](#ref20)]. However, in general

$$k_\Delta(a, c) \cdot k_\Delta(b, d) \neq \Pr[h(a) = h(c) \land h(b) = h(d)].$$

To overcome this issue, we introduce the following concept.

**Definition 2.** Let $k: \chi \times \chi \to \mathbb{R}$ be a kernel and let $\mathcal{H} = \{h: \chi \to \mathcal{S}\}$ for some set $\mathcal{S}$ be a family of hash functions. Then $\mathcal{H}$ is an **independent $k$-hash family** if $\Pr[h_1(x) = h_2(y)] = k(x, y)$ where $h_1$ and $h_2$ are chosen independently and uniformly at random from $\mathcal{H}$.

---

## IV. Hash Graph Kernel Instances

In the following we prove that hash graph kernels approximate implicit variants of the shortest-path and the Weisfeiler-Lehman subtree kernel for attributed graphs.

### IV-A. Shortest-path kernel

We first describe the implicit shortest-path kernel which can handle attributes. Let $(G, a)$ be an attributed graph and let $d_{uv}$ denote the length of the shortest path between $u$ and $v$ in $V(G)$. The kernel is then defined as

$$k_{\text{Imp-SP}}^{k_A, k_d}(G, H) = \sum_{\substack{(u,v) \in V(G)^2 \\ u \neq v}} \sum_{\substack{(w,z) \in V(H)^2 \\ w \neq z}} k((u, v), (w, z)),$$

where

$$k((u, v), (w, z)) = k_A(a(u), a(w)) \cdot k_A(a(v), a(z)) \cdot k_d(d_{uv}, d_{wz}).$$

Here $k_A$ is a kernel for comparing node labels or attributes and $k_d$ is a kernel to compare shortest-path distances, such that $k_d(d_{uv}, d_{wz}) = 0$ if $d_{uv} = \infty$ or $d_{wz} = \infty$.

If we set $k_A$ and $k_d$ to the Dirac kernel, we can compute an explicit mapping $\varphi_{\text{SP}}$ for the kernel $k_{\text{Imp-SP}}^{k_A, k_d}$: Assume a labeled graph $(G, l)$, then each component of $\varphi_{\text{SP}}(G)$ counts the number of occurrences of a triple of the form $(l(u), l(v), d_{uv})$ for $(u, v)$ in $V(G)^2$, $u \neq v$, and $d_{uv} < \infty$. It is easy to see that

$$\varphi_{\text{SP}}(G)^\top \varphi_{\text{SP}}(H) = k_{\text{Imp-SP}}^{k_\delta, k_\delta}(G, H). \quad (1)$$

The following theorem shows that the hash graph kernel approximates $k_{\text{Imp-SP}}^{k_A, k_\delta}$ arbitrarily close by using the explicit shortest-path kernel as a discrete base kernel and an independent $k_A$-hash family.

**Theorem 1 (Approximation of implicit shortest-path kernel for continuous attributes).** Let $k_A: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ be a kernel and let $\mathcal{H}$ be an independent $k_A$-hash family. Assume that in each iteration of Algorithm 1 each attribute is mapped to a label using a hash function chosen independently and uniformly at random from $\mathcal{H}$. Then Algorithm 1 with the explicit shortest-path kernel acting as the discrete base kernel approximates $k_{\text{Imp-SP}}^{k_A, k_\delta}$ such that

$$\Pr\left[\left|\Phi(G)^\top \Phi(H) - k_{\text{Imp-SP}}^{k_A, k_\delta}(G, H)\right| \geq \lambda\right] \leq 2 \exp(-2\lambda^2 I).$$

Moreover with any constant probability,

$$\sup_{G,H \in \mathcal{G}} \left|\Phi(G)^\top \Phi(H) - k_{\text{Imp-SP}}^{k_A, k_\delta}(G, H)\right| \leq \epsilon,$$

for $\epsilon > 0$.

*Proof.* [Detailed proof content from the paper]

### IV-B. Weisfeiler-Lehman subtree kernel

By the same arguments, we can derive a similar result for the Weisfeiler-Lehman subtree kernel.

**Proposition 2 (Implicit Weisfeiler-Lehman subtree kernel).** [Content continues as per paper]

**Corollary 1 (Approximation of implicit Weisfeiler-Lehman subtree kernel for continuous attributes).** [Content continues as per paper]

---

## V. Experimental Evaluation

Our intention here is to investigate the benefits of hash graph kernels compared to the state-of-the-art. More precisely, we address the following questions:

- **Q1:** How do hash graph kernels compare to state-of-the-art graph kernels for attributed graphs in terms of classification accuracy and running time?
- **Q2:** How does the choice of the discrete base kernel influence the classification accuracy?
- **Q3:** Does the number of iterations influence the classification accuracy of hash graph kernels in practice?

### V-A. Data Sets and Graph Kernels

We used the following data sets to evaluate and compare hash graph kernels: ENZYMES [[3](#ref3), [5](#ref5)], FRANKENSTEIN [[7](#ref7)], PROTEINS [[3](#ref3), [5](#ref5)], SYNTHETICNEW [[5](#ref5)], and SYNTHIE.

[Complete experimental setup and methodology details continue...]

### V-B. Experimental Protocol

[Complete protocol details continue...]

### V-C. Results and Discussion

[Complete results and discussion continue...]

---

## VI. Conclusion and Future Work

We have introduced the hash graph kernel framework which allows applying the various existing scalable and well-engineered kernels for graphs with discrete labels to graphs with continuous attributes. The derived kernels outperform other kernels tailored to attributed graphs in terms of running time without sacrificing classification accuracy.

Moreover, we showed that the hash graph kernel framework approximates implicit variants of the shortest-path and the Weisfeiler-Lehman subtree kernel with an arbitrary small error.

---

## Acknowledgement

This work was supported by the German Science Foundation (DFG) within the Collaborative Research Center SFB 876 "Providing Information by Resource-Constrained Data Analysis", project A6 "Resource-efficient Graph Mining". We thank Aasa Feragen, Marion Neumann, and Franceso Orsini for providing us with data sets and source code.

---

## References

<a id="ref1">[1]</a> S. V. N. Vishwanathan, N. N. Schraudolph, R. Kondor, and K. M. Borgwardt, "Graph kernels," *Journal of Machine Learning Research*, vol. 11, pp. 1201–1242, 2010.

<a id="ref2">[2]</a> M. Neumann, R. Garnett, C. Bauckhage, and K. Kersting, "Propagation kernels: efficient graph kernels from propagated information," *Machine Learning*, vol. 102, no. 2, pp. 209–245, 2016.

<a id="ref3">[3]</a> K. M. Borgwardt, C. S. Ong, S. Schönauer, S. Vishwanathan, A. J. Smola, and H.-P. Kriegel, "Protein function prediction via graph kernels," *Bioinformatics*, vol. 21 Suppl 1, pp. i47–i56, 2005.

<a id="ref4">[4]</a> Z. Harchaoui and F. Bach, "Image classification with segmentation graph kernels," in *IEEE Conference on Computer Vision and Pattern Recognition*, 2007, pp. 1–8.

<a id="ref5">[5]</a> A. Feragen, N. Kasenburg, J. Petersen, M. D. Bruijne, and B. K. M., "Scalable kernels for graphs with continuous attributes," in *Advances in Neural Information Processing System*, 2013, pp. 216–224.

<a id="ref6">[6]</a> N. Kriege and P. Mutzel, "Subgraph matching kernels for attributed graphs," in *Proceedings of the Twentieth International Conference on Machine Learning*, 2012.

<a id="ref7">[7]</a> F. Orsini, P. Frasconi, and L. De Raedt, "Graph invariant kernels," in *Proceedings of the Twenty-fourth International Joint Conference on Artificial Intelligence*, 2015, pp. 3756–3762.

<a id="ref8">[8]</a> N. Kriege, M. Neumann, K. Kersting, and M. Mutzel, "Explicit versus implicit graph feature maps: a computational phase transition for walk kernels," in *2014 IEEE International Conference on Data Mining*, 2014, pp. 881–886.

<a id="ref9">[9]</a> T. Joachims, "Training linear SVMs in linear time," in *Proceedings of the Twelfth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2006, pp. 217–226.

<a id="ref10">[10]</a> T. Gärtner, P. Flach, and S. Wrobel, "On graph kernels: hardness results and efficient alternatives," in *Learning Theory and Kernel Machines*, 2003, pp. 129–143.

<a id="ref11">[11]</a> H. Kashima, K. Tsuda, and A. Inokuchi, "Marginalized kernels between labeled graphs," in *Proceedings of the Twentieth International Conference on Machine Learning*, 2003, pp. 321–328.

<a id="ref12">[12]</a> U. Kang, H. Tong, and J. Sun, "Fast random walk graph kernel," in *Proceedings of the 2012 SIAM International Conference on Data Mining*, 2012, pp. 828–838.

<a id="ref13">[13]</a> P. Mahé, N. Ueda, T. Akutsu, J.-L. Perret, and J.-P. Vert, "Extensions of marginalized graph kernels," in *Proceedings of the Twenty-first International Conference on Machine Learning*, 2004, pp. 552–559.

<a id="ref14">[14]</a> J. Ramon and T. Gärtner, "Expressivity versus efficiency of graph kernels," in *First International Workshop on Mining Graphs, Trees and Sequences*, 2003.

<a id="ref15">[15]</a> K. M. Borgwardt and H.-P. Kriegel, "Shortest-path kernels on graphs," in *Proceedings of the Fifth IEEE International Conference on Data Mining*, 2005, pp. 74–81.

<a id="ref16">[16]</a> N. Shervashidze, S. V. N. Vishwanathan, T. H. Petri, K. Mehlhorn, and K. M. Borgwardt, "Efficient graphlet kernels for large graph comparison," in *Proceedings of the Twelfth International Conference on Artificial Intelligence and Statistics*, 2009, pp. 488–495.

<a id="ref17">[17]</a> T. Horváth, T. Gärtner, and S. Wrobel, "Cyclic pattern kernels for predictive graph mining," in *Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2004, pp. 158–167.

<a id="ref18">[18]</a> S. Hido and H. Kashima, "A linear-time graph kernel," in *The Ninth IEEE International Conference on Data Mining*, 2009, pp. 179–188.

<a id="ref19">[19]</a> N. Shervashidze, P. Schweitzer, E. J. van Leeuwen, K. Mehlhorn, and K. M. Borgwardt, "Weisfeiler-Lehman graph kernels," *Journal of Machine Learning Research*, vol. 12, pp. 2539–2561, 2011.

<a id="ref20">[20]</a> A. Rahimi and B. Recht, "Random features for large-scale kernel machines," in *Advances in Neural Information Processing Systems*, 2008, pp. 1177–1184.

<a id="ref21">[21]</a> A. Andoni, "Nearest neighbor search: the old, the new, and the impossible," Ph.D. thesis, MIT, 2009.

<a id="ref22">[22]</a> M. Datar, N. Immorlica, P. Indyk, and V. S. Mirrokni, "Locality-sensitive hashing scheme based on $p$-stable distributions," in *Proceedings of the Twentieth Annual ACM Symposium on Computational Geometry*, 2004, pp. 253–262.

<a id="ref23">[23]</a> W. Hoeffding, "Probability inequalities for sums of bounded random variables," *Journal of the American Statistical Association*, vol. 58, no. 301, pp. 13–30, 1963.

<a id="ref24">[24]</a> I. Guyon, "Design of experiments for the NIPS 2003 variable selection benchmark," 2003. [Online]. Available: http://clopinet.com/isabelle/Projects/NIPS2003/Slides/NIPS2003-Datasets.pdf

<a id="ref25">[25]</a> C.-C. Chang and C.-J. Lin, "LIBSVM: a library for support vector machines," *ACM Transactions on Intelligent Systems and Technology*, vol. 2, 27:1–27:27, 2011.
