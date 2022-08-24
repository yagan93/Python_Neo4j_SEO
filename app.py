from flask import Flask
from controller.combinationController import combinationController
from controller.synonymController import synonymController

app = Flask(__name__)
app.register_blueprint(combinationController)
app.register_blueprint(synonymController)

if __name__ == '__main__':
    app.run(debug=True)