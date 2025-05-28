# WiMarka Experiment

This repository is used for experiments evaluating LLM translation tasks, as part of our thesis project.


### Prerequisites
- Python >= 3.8
- Ollama CLI (install from [Ollama.com](https://ollama.com))

### Setup

Create a virtual environment

`python -m venv WMK`

Activate the virtual environment

`WMK\Scripts\activate`

Install the packages

`pip install -r requirements.txt`


### Experiment

##### Models

Pull a model from Ollama

`ollama pull <model_name>`

The following models used for the experiment:
- gemma3:4b
- llama3.2:3b
- qwen3:4b 
- phi3:3.8b 

Ensure the model has been pulled

`ollama list`

Start running the model

`ollama run <model_name>`

or if you want to run the model and pass the file


`type <Relative_path> | ollama run <model_name> "DIRECT ANSWERS ONLY! TRANSLATE ALL OF THESE SENTENCES TO <LANGUAGE>"`

##### Targeted Languages

The following langugaes to be translated from English:
- Bicolano
- Cebuano
- Hiligaynon
- Ilocano
- Pampangan
- Pangasinan
- Tagalog
- Waray