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
from json_helper import reddit_worker
from bs4 import BeautifulSoup

def get_html_tag(url, html_data, reap_dir):
    try:
        soup = BeautifulSoup(html_data, 'lxml')
        body_tag = soup.find("body")
        comments = body_tag.find_all("div", class_="md")
        comment_texts = [comment.get_text().strip().replace('\u2019', "'").replace('\n', ".") for comment in comments[2:]] if comments else None
        html_tags = {url: comment_texts}
        
        tags_fname = os.path.join(reap_dir, f"{url.replace('https://old.reddit.com', 'reddit').replace('/', '_')}tags.json")

        if reddit_worker.write_dict(html_tags, tags_fname):
            return html_tags
        return None
    
    except Exception as e:
        print("Error: ", str(e))
        return None
