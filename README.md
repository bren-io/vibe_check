# About

Stuff

This program takes a file containing reddit urls, gets the HTML data from the urls, and sends them to OpenAI API to process

# Installation

You can clone this repository and run the yaml file for setup 

```
git clone <HTTPS/SSH/CLI>
python -m venv <env_name>  # Create a new venv
source <env_name>/bin/activate  # Activate the venv on Unix-like systems (use `activate.bat` on Windows)
pip install -r environment.yml  # Install packages from the YAML file
```

You will also need to provide an API key for OpenAI

```
touch .env # MUST match this name and be in the root directory of the application
```

Inside this file use this format

```
OPENAI_API_KEY=abc123
```

# Usage

```
python main.py <url_file>
```

# OpenAI

Go to the openai.com to sign up. Once you login there will be two option between chatgpt and API. After selecting API go to the menu and select API keys. From here you may create a unique key that will be the authenticator for making calls to the API.

You can refrence the library in your program by importing it. There are two ways you can invoke the openai class, directly or using the contstructor. If called directly you must use

```
openai.api_key = os.environ.get("OPENAI_API_KEY")
```

otherwise you can pass the key to the constructor

```
client = OpenAI(
       api_key=os.environ.get("OPENAI_API_KEY"),
)
```

Optionally you can replace the environment variable name with a custom name

# CHORES

Implementation is to only handle roughly 4096 tokens per request. See how to count tokens gpt_wrapper.py:format_gpt_request()

Need to encapsulate a lot of features and maybe make a class to work with instead of modules.

Should allow user to interact and change file directories, switch GPT model, file formats.

When pushing the matplotlib graphs to github, you may sometimes need to delete them from github first. Simply remove them from your local directory and push the changes.