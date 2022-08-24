import requests
import json


def get_synonyms_of_word(word):
    synonyms_of_word = []
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    if response.status_code == 200:
        for part_of_speech in json.loads(response.content):
            for meaning in part_of_speech['meanings']:
                synonyms = meaning['synonyms']
                if not isinstance(synonyms, list):
                    synonyms_of_word.append(synonyms)
                else:
                    for synonym in synonyms:
                        synonyms_of_word.append(synonym)
    return synonyms_of_word
