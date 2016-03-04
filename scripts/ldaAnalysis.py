from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

nTopics = [5, 10, 20]
nWords = [3, 5, 8, 10]

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# compile sample documents into a list
doc_set = []
folder = "../resources/TheirOwnWords/Republic/"
files = ["JebBush/JebBush.txt", "BenCarson/BenCarson.txt", "ChrisChristie/ChrisChristie.txt", "TedCruz/TedCruz.txt", "CarlyFiorina/CarlyFiorina.txt", "JohnKasich/JohnKasich.txt", "MarcoRubio/MarcoRubio.txt", "RickSantorum/RickSantorum.txt"]
for file1 in files:
    with open(folder+file1, "rb") as f:
        for line in f:
            doc_set.append(line.decode('utf-8'))


# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [j for j in tokens if not j in en_stop and len(j)>1]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(j) for j in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)
    #texts.append(stopped_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
for NUM_WORDS in nWords:
    for NUM_TOPICS in nTopics:
        print "# Topics =", NUM_TOPICS, "# Words =", NUM_WORDS
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word = dictionary, passes=20)
        for elem in ldamodel.print_topics(num_topics=NUM_TOPICS, num_words=NUM_WORDS):
            print elem
        print "-"*80
