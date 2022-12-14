import requests
from bs4 import BeautifulSoup
import repository
import json


def get_anchor_href_combinations(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    anchor_href_combinations = []
    for link in soup.find_all("a", href=True):
        anchor_href_combinations.append((link.getText().replace("\n", "").replace(" ", ""), link["href"]))
    repository.embed_anchor_href_combinations(anchor_href_combinations)
    return anchor_href_combinations


def get_href_with_ambiguous_anchors(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    href_anchor_dict = {}
    ambiguous_anchors = {}
    for link in soup.find_all("a", href=True):
        if link["href"] != "":
            _append_value(href_anchor_dict, link["href"], link.getText().replace("\n", "").replace(" ", ""))
    for key in href_anchor_dict:
        if isinstance(href_anchor_dict[key], list) and len(href_anchor_dict[key]) == len(set(href_anchor_dict[key])):
            ambiguous_anchors[key] = href_anchor_dict[key]
    repository.embed_ambiguous_combinations(ambiguous_anchors, 1)
    return ambiguous_anchors


def get_anchors_with_ambiguous_hrefs(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    href_anchor_dict = {}
    ambiguous_hrefs = {}
    for link in soup.find_all("a", href=True):
        anchor_tag = link.getText().replace("\n", "").replace(" ", "")
        if anchor_tag != "":
            _append_value(href_anchor_dict, anchor_tag, link["href"])
    for key in href_anchor_dict:
        if isinstance(href_anchor_dict[key], list) and len(href_anchor_dict[key]) == len(set(href_anchor_dict[key])):
            ambiguous_hrefs[key] = href_anchor_dict[key]
    repository.embed_ambiguous_combinations(ambiguous_hrefs, 0)
    return ambiguous_hrefs


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


def _append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value
