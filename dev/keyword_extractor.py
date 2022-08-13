from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import numpy as np
from keybert import KeyBERT

class TfIdfExtractor:
    """
    An encapulation of TF-IDF extractor from sklearn
    """
    def __init__(self):
        """
        Initialize the class using TfidfVectorizer from sklearn
        """
        self.vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))

    def extract_keywords(self, doc, keep_term=3):
        """Extract keywords using TF-IDF algorithm

        Args:
            doc (list): a list of sentences to extract keywords
            keep_term (int, optional): Number of keywords to return. If there are less than specified keywords to return, all keywords will be returned. Defaults to 3.

        Returns:
            list: A list of keywords-score pairs.
        """
        vectors = self.vectorizer.fit_transform(doc)
        feature_names = self.vectorizer.get_feature_names()
        dense = vectors.todense()
        index = np.asarray(np.argsort(dense, axis=1)[:, :(-1-keep_term):-1])
        output = []
        for i,term in enumerate(index):
            features = [feature_names[y] for y in term]
            scores = [dense[i, x] for x in term]
            term_feature = []
            for ii, s in enumerate(scores):
                if s > 0:
                    term_feature.append(tuple([features[ii], s]))
            output.append(term_feature)
        return output

class KeyBERTExtractor:
    """An naive ecapsulation of KeyBERT to ensure similar APIs
    """
    def __init__(self, model='../pretrained_models/all-MiniLM-L6-v2'):
        """Initiate KeyBERT using saved embedding model

        Args:
            model (str, optional): Path to local model. Defaults to '../pretrained_models/all-MiniLM-L6-v2'.
        """
        self.model = KeyBERT(model=model)

    def extract_keywords(self, doc, keyphrase_ngram_range=(1,1), stop_words=stopwords.words('english'), keep_term=3, fast_algo=False):
        """An naive encapsulation of extract_keywords function. This function use a slow but memory efficient algorithm by default.

        Args:
            doc (list): A list of string to extract keywords from.data
            keyphrase_ngram_range (tuple, optional): The range of ngrams allowed. Defaults to (1,1).
            stop_words (list, optional): A list of stopwords. Defaults to stopwords.words('english').
            keep_term (int, optional): Number of keywords to keep. If a sentence has less keywords than specified number, all keywords will be returned. Defaults to 3.

        Returns:
            list: A list of keywords-score pairs.
        """
        if fast_algo:
            return self.model.extract_keywords(doc, keyphrase_ngram_range=keyphrase_ngram_range, stop_words=stop_words, top_n=keep_term)
        
        if isinstance(doc, str):
            return self.model.extract_keywords(
                doc, keyphrase_ngram_range=keyphrase_ngram_range, stop_words=stop_words, top_n=keep_term, use_mmr=True, use_maxsum=False)

        output = []
        for i in doc:
            term_feature = self.model.extract_keywords(
                i, keyphrase_ngram_range=keyphrase_ngram_range, stop_words=stop_words, top_n=keep_term, use_mmr=True, use_maxsum=False)
            output.append(term_feature)
        return output
