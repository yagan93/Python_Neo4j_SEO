from flask import Flask, request
import services
import db


app = Flask(__name__)


@app.route('/pairs', methods=['GET'])
def get_href_anchor_pairs():
    return services.get_href_anchor_pairs(request.args.get('url'))


@app.route('/ambiguousHref', methods=['GET'])
def get_href_with_ambiguous_anchor_tags():
    return services.get_href_with_ambiguous_anchor_tags(request.args.get('url'))


@app.route('/ambiguousAnchorTags', methods=['GET'])
def get_anchor_tags_with_ambiguous_href():
    return services.get_anchor_tags_with_ambiguous_href(request.args.get('url'))


@app.route('/embedding', methods=['POST'])
def graph_embedding():
    return db.graph_embedding(services.get_anchor_tags_with_ambiguous_href(request.args.get('url')))


if __name__ == '__main__':
    app.run(debug=True)
