import base64
import requests
import json
import sys

ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"

def query_model(prompt=""):
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(ENDPOINT,json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response text returned.")
    
    except requests.RequestException as e:
        return f"Request failed: {e}"

def translate(file, language):
    
    cout = 1
    
    for line in file:
        response = query_model(f"Translate this line \'{line}\' into {language}. Then response only with this format: {line} - Translation")
        print(f"{cout}. {response}")
        cout+=1
        
FILE_PATH = r"Simple_Declarative\EN.txt"
FILE = open(FILE_PATH, 'r', encoding="utf-8")
LANGUAGE = "Tagalog"

translate(FILE_PATH, LANGUAGE)