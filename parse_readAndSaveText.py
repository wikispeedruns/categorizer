import csv
import json
from parse_textExtract import textExtract

def dict_filter(it, *keys):
    for d in it:
        yield dict((k, d[k]) for k in keys)

if __name__ == '__main__':

    articles = {}
    textExtractor = textExtract()

    with open('combined_labeled.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        headers = csv_reader.fieldnames
        
        for row in dict_filter(csv_reader, 'id', 'name'):
            articles[row['id']] = row   

    counter = 0

    with open('combined_labeled_text.csv', 'w', encoding="utf-8", newline='') as csvfile:
        headers = ['id', 'name', 'text', 'text_length']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        
        writer.writeheader()
        for id in articles:
            article = {'id': articles[id]['id'], 'name': articles[id]['name']}
            
            if counter < 30000:
                try:
                    text = textExtractor.getArticleText(article['name']).replace('\n', ' ')
                except:
                    print("ERROR: "+ article['name'])
                    text = ""
                print(counter, id)
            else:
                text = ""
            article['text'] = json.dumps(text)
            article['text_length'] = len(text)
            writer.writerow(article)
            
            counter += 1