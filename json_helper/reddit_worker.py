# This file wraps the json library for specific usage
# read_json returns a python object depending on the type
# write_json cleans the urls of whitespace and returns the output file
#
# CHORE: Maybe make this its own module in the root directory
# CHORE: Probably should make write_json have functionality for list or dict

import json

def make_html_raw(input_buffer, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(input_buffer, json_file, indent=2)

        print(f"Raw HTML Data: {output_file}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

def read_json(in_file):
    try:
        with open(in_file, 'r', encoding='UTF-8') as file:
            json_dat = json.load(file)

            if isinstance(json_dat, list):
                return json_dat
            elif isinstance(json_dat, dict):
                return json_dat
            else:
                print("Invalid JSON format")
                return None

    except FileNotFoundError:
        print(f"Error: File '{in_file}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{in_file}' JSON decode error")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def make_url_list(input_file, output_file):
    urls = []
    try:
        with open(input_file, 'r', encoding='utf-8', errors='replace') as file:
            urls = [line.replace('www.', 'old.').strip() for line in file]
            
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(urls, json_file, indent=2)

        print(f"URL List: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False
