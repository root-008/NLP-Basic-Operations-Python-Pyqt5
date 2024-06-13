from model import Model

class Operations:

    @staticmethod
    def getComboboxItem(cbox_operations):
        items = ['Tokenize','Part of Speech Tagging','Porter Stemmer',
                 'Snowball Stemmer','Lemmatization',
                 'Use StopWord','Morpheme Analysis',
                 'Finding Relationships Between Structures (WordNet)',
                 'Finding Relationships Between Structures (Model)',
                 'Word Relationships in Text',
                 'Word Density','Identify Phrases','Identify Structural Elements',
                 'Word Distribution','Trigram Analysis']

        for item in items:
            cbox_operations.addItem(item)

    @staticmethod
    def getSelectedItemToModel(self,selected_item):
        model = Model()

        text = self.edit_text.toPlainText()

        if selected_item == 'Tokenize':
            return model.tokenize(text)
        if selected_item == 'Part of Speech Tagging':
            return model.part_of_speech_tagging(text)
        if selected_item == 'Porter Stemmer':
            return model.apply_porter_stemmer(text)
        if selected_item == 'Snowball Stemmer':
            return model.apply_snowball_stemmer(text)
        if selected_item == 'Lemmatization':
            return model.lemmatization(text)
        if selected_item == 'Use StopWord':
            return model.stopWords(text)
        if selected_item == 'Morpheme Analysis':
            return model.morpheme_analysis(text)
        if selected_item == 'Finding Relationships Between Structures (Model)':
            word1 = self.textbox_varr1.text()
            word2 = self.textbox_varr2.text()
            return model.find_similarity_using_model(word1, word2)
        if selected_item == 'Finding Relationships Between Structures (WordNet)':
            word1 = self.textbox_varr1.text()
            word2 = self.textbox_varr2.text()
            return model.find_relationships(word1, word2)
        if selected_item == 'Word Relationships in Text':
            return model.find_word_relationships(text)
        if selected_item == 'Word Density':
            return model.word_density(text)
        if selected_item == 'Identify Phrases':
            return model.identify_phrases(text)
        if selected_item == 'Identify Structural Elements':
            return model.identify_structural_elements(text)
        if self.selected_item == 'Word Distribution':
            return model.word_distribution(text)
        if self.selected_item == 'Trigram Analysis':
            return model.trigram_analysis(text)
        

    @staticmethod
    def labelNameInputs(self,selected_item):
        self.textbox_varr2.setEnabled(False)
        self.textbox_varr1.setEnabled(False)
        self.label_varr1.setText('No Input')
        self.label_varr2.setText('No Input')
        self.edit_text.setEnabled(True)

        if selected_item == 'Finding Relationships Between Structures (Model)':
            self.label_varr1.setText('Word 1 :')
            self.label_varr2.setText('Word 2 :')
            self.textbox_varr1.setEnabled(True)
            self.textbox_varr2.setEnabled(True)
            self.edit_text.setEnabled(False)
        elif selected_item == 'Finding Relationships Between Structures (WordNet)':
            self.label_varr1.setText('Word 1 :')
            self.label_varr2.setText('Word 2 :')
            self.textbox_varr1.setEnabled(True)
            self.textbox_varr2.setEnabled(True)
            self.edit_text.setEnabled(False)

    