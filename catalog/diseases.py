import pandas as pd
import logging

class DiseaseInfo:
    def __init__(self):
        df = pd.read_csv('data/Disease_names.csv')

        self.names = df['Disease_Name'].tolist()
        webmd_url = "https://www.webmd.com/search/search_results/default.aspx?query="

        self.disease_to_links = {}
        for disease in self.names:
            self.disease_to_links[disease] = webmd_url + disease.replace(" ", "%20")
        
        self.diseaseid_to_info = []
        for i, disease in enumerate(self.names):
            self.diseaseid_to_info.append((disease, self.disease_to_links[disease]))  

    def get_diseaseinfo (self, disease_id):
        if disease_id < 0 or disease_id > len(self.diseaseid_to_info)-1:
            return ('error', 'www.error.com')
        else:
            return self.diseaseid_to_info[disease_id]





        
        


