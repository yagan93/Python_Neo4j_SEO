from flask import Flask, request
import services
import repository

app = Flask(__name__)


@app.route('/combinations', methods=['GET'])
def get_anchor_href_combinations():
    return services.get_anchor_href_combinations(request.args.get('url'))


@app.route('/combinations/ambiguous/hrefs', methods=['GET'])
def get_href_with_ambiguous_anchors():
    return services.get_href_with_ambiguous_anchors(request.args.get('url'))


@app.route('/combinations/ambiguous/anchors', methods=['GET'])
def get_anchors_with_ambiguous_href():
    return services.get_anchors_with_ambiguous_hrefs(request.args.get('url'))


@app.route('/synonyms', methods=['GET'])
def get_synonyms():
    return services.get_synonyms_of_word(request.args.get('word'))


if __name__ == '__main__':
    app.run(debug=True)
