from flask import Flask
import services


app = Flask(__name__)


@app.route('/pairs', methods=['GET'])
def get_href_anchor_pairs():
    return services.get_href_anchor_pairs()


@app.route('/ambiguousHref', methods=['GET'])
def get_href_with_ambiguous_anchor_tags():
    return services.get_href_with_ambiguous_anchor_tags()


@app.route('/ambiguousAnchorTags', methods=['GET'])
def get_anchor_tags_with_ambiguous_href():
    return services.get_anchor_tags_with_ambiguous_href()


if __name__ == '__main__':
    app.run(debug=True)
