This is a code on sentiment analysis using twitter dataset available for free on multiple sources including kaggle.
Availale here - http://help.sentiment140.com/for-students

the dataset has 1.6 million tweets with a sentiment target value of 0-negative or 4-positive.
Additional columns are: timestamp, query (which is blank), and username.
While the extra info might be useful in some other cases, for Sentiment Analysis we will only need the tweets and target values.


Broad Steps:

1. Basic EDA: Going through the data, exploring the counts and frequency of tweets
		result- Post removal of mentions from tweets (@___), repititions are observed, with different target values,
		Duplicates removed, final target value averaged and rounded off. midway values(=2) and blank tweets are removed

2. Preprocessing: Just like any other NLP project we use preprocessing techniques on text to make it computer-readable.
		we use RegEx and NLTK for that. 

3. Embeddings: After preprocessing, the sentences obtained, are encoded to form vectors, which can directly be used on different algorithms to generate results. I use 2 different embedding methods, and have made different notebooks for that. First, TF-IDF vectoriser. this vectoriser takes individual words and counts their frequency of appearance in the sentence (TF) and in the document and takes reciprocal (IDF) and assigns a value which is grouped together to give a vector value to a sentence. This vector is then used for any classification algorithm. Second, I use Word2Vec tool from gensim library. this tool helps me assign a semantic value (or a vector) to individual words. Using this we can check between similarity of words and such. The vectors are then clubbed together and padded to form vector inputs to different algorithms. This methods is more compatible with methods like ANN. 

4. Data Modelling:  Due to some computation restrictions, only simple methods are used, like Naive Bayes, Logistic Regression, Support Vector Classifiers.
		with some sampling we also use methods like random forests, and XGBoost
		
