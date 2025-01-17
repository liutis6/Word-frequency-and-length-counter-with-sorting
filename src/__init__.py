from .functions import *
from .word_classes import *
import json

def run(settings_path:str = "settings.json"):
    settings = get_settings(settings_path)
    x = get_stats(settings["inputPath"], settings["lengthOrder"], settings["countOrder"])
    x.sort()
    write_output(settings["outputPath"], x)

def get_settings(settings_path):
    try:
        with open(settings_path, "r") as file:
            settings = json.load(file)
    except:
        raise FileExistsError("No settings found")
    
    return settings