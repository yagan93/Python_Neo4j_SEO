import requests
from bs4 import BeautifulSoup

url = "https://github.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


def get_href_anchor_pairs():
    anchor_tags = []
    for link in soup.find_all("a", href=True):
        anchor_tags.append((link["href"], link.getText().replace("\n", "").replace(" ", "")))
    return anchor_tags


def get_href_with_ambiguous_anchor_tags():
    href_anchor_dict = {}
    ambiguous_anchors = {}
    for link in soup.find_all("a", href=True):
        if link["href"] != "":
            _append_value(href_anchor_dict, link["href"], link.getText().replace("\n", "").replace(" ", ""))
    for key in href_anchor_dict:
        if isinstance(href_anchor_dict[key], list) and len(href_anchor_dict[key]) == len(set(href_anchor_dict[key])):
            ambiguous_anchors[key] = href_anchor_dict[key]
    return ambiguous_anchors


def get_anchor_tags_with_ambiguous_href():
    href_anchor_dict = {}
    ambiguous_anchors = {}
    for link in soup.find_all("a", href=True):
        if link["href"] != "":
            _append_value(href_anchor_dict, link.getText().replace("\n", "").replace(" ", ""), link["href"])
    for key in href_anchor_dict:
        if isinstance(href_anchor_dict[key], list) and len(href_anchor_dict[key]) == len(set(href_anchor_dict[key])):
            ambiguous_anchors[key] = href_anchor_dict[key]
    return ambiguous_anchors


def _append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value


