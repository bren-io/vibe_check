#--------------------------------------
# This module takes a list of URL's and creates a json dict as "URL: HTML"
#
# CHORE: Maybe see about moving all the json related functions into the json_helper.py script
#-------------------------------------

import requests
import time
import json
from . import json_helper

def url_content_dict(url_dict, json_dict):
    with open(json_dict, 'w', encoding='utf-8') as json_file:
        json.dump(url_dict, json_file, indent=2)

    print(f"JSON URL Dict: {json_dict}")
    return json_dict

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

def url_to_json_dict(url_list, url_json_list, url_json_dict):
    HTML_dict = {} # Buffer for url_json_dict
    try:
        json_fname = json_helper.write_json(url_list, url_json_list) # convert file to json format
        print(f"JSON URL List: {json_fname}")
        
        if json_fname:
            urls = json_helper.read_json(json_fname)

        # if we have a list of urls lets get their HTML data
        if urls:
            if isinstance(urls, list):
                for entry in urls:
                    HTML_dict[entry] = download_text(entry, 50, 0.1)
                    
                return url_content_dict(HTML_dict, url_json_dict)
            
            elif isinstance(urls, dict):
                for key, value in url_dat.items():
                    print(f"{key}: {value}")
                    #entry_dict_raw = download_text(entry, 20, 0.1)
                return urls
            
            else:
                print("Invalid json")
                return None

    except Exception as e:
        print(f"Error: {e}")
        return None
