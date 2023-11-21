# SE_fall23

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

# Project 3

I did create a branch when I did this part, when I merged it with my main branch I deleted the project3 branch. So you will not see it here.

# Project 4

First you would go to the openai.com to sign up. Once you login there will be two option between chatgpt and API. After selecting API go to the menu and select API keys. From here you may create a unique key that will be the authenticator for making calls to the API. You MUST save your API key or write it down somewhere for security. If you lose it you'll have to make a new one.

Now to make a call you will need to install the openai package. After you install this package you can refrence the library in your program by importing it. There are two ways you can invoke the openai class, directly or using the contstructor. If called directly you must use

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

# Project 5

Refactored a TON from project4 Usage and Installation havent changed though other than the fact that you pass a file containing a url now instead of the actual url
Also note that this implementation is to only handle roughly 4096 tokens. See gpt_wrapper.py:format_gpt_request()