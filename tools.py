import re

def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.upper())