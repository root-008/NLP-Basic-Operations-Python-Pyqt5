# Natural Language Processing Application

This project provides an interface for performing basic Natural Language Processing (NLP) operations. It is developed using Python and the NLTK library.

## Screenshot
<img src="https://github.com/root-008/NLP-Basic-Operations-Python-Pyqt5/assets/100479281/2dd316f5-4af4-4080-b965-f98dc56c96c2" width = 700/>

## Features

- **Word Tokenization**: Tokenizing words in a text.
- **Part-of-Speech Tagging**: Identifying the part of speech of words (verb, noun, etc.).
- **Stemming**: Reducing words to their roots using Porter and Snowball Stemmer.
- **Lemmatization**: Reducing words to their dictionary forms.
- **Stopword Removal**: Removing irrelevant words (stopwords) from the text.
- **Morphological Analysis**: Analyzing the morphological structure of words.
- **Finding Structural Connections with WordNet**: Determining hierarchical relationships between words using WordNet.
- **Finding Structural Connections with Model**: Determining the similarity between words using the word2vec model.
- **Word Relationships in Text**: Identifying relationships between words within the text.
- **Lexical Density**: Calculating the ratio of unique words to the total number of words in a text.
- **Phrase Identification**: Identifying phrase structures such as Noun-Noun, Adjective-Noun, Determiner-Noun in the text.
- **Identifying Structural Elements**: Recognizing structural elements like headings, subheadings, list items, and paragraphs in the text.
- **Word Distribution**: Calculating the most frequent words that follow a given word.
- **Trigram Analysis**: Analyzing trigrams in the text and calculating their frequencies.

## Usage

1. Clone or download the project.
2. Install the required libraries (NLTK, Spacy, Gensim).
3. Run the `main_screen.py` file.
4. Enter your text in the interface.
5. Select the desired NLP operation and click the "Show Result" button.
6. The results will be displayed in a table.

## Installation

### Install Libraries

```bash
pip install nltk spacy gensim
```
### Download Spacy Model

```bash
python -m spacy download en_core_web_sm
```

### Resources
NLTK: https://www.nltk.org/

Spacy: https://spacy.io/

Gensim: https://radimrehurek.com/gensim/

WordNet: https://wordnet.princeton.edu/
