#----------------------------
# The start of the program, expects a URL specifically to reddit but will
# work with other HTML files. Behavior unpredictable although if not used
# in a reddit website
#-------------------------------------

import sys
import os
import json
from html_request import reddit_scraper
from html_parse import reddit_reaper
from gpt_helper import reddit_gpt
from visualizer import reddit_pandas

#-------------------------
# Constants
#-----------------------

data_dir = "data"
raw_dir = f"{data_dir}/raw"
reap_dir = f"{data_dir}/processed"
vibe_dir = f"{reap_dir}/sentiments"
plot_dir = f"{data_dir}/plots"

#----------------------
# Functions
#---------------------

# Create visual representation of sentiments for a post
def reddit_graph():
    reddit_pandas.get_graph(vibe_dir, plot_dir)
                
def reddit_process():
    # Usage
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL_FILE>")
        sys.exit(1)
        
    # Get file path
    file_path = sys.argv[1]
    if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]
    explicit_path = os.path.abspath(file_path)

    # Open file and process
    if os.path.isfile(explicit_path):
        html_raw = reddit_scraper.get_html_raw(explicit_path, raw_dir)
        for url, html in html_raw.items():
            html_tag = reddit_reaper.get_html_tag(url, html_raw[url], reap_dir)
            tag_vibe = reddit_gpt.get_vibe(url, html_tag[url], vibe_dir)
#            vibe_df = reddit_pd.get_df(url, tag_vibe[url])
    else:
        print(f"Error: {explicit_path} does not exist")

def main():
    return None

if __name__ == "__main__":
#    reddit_process() # Creates files relevant to reddit posts
    reddit_graph()   # Creates graphs from files
