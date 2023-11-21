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
prompt = f"You are a helpful psychiatrist that can analyze the sentiment of messages. Only return the sentiments of the given messages, delimited by {delimiter}. Format your response as comma seperated values" # Prompt to tell the GPT model how to behave

########
# END DATA
########

##############################
# Format list to delimited string
##############################

def format_gpt_request(url_comments):
    comments_as_string = delimiter.join(url_comments) # Needed to send all comments in a single request
    comments_as_string = comments_as_string[:7777] # Cut the end off, max tokens for prompt + response is 4096, so half 2048, multiply by 4 (avg token character count) and subtract some extra for error
        
    return comments_as_string
    
##############################
# Make a call to GPT, you can use any
#############################
def request_sentiment(user_prompt, prompt_content):
    sentiments = ""
    #print(f"Working on {prompt_content}") # For debugging can remove
    # See OpenAI doc for usage
    assistant = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": user_prompt},
            {"role": "user", "content": prompt_content}
        ],
        max_tokens=2048
    )
    if assistant.choices[0].finish_reason == 'length':
        print("Max tokens for model reached. File still created")
        sentiments = assistant.choices[0].message.content
        return sentiments
    else:
        sentiments = assistant.choices[0].message.content
        return sentiments

###########################
# Write the sentiments out to a file
###########################
def write_sentiment(url, url_tag_content, sentiment_output_dir):
    analysis = request_sentiment(prompt, format_gpt_request(url_tag_content))
    try:
        sentiment_buffer = {url: analysis}
        output_sentimentf = os.path.join(sentiment_output_dir, f"{url.replace('https://old.reddit.com', 'reddit').replace('/', '_')}_sentiment.json")
        with open(output_sentimentf, 'w', encoding='utf-8') as file:
            json.dump(sentiment_buffer, file, indent=2)
            print(f"JSON HTML TAG SENTIMENT Dict: {output_sentimentf}")


        return output_sentimentf

    except Exception as e:
        print("Error " + e + " has occured")
        return None
