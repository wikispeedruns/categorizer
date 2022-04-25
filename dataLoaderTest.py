from dataLoader import dataLoader
from parse_textExtract import textExtract


if __name__ == '__main__':
    
    ##loading from new unseen data (Article NAME):
    print("testing API call")
    t = textExtract()
    
    while (True):
        cmd = input("Enter article name ('exit' to end) >> ") #639 should return Alkane
        if cmd == 'exit':
            break
        try:
            article = t.getArticleText(cmd) #should return article info for 'alkane'
            print(article)
        except:
            print("ERROR")
    
    
    
    
    ## loading from existing dataset
    print("testing local data import")
    d = dataLoader('combined_labeled.csv', 'combined_labeled_text.csv')
    
    print("Starting load")
    d.loadData()
    print("Finished data load, total: " + str(d.length))
    
    while (True):
        cmd = input("Enter article ID (exit to end) >> ") #Alkane
        if cmd == 'exit':
            break
        
        try:
            article = d.getArticleByName(cmd) #should return article info for 'alkane'
            
            print(article['name'])
            print(article['text_length'])
        except:
            print("ERROR")