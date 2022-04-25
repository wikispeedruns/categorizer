import requests
import mwparserfromhell

class textExtract:
    
    def __init__(self):
        return

    def getArticleText(self, name):
        
        if name is None:
            print("No args found for article")
            return
        else:
            response = requests.get(
                'https://en.wikipedia.org/w/api.php',
                params={
                    'action': 'query',
                    'format': 'json',
                    'titles': name,
                    'redirect': 'true',
                    'prop': 'revisions',
                    'rvprop': 'content'
                }).json()

        page = next(iter(response['query']['pages'].values()))
        wikicode = page['revisions'][0]['*']
        parsed_wikicode = mwparserfromhell.parse(wikicode)
        return parsed_wikicode.strip_code()

