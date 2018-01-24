def print_hedz(url='https://wgetsnaps.github.io/stanford-edu-news/news/'):
   txt = fetch_html(url)
   htags = parse_headline_tags(txt)
   for t in htags:
       hedtxt = extract_headline_text(t)
       print(hedtxt)
def extract_headline_text(txt):
   return txt.split('>')[2].split('<')[0]

def parse_headline_tags(txt):
    myList = []
    fulltext = htm_fetch()
    lines = fetch_html.splitlines()
    for line in lines:
        if '<h3><a' in line:
            myList.append(line)
    return myList

def fetch_html(url):
    import requests
    url = 'https://wgetsnaps.github.io/stanford-edu-news/news/'
    resp=requests.get(url)
    return(resp.text)