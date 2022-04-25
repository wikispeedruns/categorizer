import csv

class dataLoader:
    
    def __init__(self, labelsfilename, textfilename):
        
        self.articles = {}
        self.labelsfilename = labelsfilename
        self.textfilename = textfilename
        
        self.label_mappings = {
                                "id":"count",
                                "name":"count",
                                "NSCI":"Natural Sciences",
                                "GEOG":"Geography",
                                "ECOL":"Ecology",
                                "TECH":"Technology",
                                "HLTH":"Human Health & Medicine",
                                "SSCI":"Human Society",
                                "PPLE":"People",
                                "GOVM":"Government & Politics",
                                "ECMY":"Economy & Business",
                                "CSMR":"Consumer goods",
                                "CULT":"The Arts",
                                "HIST":"Human History",
                                "RELG":"Religion",
                                "FOOD":"Food & Drinks",
                                "SPRT":"Sports & Games",
                                "ENTR":"Entertainment"
                                }
        
        self.length = 0
        
    def loadData(self):
        
        with open(self.labelsfilename, mode='r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            #headers = csv_reader.fieldnames
            
            for row in csv_reader:
                self.articles[row['name']] = row   
                self.length += 1
                
        with open(self.textfilename, mode='r', encoding="utf-8") as csv_file:
            
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                
                name = row['name']
                text = row['text']
                
                if name in self.articles:
                    if int(row['text_length']) == 0:
                        print("Empty text for " + name + ", removing from dict")
                        self.length -= 1
                        self.articles.pop(name, None)
                    else:
                        self.articles[name]['text'] = text
                        self.articles[name]['text_length'] = row['text_length']
                else:
                    print("missing article: " + str(name) + ", " + str(row['id']))
                    
                    
    def getArticleByName(self, name):
        return self.articles[name]