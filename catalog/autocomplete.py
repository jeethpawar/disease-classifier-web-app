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
        

symptoms = ["fever", "feverish", "bodyache", "fart", "fevery"]
symptom = "fev"

t = AutocompleteSystem()
t.formTrie(symptoms)

t.select('feverish')
comp = t.printSuggestions(symptom)
t.select('feverish')    
comp = t.printSuggestions('fe')

if comp == -1:
    print('No strings with this prefix')
elif comp == 0:
    print('No strings wiht this prefix')