import re
import pandas as pd
import spacy
import gensim.downloader as api
from nltk.corpus import stopwords, wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import pos_tag
from itertools import combinations
from nltk.probability import FreqDist
from nltk.util import ngrams
from collections import defaultdict, Counter

class Model:
    def __init__(self):
        self.porter_stemmer = PorterStemmer()
        self.snowball_stemmer = SnowballStemmer("english")
        self.lemmatizer = WordNetLemmatizer()
        self.tag_dict = self.load_tag_dict()
        self.stop_words = set(stopwords.words('english'))
        
        
    def load_tag_dict(self):
        # POS etiketlerini içeren bir Excel dosyası yükleniyor ve bir sözlüğe dönüştürülüyor.
        df = pd.read_excel('./libraries/postag_list.xlsx')
        return pd.Series(df.Description.values, index=df.Tag).to_dict()
    
    def get_pos_tag(self, word):
        # Kelimenin POS etiketi alınıyor ve uygun WordNet POS etiketiyle eşleştiriliyor.
        tag = pos_tag([word])[0][1]
        
        tag_dict = {
            'JJ': 'a', 'JJR': 'a', 'JJS': 'a',
            'NN': 'n', 'NNS': 'n', 'NNP': 'n', 'NNPS': 'n',
            'RB': 'r', 'RBR': 'r', 'RBS': 'r',
            'VB': 'v', 'VBD': 'v', 'VBG': 'v', 'VBN': 'v', 'VBP': 'v', 'VBZ': 'v',
        }
        
        return tag_dict.get(tag, 'n')

    def tokenize(self, text):
        return word_tokenize(text)
    
    def part_of_speech_tagging(self, text):
        # Metindeki kelimelerin POS etiketlerini alır.
        tokens = self.tokenize(self.stopWords(text))
        tagged = pos_tag(tokens)
        return [(word, self.tag_dict.get(tag, tag)) for word, tag in tagged]
    
    def apply_porter_stemmer(self, text):
        # Metindeki kelimeleri Porter Stemmer ile köklerine ayırır.
        tokens = self.tokenize(text)
        return [self.porter_stemmer.stem(token) for token in tokens]
    
    def apply_snowball_stemmer(self, text):
        # Metindeki kelimeleri Snowball Stemmer ile köklerine ayırır.
        tokens = self.tokenize(text)
        return [self.snowball_stemmer.stem(token) for token in tokens]
    
    def lemmatization(self, text):
        # Metindeki kelimeleri lemmatize eder.
        tokens = self.tokenize(text)
        lemma = []
        for token in tokens:
            pos = self.get_pos_tag(token)
            lemma.append(self.lemmatizer.lemmatize(token, pos))
        
        return lemma
    
    def stopWords(self, text):
        # Metindeki gereksiz kelimeleri çıkarır ve temizler.
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        words = word_tokenize(text)
        filtered_words = [word for word in words if word.lower() not in self.stop_words]
        cleaned_text = ' '.join(filtered_words)
        return cleaned_text
    
    def morpheme_analysis(self, text):
        # Kelimelerin morfolojik analizini yapar.
        filtered_text = self.stopWords(text)
        tokens = word_tokenize(filtered_text)
        morphemes = []
        for word in tokens:
            pos = self.get_pos_tag(word)
            
            lemma = self.lemmatizer.lemmatize(word, pos)
            if lemma != word:    
                suffix = word[len(lemma):]
                morphemes.append((lemma, suffix))
            
        return morphemes

    def find_relationships(self, word1, word2):
        # İki kelime arasındaki ilişkileri bulur.
        synsets1 = wn.synsets(word1)
        synsets2 = wn.synsets(word2)

        relationships = []
        for syn1 in synsets1:
            for syn2 in synsets2:
                if syn1.wup_similarity(syn2) is not None:
                    relationships.append((syn1, syn2, syn1.wup_similarity(syn2)))
        
        sorted_relationships = sorted(relationships, key=lambda x: -x[2])
        formatted_relationships = []

        for rel in sorted_relationships:
            syn1, syn2, similarity = rel
            formatted_relationships.append([
                syn1.name(),
                syn1.definition(),
                syn2.name(),
                syn2.definition(),
                round(similarity, 3)
            ])
        return formatted_relationships
    
    def find_similarity_using_model(self,word1,word2):
        # Model kullanarak iki kelime arasındaki benzerliği bulur.
        model = api.load("word2vec-google-news-300")
        if word1 in model.key_to_index and word2 in model.key_to_index:
            return model.similarity(word1, word2)
        else:
            return None
        
    def find_word_relationships(self, text):
        # Metindeki kelimeler arasındaki ilişkileri bulur.
        threshold=0.50
        # Temizleme ve tokenizasyon
        tokens = [word for word in word_tokenize(text.lower()) if word.isalnum() and word not in self.stop_words]
        model = api.load("word2vec-google-news-300")
        # Kelimeler arasındaki ilişkileri bulma
        relationships = []
        for word1, word2 in combinations(tokens, 2):
            if word1 in model.key_to_index and word2 in model.key_to_index:
                similarity = model.similarity(word1, word2)
                if similarity > threshold:
                    relationships.append((word1, word2, similarity))
        
        return relationships
    
    def word_density(self, text):
        # Metindeki kelime yoğunluğunu hesaplar.
        tokens = self.tokenize(self.stopWords(text.lower()))
        freq = FreqDist(tokens)
        uniq_words = set(tokens)
        uniq_words_count = len(uniq_words)
        total_word_count = len(tokens)
        density = uniq_words_count / total_word_count

        uniq_words_with_freq = sorted([(word, freq[word]) for word in uniq_words], key=lambda x: x[1], reverse=True)

        return uniq_words_count, density, uniq_words_with_freq

    def identify_phrases(self, text):
        # Metindeki tamlama yapıları tanımlar.
        words = word_tokenize(text)
        tagged_words = pos_tag(words)
        phrases = []

        for i in range(len(tagged_words) - 2):
            word1, tag1 = tagged_words[i]
            word2, tag2 = tagged_words[i+1]
            word3, tag3 = tagged_words[i+2]

            if tag1.startswith('NN') and tag2.startswith('NN'):
                phrase = word1 + ' ' + word2
                phrases.append((phrase, "Noun-Noun Phrase"))

            if tag1.startswith('JJ') and tag2.startswith('NN'):
                phrase = word1 + ' ' + word2
                phrases.append((phrase, "Adjective-Noun Phrase"))

            if tag1.startswith('DT') and tag2.startswith('NN'):
                phrase = word1 + ' ' + word2
                phrases.append((phrase, "Determiner-Noun Phrase"))

            if tag1.startswith('NN') and tag2.startswith('DT') and tag3.startswith('NN'):
                phrase = word1 + ' ' + word2 + ' ' + word3
                phrases.append((phrase, "Noun-Determiner-Noun Phrase"))

            if tag1.startswith('RB') and tag2.startswith('JJ') and tag3.startswith('NN'):
                phrase = word1 + ' ' + word2 + ' ' + word3
                phrases.append((phrase, "Adverb-Adjective-Noun Phrase"))

        return phrases
    
    def identify_structural_elements(self,text):
        # Metindeki yapısal ögeleri tanımlar. Başlık paragraf vs.
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)

        structural_elements = []

        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.isupper() and len(line.split()) < 10:
                structural_elements.append(("Title", line))
            elif line.startswith('#'):
                structural_elements.append(("Subheading", line))
            elif line.startswith(('*', '-')):
                structural_elements.append(("List Item", line))
            else:
                # Daha sofistike paragraf tespiti
                if len(line.split()) > 5 and not line.startswith(('>', '    ', ' ')):
                    structural_elements.append(("Paragraph", line))
        
        return structural_elements

    def word_distribution(self, text):
        # Kelimelerin dağılımını hesaplar.
        tokens = self.tokenize(self.stopWords(text.lower()))
        
        # Calculate the most common word following each word
        bigrams = list(ngrams(tokens, 2))
        following_words = defaultdict(lambda: FreqDist())
        for (first, second) in bigrams:
            following_words[first][second] += 1
        
        return following_words
    
    def trigram_analysis(self,text):
        # Metindeki trigram'ları analiz eder.
        tokens = self.tokenize(self.stopWords(text.lower()))
        
        trigrams = list(ngrams(tokens, 3))
        
        freq_dist = Counter(trigrams)
        sorted_freq_dist = freq_dist.most_common()
        
        return sorted_freq_dist
    
