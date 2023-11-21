#--------------------------------------
# This module uses a url, HTML data, and a path to a directory
# Parses the HTML data using bs4.
# Then writes a json dict of the parsed HTML data
#
# @ line 24 important to strip before replacing, since strip only handles starting and ending whitespace.
# Also maybe look for something better than "." to replace \n with?
# Lastly I tried using python .text which resulted in an error?? Idk why
#------------------------------------

import os
import lxml
import chardet
import json
from bs4 import BeautifulSoup

def get_html_tags(url, url_content, tag_path):
    try:
        soup = BeautifulSoup(url_content, 'lxml')
        body_tag = soup.find("body")
        comments = body_tag.find_all("div", class_="md")
        comment_texts = [comment.get_text().strip().replace('\u2019', "'").replace('\n', ".") for comment in comments[2:]] if comments else None
        tag_buffer = {url: comment_texts}
        
        output_tagf = os.path.join(tag_path, f"{url.replace('https://old.reddit.com', 'reddit').replace('/', '_')}_tags.json")

        with open(output_tagf, 'w', encoding='utf-8') as tag_file:
            json.dump(tag_buffer, tag_file, indent=2)    
            print(f"JSON HTML TAG Dict: {output_tagf}")

            
        return output_tagf
    
    except Exception as e:
        print("Error: ", str(e))
        return None
