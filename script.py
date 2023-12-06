import re
import requests
import json
import os

def load_config(): #load values from config file
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
    return data

def get_packages(base_url): #gets repo content
    try:
        response = requests.get(base_url)
    except Exception:
        print("Faced an error while sending GET request to git repo")
        exit()
    else:
        if response.status_code > 400:
            print("Page not found, please check your repo link")
            exit()
        return response.json()

def filter_packages(regex_statement, include, base_url):
    packages = get_packages(base_url)

    for package in packages:
        package_name = package['name']
        if include:  #If we want to delete all files matching regex
            if (re.match(regex_statement, package_name)):
                print(f"Package '{package_name}' will be removed.")
        else: #If we want to delete all files NOT matching regex
            if not (re.match(regex_statement, package_name)):
                print(f"Package '{package_name}' will be removed.")

if __name__ == '__main__':
    
    null_device = 'nul' if os.name == 'nt' else '/dev/null'
    py_command = 'python -m' if os.name == 'nt' else 'python3 -m'
    os.system(f"{py_command} pip install -r requirements.txt > {null_device}") #install requirements modules
    params = load_config()
    regex_statement = params["REGEX_STATEMENT"] # store values retrieved from config file to variables
    regex_include = params["REGEX_INCLUDE"]
    api_key = params["API_KEY"]
    base_url = params["BASE_URL"]
    filter_packages(regex_statement, regex_include, base_url)