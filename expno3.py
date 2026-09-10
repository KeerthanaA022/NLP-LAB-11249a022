import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = input("Enter a sentence: ")

words = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("\nMorphological Analysis")
print("-" * 50)

print("{:<15} {:<15} {:<15}".format(
    "Original", "Stemmed", "Lemmatized"
))

print("-" * 50)

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print("{:<15} {:<15} {:<15}".format(
        word, stem, lemma
    ))

print("-" * 50)