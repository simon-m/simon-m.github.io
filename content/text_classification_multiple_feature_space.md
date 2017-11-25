Title: Classification of text data: using multiple feature spaces
Date: 2017-11-02 21:40
Modified: 2017-11-02 21:40
Category: Machine learning
Tags: NLP, Text classification, Word embedding, Python, Scikit-learn, Sklearn, Gensim
Authors: Simon-M
Summary: How to combine multiple topic-based and word embedding-based methods for text classification with scikit-learn and Gensim.


As mentionned in another [post](using-facebooks-fasttext-for-document-classification.html), I am currently working on a text classification task and experimenting with
several features extraction methods.

# Input features for text classification

## Topic-based
I have started with the regular "topic-based" method such as
[latent semantic indexing/analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (LSI/LSA),
[latent dirichlet allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) (LDA)
and [non-negative matrix factorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization) (NMF).

These methods start with a term-document matrix \\(T\\) with documents as rows and terms as columns.
In the simplest case, the value \\(T_{ij}\\) is simply the absolute frequency (or count) of
term \\(j\\) in document \\(i\\). This value is often replaced by the so-called TF-IDF value (Term Frequency -
Inverse Document Frequency) which basically allows to give more importance to rare terms.
Note that "terms" could be words or n-grams or possibly any other relevant unit of text.

From this matrix, topic-based methods seek to discover latent factors called *topics*, which are linear
combinations of the terms and represent documents as linear combinations of topics.
The expectation is that words found in similar documents will end up in the same topic,
hoping that topics are more releveant than bare words for classification.
Moreover using \\(T\\) directly as input to a classifier would result in on feature per word which can
lead to a prohibitively large number of features. Topic extraction can therefore be seen as
a dimensionality reduction step.

In practice LSI uses singular value decomposition (SVD) decomposition on \\(T\\),
LDA is a probabilistic model over topics and documents, and NMF, well, relies on the
non-negative matrix factorization of \\(T\\).


## Word embedding-based
Although these approaches are standard in text analysis, I was curious about the newer so-called *word embedding*
methods such as [Facebook's FastText](Bag of Tricks for Efficient Text Classification). These follow a rather
orthogonal approach to topic-based methods as they
seek to find a vector representation of *words* so that semantically similar words are represented by similar vectors
(according to a given metric).
To reach this goal, the broad idea is to find an embedding allowing to predict which word should occur given its *context*
(for the continuous bag of words representation, the skip-gram representation swaps words and contexts).
Here context mean "surroundings words", i.e. words found in a windows around the word of interest.
Note that I use "word" instead of "terms", but this can also be applied to n-grams as a unit.

As opposed to topic-based methods, word-embedding methods consider a more local context:
for the former, similar terms are those appearing in similar documents, for the latter,
similar terms appear in similar contexts *within* a document.


## The best of both worlds?
The two approaches seeming quite complementary so I thought may give a shot to
combining their resulting features. I settled to use NMF and a FastText-based
document embedding.


# In practice: document FastText

Document embedding methods results in vectors for *terms* but not for documents.
Therefore I used a fairly simple method to get document-vectors from terms-vectors: simply
concatenate the element-wise min, max and mean of all words in the document. For a
term-embedding of size \\(k\\), this results in a document-embedding of size \\(3k\\).
This original idea was described [here](https://arxiv.org/abs/1607.00570) and gave simingly good
results for short documents.

The code using Gensim's FastText:

```python
from sklearn.base import BaseEstimator
from gensim.models.fasttext import FastText


class DocumentFastText(BaseEstimator):
    def __init__(self, sentences=None, sg=0, hs=0, size=100, alpha=0.025, window=5, min_count=5,
                 max_vocab_size=None, word_ngrams=1, loss='ns', sample=0.001, seed=1, workers=3,
                 min_alpha=0.0001, negative=5, cbow_mean=1, hashfxn=hash, iter=5, null_word=0,
                 min_n=3, max_n=6, sorted_vocab=1, bucket=2000000, trim_rule=None,
                 batch_words=10000, epochs=5):
        sentences = None
        self.sg = sg
        self.hs = hs
        self.size = size
        self.alpha = alpha
        self.window = window
        self.min_count = min_count
        self.max_vocab_size = max_vocab_size
        self.word_ngrams = word_ngrams
        self.loss = loss
        self.sample = sample
        self.seed = seed
        self.workers = workers
        self.min_alpha = min_alpha
        self.negative = negative
        self.cbow_mean = cbow_mean
        self.hashfxn = hashfxn
        self.iter = iter
        self.null_word = null_word
        self.min_n = min_n
        self.max_n = max_n
        self.sorted_vocab = sorted_vocab
        self.bucket = bucket
        self.trim_rule = trim_rule
        self.batch_words = batch_words
        self.epochs = epochs
        self.fast_text = FastText(sentences, sg, hs, size, alpha, window, min_count, max_vocab_size,
                 word_ngrams, loss, sample, seed, workers, min_alpha, negative, cbow_mean,
                 hashfxn, iter, null_word, min_n, max_n, sorted_vocab,
                 bucket, trim_rule, batch_words)
        self.is_fit = False

    def fit(self, text, y=None):
        self.fast_text.build_vocab(text)
        self.fast_text.train(text, epochs=self.epochs)
        self.is_fit = True
        return self
```


# In practice: getting the inputs right

Now, my workflow is based on scikit-learn's
[pipelines](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline)
and FastText has been implemented in the Gensim Library but not in sklearn as it is not general enough.
for this reason, FastText was not design to work with sklearn's convenient
[Vectorizers](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_extraction.text)
and has to be fed with a list of words instead of a document-term matrix.
Thus I have to find a way to:

1. combine the feature coming from both methods before feeding them to the classifier which can be done easily with a FeatureUnion

2. do so starting from a different representation of the text (list versus document-term matrix)

3. allow some parameters to be shared between these representations (stop words for instance)

For this, let's first build a class which replicates the pre-processing and tokenizing steps of the Vectorizer.
This yields a list a words for FastText to use while still taking into account the parameters passed to the original
vectorizer and is used with NMF.

```python
from sklearn.base import BaseEstimator

class TextPreProcessor(BaseEstimator):
    def __init__(self, vectorizer):
        self.vectorizer = vectorizer
        self.preprocess = vectorizer.build_preprocessor()
        self.tokenize = vectorizer.build_tokenizer()

    def fit(self, text, y=None):
        return self

    def transform(self, text):
        return np.array([self.tokenize(self.preprocess(self.vectorizer.decode(t))) for t in text])

    def fit_transform(self, text, y=None):
        return self.transform(text)
```

# In practice: putting it all together

Then, it is mostly a matter of building and pluging the corresponding pipes together
into a final pipeline:

```python       
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import StratifiedKFold, GridSearchCV

train_vectorizer = CountVectorizer()
doc_fast_text = pftc.DocumentFastText()
fasttext_subpipe = Pipeline(steps=[('text_prepro', pftc.TextPreProcessor(train_vectorizer)),
                                   ('transfo', doc_fast_text)])
nmf = NMF()
nmf_subpipe = Pipeline(steps=[('vectorizer', train_vectorizer), ('transfo', nmf)])

feature_union = FeatureUnion([("embedding", fasttext_subpipe), ("topics", nmf_subpipe)])

classifier = GradientBoostingClassifier()
pipe = Pipeline(steps=[('feature_extraction', feature_union), ("classfier", classifier)])

```

I can then run my workflow; a grid search over parameters for instance.
Conveniently, multiple nesting of parameters are handled with the "__" syntax.

```python
params_grid = {
    "feature_extraction__embedding__transfo__size": [100, 200],
    "feature_extraction__embedding__transfo__min_count": [2, 5],
    "feature_extraction__embedding__transfo__word_ngrams": [1, 2, 3],

    "feature_extraction__topics__vectorizer__ngram_range": [(1, 1), (1, 2), (1, 3)],
    "feature_extraction__topics__vectorizer__binary": [True, False],

    "feature_extraction__topics__transfo__n_components": [100, 200],
    "feature_extraction__topics__transfo__alpha": [0, 0.25, 0.5],
    "feature_extraction__topics__transfo__l1_ratio": [0, 0.5, 1]
}

kfold_cv = StratifiedKFold()
gs_cv = GridSearchCV(pipe, param_grid=params_grid,
                     scoring=best_cut_mcc_scoring, cv=kfold_cv,
                     n_jobs=n_cores, verbose=10,
                     random_state=RANDOM_STATE_SEED).fit(train_text, train_decision)
```

And that's it.

# Epilogue
It turns out that using both feature spaces as input improves on using either separately.

# References:

- [https://stats.stackexchange.com/questions/221715/apply-word-embeddings-to-entire-document-to-get-a-feature-vector](https://stats.stackexchange.com/questions/221715/apply-word-embeddings-to-entire-document-to-get-a-feature-vector)
- [https://arxiv.org/abs/1607.00570](https://arxiv.org/abs/1607.00570)
