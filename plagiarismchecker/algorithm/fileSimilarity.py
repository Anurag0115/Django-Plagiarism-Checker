import re
import math
from nltk.corpus import stopwords


def findFileSimilarity(inputQuery, database):
    if not inputQuery or not database:
        return 0.0

    # Convert to lowercase
    lowercaseQuery = inputQuery.lower()
    databaseLower = database.lower()

    # Define English stopwords
    en_stops = set(stopwords.words('english'))

    # Tokenize and clean words (remove punctuation)
    queryWordList = re.sub(r"[^\w]", " ", lowercaseQuery).split()
    databaseWordList = re.sub(r"[^\w]", " ", databaseLower).split()

    # Build a set of unique, non-stop words
    universalSetOfUniqueWords = list({
        word for word in queryWordList + databaseWordList
        if word and word not in en_stops
    })

    if not universalSetOfUniqueWords:
        return 0.0

    # Term frequency (TF) vectors
    queryTF = [queryWordList.count(word) for word in universalSetOfUniqueWords]
    databaseTF = [databaseWordList.count(word) for word in universalSetOfUniqueWords]

    # Cosine similarity
    dotProduct = sum(q * d for q, d in zip(queryTF, databaseTF))
    queryMagnitude = math.sqrt(sum(q ** 2 for q in queryTF))
    databaseMagnitude = math.sqrt(sum(d ** 2 for d in databaseTF))

    # Avoid division by zero
    if queryMagnitude == 0 or databaseMagnitude == 0:
        return 0.0

    matchPercentage = (dotProduct / (queryMagnitude * databaseMagnitude)) * 100
    return matchPercentage
