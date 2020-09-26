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
        res = []
        symps = pd.read_csv('data/symptom_ids.csv')
        for i in range(len(symps.columns)):
            if i > 0:
                key = str(i)
                res.append(symps[key][0])
        self.formTrie(res)

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
        
    
    def Search(self, symptom):
        node = self.root
        found = True
        for ch in list(symptom):
            if not node.children.get(ch):
                found = False
                break
            
            node = node.children[ch]

        return node and node.isEnd and found
        
    def suggestions(self, node, word):
        if node.isEnd:
            self.word_list.append((node.rank, word))
        for ch,n in node.children.items():
            self.suggestions(n, word + ch)
   
    def printSuggestions(self, symptom):
        self.word_list = []
        node = self.root
        nonexsistent = False
        search_char = ''
        for ch in list(symptom):
            if not node.children.get(ch):
                nonexsistent = True
                break
            search_char += ch
            node = node.children[ch]
        if nonexsistent:
            return 0
        elif node.isEnd and not node.children:
            return -1
        t.suggestions(node, search_char)

        self.word_list.sort()
        for s in self.word_list:
            print(s[1])

        
    
    def select(self,symptom):
        self._addRecord(symptom, 1)