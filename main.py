#----------------------------
# The start of the program, expects a URL specifically to reddit but will
# work with other HTML files. Behavior unpredictable although if not used
# in a reddit website
#-------------------------------------

# Need sys for reading from command line

import sys
from html_request.get_html_content import url_to_json_dict
from html_request.json_helper import read_json
from html_parse.data_parser import get_html_tags
from gpt_sentiment.gpt_wrapper import write_sentiment

def main():

    # Usage
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL_FILE>")
        sys.exit(1)

    # Data
    ufile = sys.argv[1]
    json_url_list = "data/raw/url_list.json"
    json_url_dict = "data/raw/url_dict.json"
    tag_dir = "data/processed/"
    sentiment_dir = f"{tag_dir}sentiments"

    
    # Driver

    # Create a dict file from the urls
    if url_to_json_dict(ufile, json_url_list, json_url_dict):
        url_dict = read_json(json_url_dict)
        # Get the tags from HTML and sentiments
        for url, content in url_dict.items():
            url_tag_file = get_html_tags(url, url_dict[url], tag_dir)
            url_tag_dict = read_json(url_tag_file)
            write_sentiment(url, url_tag_dict[url], sentiment_dir)
    
if __name__ == "__main__":
    main()
