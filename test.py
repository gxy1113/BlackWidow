from bs4 import BeautifulSoup
import os
import sys
import json
import re
#appname = sys.argv[1]

def load_file(folder, name):
    try:
        with open(folder + 'a_' + name, 'r') as f:
            data = json.load(f)
        return data
    except:
        return False
    
def write_file(folder, name, data):
    try:
        with open(folder + 'a_' + name, 'w') as f:
            json.dump(data, f, indent=4)
    except:
        print("failed to write to file")
        return False
    
def html_parser(page_html):
    if(len(page_html) == 0):
        return False
    soup = BeautifulSoup(page_html, 'html.parser')
    page_text = soup.get_text()
    page_text = re.sub(r'\W+', '', page_text)
    html_str = soup.body.prettify()

page_html = load_file("data/", "page_html.json")
html_parser(page_html)