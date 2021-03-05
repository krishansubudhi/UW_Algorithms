\documentclass{homeworg}

\title{CSEP 521, Winter 2021: Homework 8}
\author{Krishan Subudhi (ksubudhi@uw.edu) - 2040900}
\usepackage[table]{xcolor}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{pythonhighlight}
\usepackage{enumitem}
\usepackage{array}

\usepackage{graphicx}
\graphicspath{ {./images/} }
\usepackage{placeins}

\let\Oldsubsection\subsection
\renewcommand{\subsection}{\FloatBarrier\Oldsubsection}
\newcommand\numberthis{\addtocounter{equation}{1}\tag{\theequation}}

\begin{document}

\maketitle

\exercise
\emph{Q: Is the $L^{1/2}$ norm a proper distance function (a metric)? Prove or disprove.}

\begin{equation}
\label{eq:1}
    ||(x, y)||_{1/2} =  (\sqrt{|x|}+\sqrt{|y|})^2
\end{equation}

The properties of a proper distance function are:
\begin{align*}
1. d(x,y) &= 0 iff x = y\\
2. d(x,y) &= d(y,x) \\
3. d(x,y) &\le d(x,z) + d(z,y)\\ 
4. d(x,y) &\ge 0
\end{align*}
$L^{1/2}$  does not always satisfy property 3 for all combination of $x$ and $y$. Hence it is not a proper distance function.

Let's take one example in 2d.
\begin{align*}
x = (0,1)\\
y = (1,0)\\
z = (0,0)\\
d(x,y) = (1+1)^2 = 4\\
d(x,z) = (0+1)^2 = 1\\
d(y,z) = (1+0)^2 = 1\\
\\
d(x,z) +d(y,z)  = 2\\
d(x,y) > d(x,z) + d(z,y)
\end{align*}
    
Since for the above example, the property $d(x,y) \le d(x,z) + d(z,y)$ does not hold true, $L^{1/2}$ norm is not a proper distance function.

\newpage
\exercise

\emph{Q. Suppose that $|U| = n$ and you select random subsets, $A \subseteq U$ and $B \subseteq U$ with $|A| = m$ and $|B| = m$. What is the expected size of $A \cap B$?}

Let $X_i$ be an indicator random variable with values
$$
X_i=\begin{cases}
			1, & \text{if $i^{th}$ element is present in both A and B}\\
            0, & \text{otherwise}
		 \end{cases}
$$
\begin{align*}
E[|A \cap B|] &= E[\sum_{i=1}^n{X_i}]\\
&=\sum_{i=1}^n{E[X_i]}\\
&= n \ast E[X_i]\\
&= n \ast P(X_i =1)\\
&= n \ast P(i \ in \ A) \ast P(i \ in \ B)\\
&= n \ast m/n \ast m/n\\
&= \frac{m^2}{n}
\end{align*}

\emph{Q: Give an expression for the value of the Jaccard similarity of A and B if $m = n/k$}
$$
J(A,B) = \frac{|A \cap B|}{|A \cup B|}
$$
if $m = n/k$, 
\begin{align*}
    E[|A \cap B|] &=  \frac{m^2}{n} = \frac{n}{k^2}\\
    E[|A \cup B|] &=  E[|A| + |B| - |A \cap B|]\\
    & = \frac{2n}{k} - \frac{n}{k^2}\\
    & = \frac{n}{k^2} (2k- 1)\\
    J(A,B) &= \frac{|A \cap B|}{|A \cup B|}\\
    &=\frac{1}{2k-1}
\end{align*}

Hence $J \alpha \frac{1}{k}$. This means that for uncorrelated data, as $k$ decreases (i.e. subset size increases), Jaccard similarity increases.

\newpage
\exercise
\newpage
\exercise
Here I downloaded the data and used python collections.Counters to store the BOW data in sparse format. During similarity calculation between X and Y, a union of the sparse dimensions are done. dimensions not present in the original sparse representations will have value 0 when accessed.

Each wordId is a dimension here and count is the value for that dimension. 

Similarity heatmap is prepared by calculating the similarity of all documents of group A with all documents of group B and averaging them.
\subsection{b) Similarity Heatmap}
\begin{figure}[!htbp]
    \centering
    \includegraphics{images/avg_similarity_jaccard.png}
    \caption{Jaccard similarity heatmap}
    \label{fig:hm_jaccard}
\end{figure}

\begin{figure}[!htbp]
    \centering
    \includegraphics{images/avg_similarity_cosine.png}
    \caption{Cosine similarity heatmap}
    \label{fig:hm_cosine}
\end{figure}

\begin{figure}[!htbp]
    \centering
    \includegraphics{images/avg_similarity_l2.png}
    \caption{L2 similarity heatmap}
    \label{fig:hm_l2}
\end{figure}
\newpage
\emph{Q. which of the measures seems the most reasonable? }

The cosine and jaccard similarity seem reasonable compared to L2. Consine similarity seems to be the best since it is somewhat independent of document length and more dependent on the distribution.

\emph{Q.Are there any pairs of newsgroups that are very similar? }
As per both Jaccard similarity and cosine similarity, talk religion.misc and soc.religion.christian seem to be very similar. Overall, the groups have mostly similar documents within themselves.

\emph{Q.Would have you expected this?}
I would have expected to to see more similarity between groups starting with comp.
I was also expecting the rec groups to have more similarity too. Overally the talk groups are more similar probably because of the limited vocabulary used in spoken english. But it's just a guess. More analysis is required. misc.forsale is dissimilar with almost every group. This means the documents that belong to this group have completely different distribution.

\subsection{Nearest-Neighbour heatmap}

The nearest-neighbour heatmap is constructed by calculating the number of nearest neighbours found for all documents in groups other then their own. Jaccard similarity was used as the metric.

\begin{figure}[!htbp]
    \centering
    \includegraphics{images/nn_heatmap.png}
    \caption{Nearest-Neighbour heatmap}
    \label{fig:nn_jaccard}
\end{figure}

\emph{Q.Your plot for part (b) was symmetric, but for part (d) was asymmetric. Explain.}

if docA is most similar to docB that does not mean docB is also most similar to docA

example:

doc A: I am Krishan

doc B: I am going to school today with Krishan.

doc C: I will be going to school today.

\emph{Which groups seem similar? Compare the plots from parts (b) and (d). Which method seems more suited to comparing newsgroups?}

alt.atheism is similar to talk.religion.misc and talk.religion.misc.
Also computer hardware groups are more similar with each other. hockey and baseball groups are similar to each other.

While average similarity gives a smoothed heatmap, the differences are hard to distinguish. Nearest neighbour looks like a discrete heatmap but helps in better comparison.

\end{document}