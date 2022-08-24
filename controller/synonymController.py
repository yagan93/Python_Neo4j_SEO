import service.synonymService as service
from flask import Blueprint, request

synonymController = Blueprint('synonymController', __name__)
parentMapping = '/synonyms'


@synonymController.route(parentMapping, methods=['GET'])
def get_synonyms():
    return service.get_synonyms_of_word(request.args.get('word'))
