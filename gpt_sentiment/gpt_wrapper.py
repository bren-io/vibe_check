#-------------------------------------------------
# Wrapper module to make the API call to openAI's models
# 
#
# CHORE: Convert GPT response to json list then assign it to the key (url) see OpenAI API json object parameter
# also, implement tiktoken to properly count number of tokens in a comment string
#-------------------------------------------------------

import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
import json
import time
# import tiktoken # Not using yet


#######
# DATA
#######

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, "..", ".env")
load_dotenv(env_path)
#openai.api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)
delimiter = '%%'
prompt = f'You are a helpful analytical psychologist. Determine the sentiment of these comments separately. Each comment ends with {delimiter}. Only indicate if the comment is "+" for positive, "0" for neutral, or "-" for negative. Output as a single string with no white space' # GPT behaviour

########
# END DATA
########

##############################
# Format list to delimited string
##############################

def format_gpt_request(url_comments):
    comments_as_string = delimiter.join(url_comments)# Needed to send all comments in a single request
    comments_as_string = comments_as_string[:4096] + delimiter # Cut the end off, max tokens for prompt + response is 4096, so half 2048, multiply by 4 (avg token character count). Here we multiply by 2 for errors in counting tokens.
    
    return comments_as_string
    
##############################
# Make a call to GPT, you can use any
#############################
def request_sentiment(user_prompt, prompt_content):
    sentiments = ""
    #print(f"Working on {prompt_content}") # For debugging can remove
    # See OpenAI doc for usage
    assistant = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0.7,
        messages=[
            {"role": "system", "content": user_prompt},
            {"role": "user", "content": prompt_content}
        ],
    )
    if assistant.choices[0].finish_reason == 'length':
        time.sleep(11)
        print("Max tokens for model reached. File still created")
        sentiments = assistant.choices[0].message.content
        return sentiments
    else:
        time.sleep(11)
        sentiments = assistant.choices[0].message.content
        return sentiments

###########################
# Write the sentiments out to a file
###########################
def write_sentiment(url, url_tag_content, sentiment_output_dir):
    analysis = request_sentiment(prompt, format_gpt_request(url_tag_content))
    analysis_list = [value for value in analysis]
    try:
        output_sentimentf = os.path.join(sentiment_output_dir, f"{url.replace('https://old.reddit.com', 'reddit').replace('/', '_')}sentiment.json")
        with open(output_sentimentf, 'w', encoding='utf-8') as file:
            json.dump(analysis_list, file, indent=2)
            print(f"JSON HTML TAG SENTIMENT List: {output_sentimentf}")


        return output_sentimentf

    except Exception as e:
        print("Error " + e + " has occured")
        return None
