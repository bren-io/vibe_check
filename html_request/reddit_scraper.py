#--------------------------------------
# This module takes a list of URL's and creates a json dict as "URL: HTML"
#
# CHORE: Maybe see about moving all the json related functions into the json_helper.py script
#-------------------------------------

import requests
import time
from json_helper import reddit_worker

def download_text(url, max_retries, retry_delay):
    for attempt in range(max_retries):
        try:
            # Send HTTP GET request
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
    
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occured: {str(e)}")
            return None
        
        except Exception as e:
            print(f"An error occured: {str(e)}")
            return None

        if attempt < max_retries -1:
            time.sleep(retry_delay)

    return None

def get_html_raw(f_urls, raw_dir): 
    url_fname = f"{raw_dir}/url_list.json"
    html_fname = f"{raw_dir}/html_raw.json"
    url_list = []
    html_data = {}
    
    try:
        if reddit_worker.make_url_list(f_urls, url_fname):
            url_list = reddit_worker.read_json(url_fname)

        if url_list:
            if isinstance(url_list, list):
                for entry in url_list:
                    html_data[entry] = download_text(entry, 50, 0.1)

                if reddit_worker.make_html_raw(html_data, html_fname):
                    return html_data

            #--------
            # CHORE
            #-------
            elif isinstance(url_list, dict):
                
                return False
            
            else:
                print("Invalid json")
                return False

    except Exception as e:
        print(f"Error: {e}")
        return False
