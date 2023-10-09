import word_split_utils
import word_cloud_utils
import semantic_similarity

def main():
  # Get the paths to the input and output files.
  input_file_1 = 'data/word_cloud_1.txt'
  input_file_2 = 'data/word_cloud_2.txt'
  output_file_1 = 'data/word_cloud_1.csv'
  output_file_2 = 'data/word_cloud_2.csv'

  # Split the input files into word cloud files.
  word_split_utils.split_word_or_pdf_to_word_cloud_file(input_file_1, output_file_1)
  word_split_utils.split_word_or_pdf_to_word_cloud_file(input_file_2, output_file_2)

  # Load the word cloud files.
  word_cloud_1_text = word_cloud_utils.load_word_cloud_text(output_file_1)
  word_cloud_2_text = word_cloud_utils.load_word_cloud_text(output_file_2)

  # Extract the keywords from each word cloud.
  word_cloud_1_keywords = word_cloud_utils.extract_keywords(word_cloud_1_text)
  word_cloud_2_keywords = word_cloud_utils.extract_keywords(word_cloud_2_text)

  # Calculate the semantic similarity between the two sets of keywords.
  semantic_similarity_score = semantic_similarity.calculate_semantic_similarity(word_cloud_1_keywords, word_cloud_2_keywords)

  # Print the semantic similarity score.
  print(f'Semantic similarity score: {semantic_similarity_score}')


if __name__ == '__main__':
  main()
