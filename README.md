# trie-cli-global

A CLI that allows a user to update or see a data structure that is hosted globally.

(IMPORTANT: PYTHON 3.9.6 MUST BE INSTALLED!!)

Please Note: 
    The README in the Github will be different from the one in PYPI. This is because the company that is requesting this project will most likely ask me to make the repo       private to keep others from looking at the code as well as development procedure. This is the full README. The one in PYPI simply shows commands and how to use. 
    
Tools Used and How: 
- AWS was used to store the Trie Data Structure. Using AWS' boto3, a pickle file is stored in an s3 bucket. 
    
- A Flask REST API was used to handle client requests and interactions. It is hosted on Heroku and the web URL is https://global-trie-     cli.herokuapp.com/updatetrie/<COMMAND>/<OPTIONAL_WORD>. (Word is optional depending on the command. See the usage instructions below). 
    
- Click was used to create the CLI. When given the correct commands, it will send a GET request via the REQUESTS Library. The returned value is printed afterwards. 
    
- The project was hosted on PYPI. Link is Here (https://pypi.org/project/trie-cli-global/). Install the project via ```pip install trie-cli-global```. 
    
## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install trie-global.

```bash
pip install trie-global
```

## Usage

# To List Trie:
```
trie-global list
```

# To add word to Trie:
```
trie-global add YOUR_WORD
```

# To remove word from Trie:
```
trie-global remove YOUR_WORD
```

# To check if word is from Trie:
```
trie-global check YOUR_WORD
```

# To get recommendations from a prefix:

```
trie-global recommend YOUR_PREFIX
```
