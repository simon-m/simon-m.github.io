Title: Using Facebook's FastText for document classification.
Date: 2017-10-24 18:30
Modified: 2017-10-31 23:00
Category: Machine learning
Tags: NLP, Text classification, Word embedding
Authors: Simon-M
Summary: A short introduction to using FastText for document classification

# Context
I am currently working on classifying some medical data in the form of examination notes,
the goal being to predict whether a patient has a pathology or not.
This text data has a few quirks compared to textbook examples of document classification:

-  Documents (one per patient) are short: less than 30 words on average
-  The text is dirty
   - many words contain typos, resulting in multiple terms refering to the same thing.
   - many abbreviations are used and some are conflicting.
-  Many words, and particularly the relevant ones, are subject-specific jargon and thus cannot be recovered
   using general-purpose spelling correctors.
-  The single binary label "pathology" / "no_pathology" is noisy because it is the result of partial manual
   annotation. More specifically, a subset of the dataset was selected for annotation based on a
   currated list of keywords (and their typo'd variations). The rest was labeled as "no_pathology".
   Moreover, the manual annotation was carried out in a fairly limited time-frame which did not allow
   multiple pass on the same patients by several annotators.
-  The dataset suffers from major class imbalance since only ~1.2% of the patient are part of the "pathology" class.

On the plus side, the dataset is rather large with ~600,000 patients.
On the minus side, I have access to a fairly limited amount of computing power (no GPU, intel i3 with 4 Gb RAM).
Therefore, even though I am fairly attracted to the recent neural networks-based methods (such as recurent neural networks
which seem to enjoy a fair share of success) there is absolutely no way I can run them on my machine. Also, cloud-based
solutions such as Amazon's AWS are out of the question, the main reason for that being that the data should not leave
the lab.


# Facebook's fastText
After trying a bunch of different methods which will be the subject of another article,
I was reading on language models, in particular n-grams and word embeddings/representations
such as word2vec and GloVe, hoping to find new ideas for extracting relevant features from
my documents' text.

Both the n-gram and word representation are interesting in their own right but I have been rather
impressed by the semantic properties of word2vec. However, word embedding methods are called
this way for a reason: the unit are words, which means each word gets vector representation.
I am therefore left with the follwing question: how to meaningfully combine these and get a document
representation?

I then stumbled upon an interesting article:
[Bag of Tricks for Efficient Text Classification](https://arxiv.org/abs/1607.01759).
In short, the approach described by the authors consists in defining word (or n-gram) representation
*à la* word2vec, simply average them to get a sentence representation and feed that to a linear
classifier.

I like this approach for several reasons: it uses the apparently word2vec framework,
it is conceptually simple, it compares favorably to baselines and more sophisticated models,
it is fast and in particular much much faster than the neural network-based models I cannot
afford, and finally, it is already implemented in the
[fastText library](https://github.com/facebookresearch/fastText/).

I therefore decided to try my luck and use fastText's classifier to gauge its ability to
classify my data.

Note that fastText is not limited to classification: it can be used in an unsupervised fashion
to get word and sentence embeddings.


## FastText for Windows
First hurdle: fastText is designed to build under Unix-like systems.
That's a bummer as despite being a long-standing user of Linux systems,
I am stuck with Windows at work.
Fortunately, someone may have felt the same and shared a
[Windows version](http://cs.mcgill.ca/~mxia3/FastText-for-Windows/) of the library.
Thumbs up to you [Meng Xuan Xia](http://cs.mcgill.ca/~mxia3).

After a quick and painless compilation with MS Visual C++ (appreciable considering it was my first time
using it), I am ready to start.


# Getting started
I am mainly giving  short version of the [documentation](https://github.com/facebookresearch/fastText/)
and [tutorials](https://github.com/facebookresearch/fastText/blob/master/tutorials), but it is advisable you
read them too.

The command-line interface (CLI) is very simple to use and the input format is very minimalistic
and convenient (I am looking at you Weka and ARFF).

The training set format is as such:
```
This is an example sentence __label__example
This is one is not (yes it is though) __label__not_example
```
Basically, each sentence/document is written as is on a single line and the labels are
prefixed with \_\_label\_\_ (this can be customized using the -label option on the CLI).
In this case, I simply encode the single binary label as two labels "__label__pathology" and
"__label__no_pathology".

Training a default classifier is dead simple with the "supervised" command.
```
fastText.exe supervised -input training_set.txt -output default_model
```

The performance of the resulting model can then be investigated using the test command
```
fastText.exe test default_model.bin test_file.txt 1;
```
The "1" here is the default value for the number of top label to be used as the prediction.
In the general case, a value of "1" will give as prediction the best label only.
In my case, since I have a single binary label, using "1" is the way to go.
This prints the precision achieved on the test set.

In this case, precision is not a good measure because of the very strong unbalance of the dataset.
Always predicting "no_pathology", one can expect precision and recall to reach ~98.8%.
Such a high baseline makes it difficult to assess whether this classifier is better than the
dummy "always predict no-pathology" strategy.

Fortunately, I can rely on the "predict" command to get predictions and compute the confusion matrix
or any other metric such as Matthews Correlation Coefficient (MCC).
```
fastText.exe predict default_model.bin test_file.txt 1 > predictions.txt;
```

Still, I need a more detailed account of the classifier's performance. Specifically,
I would like to get a maximum of true positives (TP) (don't we all?) while keeping the number of
false positives (FP) close to TP. This has to do with the way the
classifier will be used, namely screening and human validation of the positive predictions.
The goal is to give a reasonable number of screened patients to the validators.
I therefore need to have access to a probability-like number instead of 0 / 1 decisions in order
to vary the "positive" cutoff during subsequent analyses.

For that, I use the "predict-proba" command.
```
fastText.exe predict-proba default_model.bin test_file.txt 1 > class_probabilities.txt;
```

# Parameters
A short description of the parameters is provided in the documentation, but I will
expand a little on the most important ones.

- ---
The "-loss" option allows you to choose the loss which is optimized for.

The default value is "ns" for negative sampling. It is an approximation of the softmax loss
based on sampling "negative examples".

Briefly and very roughly, the goal of word2vec is to find an embedding of words, i.e. a vector
representation for each word in a space of fixed dimension.
Given a *context* i.e. words surrounding a word of interest (e.g. in a fixed size window around it),
a good embedding should satisfy the following:

1. the dot product between the vectors of a word and a context often found together should be large.
2. this dot product must be small for words and contexts which rarely co-occur

Given the vector representation \\(w_i\\) of a word and a context \\(c_j\\), the goal is
therefore to maximize \\(\frac{w_i \\cdot c_j}{\\sum_w(w \\cdot c_j)}\\). The normalization
is a sum over all words which can be prohibitively large and yield very long computation
times.

Remark: this is a simplification to get the idea across; the actual softmax loss is actually
\\(-log P(w_i | c_j) = -log(e^{w_i \\cdot c_j} / \\sum_w(e^{w \\cdot c_i}))\\) which
should be minimized instead of maximized.

An alternative is therefore to replace the sum over all words by  a sum over a random
sample, under the reasonable assumption that most are "negative", i.e. rarely co-occur
with a given context. This resutls in the negative sampling loss. See also this
[stackoverflow post](https://stackoverflow.com/questions/27860652/word2vec-negative-sampling-in-layman-term).


The "softmax" value results in using the regular softmax loss which is much *much* slower.

The "hs" value uses hierarchical softmax. The goal is to organize the set of all words in a tree so that
the sum over all words reduces instrad to a sum over one path in the tree.

Namely, the probability \\(P(w_i | c_j)\\) is computed by first building
a [Huffman tree](https://en.wikipedia.org/wiki/Huffman_coding) with words as leaves,
so that most common words are found at smaller depth.
Each internal node \\(n_i\\) has two children and their associated probabilities \\(p_i\\) and
\\(q_i = 1 - p_i\\) where \\(p_i\\) depends both on the context \\(c_j\\) and a vector which is learned during training.
The probaility \\(P(w_i | c_j)\\) is then computed by following the path from the root to the
\\(w_i\\) and multiplying the \\(p_i\\) or \\(q_i\\) depending on which child is followed.
Since the depth of a balanced tree with \\(n\\) leaves is \\(O(log n)\\), this reduces the computation of
the softmax loss from \\(O(W)\\) to \\(O(log W)\\) for \\(W\\) words. A more detailed explanation with nice
graphics can be found [here](http://building-babylon.net/2017/08/01/hierarchical-softmax/).

For a more rigorous description of negative sampling and hierarchical softmax, see
[this article](https://arxiv.org/abs/1310.4546) and references therein.

In general, "ns" or "hs" are the only way to train the model in reasonable time when the vocabulary size is large.
As a rule of thumb, "ns" requires several epochs to be accurate ("-epoch" flag) whereas "hs" does not benefits from
more epoch([as stated here](https://groups.google.com/forum/#!msg/word2vec-toolkit/WUWad9fL0jU/LdbWy1jQjUIJ)).

- ---

The "-bucket" option is used to tune the number of buckets used in the hash table. There is a
trade-off between accuracy and memory used as a smaller value implies more collisions.

- ---
The "-lr" option tunes the learning rate. In general, a larger value means faster training and a
potentially less accurate model because of a higher risk of getting stuck in local minimum.



# Some results
After a light parameter tuning phase, the best cutoff to balance TP and FP results in
a ~2/3 precision. Interestingly, this is almost the best that can be reached.
Indeed, lowering the threshold further (i.e. predicting more and more patients as "pathology") yields
very marginal changes on the precision, TP and FP until reaching a threshold where everything is predicted
as "pathology". This is because most of the low probabilities are all clustered very closely around the
same value.

All in all, these results are fairly good considering I did not have to engineer any features and spent
little time optimizing the parameters.
The next step is to see whether word2vec features could benefit a classifier when used along LDA
topic mixtures.


# Further thoughts:
I stumbled upon other alternatives in a similar vein:

- [Gensim's Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html) does exactly what it
  says: it computes the embedding of whole documents/sentences which can then be fed to a classifier.
  Note: Gensim also implements word2vec and FastText.
- Using word2vec/FasText, compute a component-wise max or min or average over all word representations
  and use the resulting vector as the sentence embedding. Computing all three min and max and average and
  concatenating them can also be used to get another embedding. Idea from this
  [stackexchange post](https://stats.stackexchange.com/questions/221715/apply-word-embeddings-to-entire-document-to-get-a-feature-vector)
  and [this paper](https://arxiv.org/abs/1607.00570).






#References:
- [https://arxiv.org/abs/1607.01759](https://arxiv.org/abs/1607.01759)
- [https://github.com/facebookresearch/fastText/](https://github.com/facebookresearch/fastText/)
- [https://github.com/facebookresearch/fastText/blob/master/tutorials](https://github.com/facebookresearch/fastText/blob/master/tutorials)
- [https://stackoverflow.com/questions/27860652/word2vec-negative-sampling-in-layman-term](https://stackoverflow.com/questions/27860652/word2vec-negative-sampling-in-layman-term)
- [https://groups.google.com/forum/#!msg/word2vec-toolkit/WUWad9fL0jU/LdbWy1jQjUIJ](https://groups.google.com/forum/#!msg/word2vec-toolkit/WUWad9fL0jU/LdbWy1jQjUIJ)
- [https://arxiv.org/abs/1310.4546](https://arxiv.org/abs/1310.4546)
- [http://building-babylon.net/2017/08/01/hierarchical-softmax/](http://building-babylon.net/2017/08/01/hierarchical-softmax/)
- [https://en.wikipedia.org/wiki/Huffman_coding](https://en.wikipedia.org/wiki/Huffman_coding)
- [https://stats.stackexchange.com/questions/221715/apply-word-embeddings-to-entire-document-to-get-a-feature-vector](https://stats.stackexchange.com/questions/221715/apply-word-embeddings-to-entire-document-to-get-a-feature-vector)
- [https://radimrehurek.com/gensim/models/doc2vec.html](https://radimrehurek.com/gensim/models/doc2vec.html)
- [https://arxiv.org/abs/1607.00570](https://arxiv.org/abs/1607.00570)
