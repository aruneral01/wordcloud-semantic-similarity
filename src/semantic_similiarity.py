import re
from nltk.corpus import wordnet

def calculate_semantic_similarity(word1, word2):
  """Calculates the semantic similarity between two words using WordNet.

  Args:
    word1: The first word.
    word2: The second word.

  Returns:
    A float value between 0 and 1, where 1 represents perfect similarity and 0
    represents no similarity.
  """

  # Get the WordNet synsets for the two words.
  # A synset is a set of synonyms that share a common meaning.
  synset1 = wordnet.synsets(word1)
  synset2 = wordnet.synsets(word2)

  # If either word has no synsets, then the similarity is 0.
  if not synset1 or not synset2:
    return 0.0

  # Calculate the path similarity between the two synsets.
  # Path similarity is a measure of how similar two words are based on the shortest
  # path between their synsets in the WordNet hierarchy.
  path_similarity = synset1[0].path_similarity(synset2[0])

  # If the path similarity is None, then the similarity is 0.
  if path_similarity is None:
    return 0.0

  # Return the path similarity.
  return path_similarity

def main():
  # Get the two words to compare.
  word1 = 'cat'
  word2 = 'dog'

  # Calculate the semantic similarity between the two words.
  semantic_similarity_score = calculate_semantic_similarity(word1, word2)

  # Print the semantic similarity score.
  print(f'Semantic similarity score: {semantic_similarity_score}')


if __name__ == '__main__':
  main()
