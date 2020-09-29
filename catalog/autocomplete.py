import pandas as pd
import os
import logging

class TrieNode():
   
    def __init__(self):
        self.children = {}
        self.rank = 0
        self.isEnd = False
        self.data = None

class AutocompleteSystem():
  
    def  __init__(self):
        self.root = TrieNode()
        self.searchWord = ''
        symps = pd.read_csv('data/symptom_ids.csv')

        self.symptoms = []

        for i in range(len(symps.columns)):
            if i > 0 and i != 169:
                key = str(i)
                self.symptoms.append(symps[key][0].lower())
        self.formTrie(self.symptoms)

    def formTrie(self, symptoms):
        for symptom in symptoms:
            self._addRecord(symptom, 0)

    def _addRecord(self, symptom, hotdegree):       
        node = self.root

        for ch in list(symptom):
            if not node.children.get(ch):
                node.children[ch] = TrieNode()

            node = node.children[ch]
        
        node.isEnd = True
        
        node.data = symptom
        node.rank -= hotdegree
        
    
    '''def Search(self, symptom):
        node = self.root
        found = True
        for ch in list(symptom):
            if not node.children.get(ch):
                found = False
                break
            
            node = node.children[ch]

        return node and node.isEnd and found'''
        
    def suggestions(self, node, word):
        if node.isEnd:
            self.word_list.append((node.rank, word))
        for ch,n in node.children.items():
            self.suggestions(n, word + ch)
   
    def search(self, symptom):
        self.word_list = []
        node = self.root
        nonexsistent = False
        search_char = ''
        for ch in list(symptom.lower()):
            if not node.children.get(ch):
                nonexsistent = True
                break
            search_char += ch
            node = node.children[ch]
        if nonexsistent:
            return []
        self.suggestions(node, search_char)
        res = [s[1].title() for s in sorted(self.word_list)[:5]]
        logging.debug(res)
        return res

    def get_symptom_id(self, symptom_name):
        symptom_name = symptom_name.lower()
        if (symptom_name in self.symptoms):
            return self.symptoms.index(symptom_name)
        else:
            return -1
    
    def get_symptom_name(self, symptom_id):
        return self.symptoms[int(symptom_id)]


        
    def select(self,symptom_id):
        if 0 <= symptom_id < len(self.symptoms):
            self._addRecord(self.symptoms[symptom_id], 1)