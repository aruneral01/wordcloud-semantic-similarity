def split_word_or_pdf_to_word_cloud_file(input_file, output_file):
  """Splits a word or PDF document to a word cloud file with frequency.

  Args:
    input_file: The path to the input file.
    output_file: The path to the output file.
  """

  # Split the input file into words.
  words = []
  if input_file.endswith('.pdf'):
    import PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(input_file)
    for page in pdf_reader.pages:
      words += re.split(r'\W+', page.extractText())
  else:
    with open(input_file, 'r') as f:
      words += re.split(r'\W+', f.read())

  # Count the frequency of each word.
  word_counts = collections.Counter(words)

  # Write the word cloud file.
  with open(output_file, 'w') as f:
    for word, count in word_counts.items():
      f.write(f'{word},{count}\n')
