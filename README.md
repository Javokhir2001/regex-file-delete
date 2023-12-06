# regex-file-delete
To use this repo correctly, change parameters in config.json file

## How to run a script

Just execute script.py file and it thats it, no need to add extra arguments etc. Just make sure that config.json file is in the same dir

## Parameters

* **API_KEY** parameter is used to store your API key in case if repository if private
* **REGEX_INCLUDE** boolean parameter that sets wether to delete files that match regex if True, and delete all other files if False
* **BASE_URL** is a URL to repo that we want to clean
* **REGEX_STATEMENT** is our regex statement that we want to apply