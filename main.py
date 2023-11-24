#----------------------------
# The start of the program, expects a URL specifically to reddit but will
# work with other HTML files. Behavior unpredictable although if not used
# in a reddit website
#-------------------------------------

# Need sys for reading from command line

import sys
import os
import json
from html_request.get_html_content import url_to_json_dict
from html_request.json_helper import read_json
from html_parse.data_parser import get_html_tags
from gpt_sentiment.gpt_wrapper import write_sentiment
from visualizer.pandas_helper import json_to_pandas
from visualizer.graph_helper import data_to_graph
import matplotlib.pyplot as matplt

def main():

    # Usage
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL_FILE>")
        sys.exit(1)

    # Data
    ufile = sys.argv[1]
    json_url_list = "data/raw/url_list.json"
    json_url_dict = "data/raw/url_dict.json"
    tag_dir = "data/processed"
    sentiment_dir = f"{tag_dir}/sentiments"

    
    # Driver

    # Create a dict file from the urls
    if url_to_json_dict(ufile, json_url_list, json_url_dict):
        url_dict = read_json(json_url_dict)
        # Get the tags from HTML and sentiments
        for url, content in url_dict.items():
            url_tag_file = get_html_tags(url, url_dict[url], tag_dir)
            url_tag_dict = read_json(url_tag_file)
            write_sentiment(url, url_tag_dict[url], sentiment_dir)


# Create visual representation of sentiments for a post
def graph_data():
    sentiment_dir = "data/processed/sentiments"
    plot_dir = "data/plots"
    file_list = os.listdir(sentiment_dir)

    for file_name in file_list:
        if file_name.endswith(".json"):
            file_path = os.path.join(sentiment_dir, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                # Load json to pandas data frame and count values
                json_data = json.load(file)
                df = json_to_pandas(json_data)
                vibe_count = df.loc[0].value_counts()

                # Plot the data frame
                matplt.bar(vibe_count.index, vibe_count.values)
                matplt.xlabel('Sentiments')
                matplt.ylabel('Count')
                matplt.title(f'{file_name.replace("reddit_r_", "").replace("comments_", "").replace("_sentiment.json", "")}')
                matplt.savefig(f'{plot_dir}/{file_name.replace(".json", ".png")}')
                
if __name__ == "__main__":
#    main()
    graph_data()
