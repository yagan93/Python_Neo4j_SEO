import service.combinationService as service
from flask import Blueprint, request

combinationController = Blueprint('combinationController', __name__)
parentMapping = '/combinations'


@combinationController.route(parentMapping, methods=['GET'])
def get_anchor_href_combinations():
    return service.get_anchor_href_combinations(request.args.get('url'))


@combinationController.route(parentMapping + '/ambiguous/hrefs', methods=['GET'])
def get_href_with_ambiguous_anchors():
    return service.get_href_with_ambiguous_anchors(request.args.get('url'))


@combinationController.route(parentMapping + '/ambiguous/anchors', methods=['GET'])
def get_anchors_with_ambiguous_href():
    return service.get_anchors_with_ambiguous_hrefs(request.args.get('url'))
