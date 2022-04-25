import csv
from os import listdir
from os.path import isfile, join

myPath = 'raw_data'
onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]

articles = {}

counter_primary = None
counter_secondary = None

dup_counter = 0

label_mappings = {
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
      "ENTR":"Entertainment"}

for file in onlyfiles:
    
    if file.startswith('data_') and file.endswith('.csv'):
        
        fullpath = myPath + "/" + file
        
        with open(fullpath, mode='r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            headers = csv_reader.fieldnames
            
            if headers is None:
                print(f"{fullpath} has no header")
                continue
            
            if counter_primary is None:
                counter_primary = {}
                counter_secondary = {}
                for header in headers:
                    counter_primary[header] = 0
                    counter_secondary[header] = 0
            
            #print(headers)
            
            for row in csv_reader:
                id = row['id']
                if id in articles:
                    dup = articles[id]
                    #print('--------------')
                    #print(dup)
                    #print('--------------')
                    #print(row)
                    
                    dup_counter += 1
                
                articles[id] = row   
                    
            print(dup_counter)
            
for id in articles:     
    article = articles[id]
    #print(article)
    for header in counter_primary:
        
        if header == 'id' or header == 'name':
            counter_primary[header] += 1
            counter_secondary[header] += 1
        else:
            if article[header] == '1':
                counter_secondary[header] += 1
            elif article[header] == '2':
                counter_primary[header] += 1
                
                
for header in counter_primary:
    if header == 'id': continue
    elif header == 'name': print(f"Total articles: {counter_primary[header]}")
    else: print(f"{label_mappings[header]}: Primary: {counter_primary[header]}; Secondary: {counter_secondary[header]}")
    

with open('combined_labeled.csv', 'w', encoding="utf-8", newline='') as csvfile:
    headers = label_mappings.keys()
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    
    writer.writeheader()
    for id in articles:
        writer.writerow(articles[id])