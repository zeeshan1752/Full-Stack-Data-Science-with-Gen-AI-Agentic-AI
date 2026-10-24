
import nltk

from nltk.stem import PorterStemmer

#using porter stemmer you can always stem the word called from PorterStemmer 
#poterstemmer librarty will help you to find the root word 

from nltk.corpus import stopwords

paragraph = '''AI, machine learning and deep learning are common terms in enterprise 
                IT and sometimes used interchangeably, especially by companies in their marketing materials. 
                But there are distinctions. The term AI, coined in the 1950s, refers to the simulation of human 
                intelligence by machines. It covers an ever-changing set of capabilities as new technologies 
                are developed. Technologies that come under the umbrella of AI include machine learning and 
                deep learning. Machine learning enables software applications to become more accurate at 
                predicting outcomes without being explicitly programmed to do so. Machine learning algorithms 
                use historical data as input to predict new output values. This approach became vastly more 
                effective with the rise of large data sets to train on. Deep learning, a subset of machine 
                learning, is based on our understanding of how the brain is structured. Deep learning's 
                use of artificial neural networks structure is the underpinning of recent advances in AI, 
                including self-driving cars and ChatGPT.'''
                
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

#import stopwords
# I want to remove all the stopwords from my senterences 
# if you check the stopwords.words('english') you get a list of word which is not at all value to the paragraph
# you do get stopwords in many language. 
# after removing the stopwords i am going to stem the words by using portstemmer

# using for loop for all of sentences & using word_tokenize will convert all sentences to words
# basically i am writhing for word in words and i am taking from unique word from stopword.english
# Stemming

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)