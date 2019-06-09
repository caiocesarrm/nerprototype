import json
from flask import request, jsonify, Blueprint, abort, Flask
from flask.views import MethodView
 
app = Flask(__name__)


class NerAPI(MethodView):
 
    def get(self):
        return jsonify({'teste1':'teste2'})
 
    def post(self):
        return {"message": "teste"}
        

app.add_url_rule('/api', view_func=NerAPI.as_view('ner_api'), methods=['GET', 'POST'])

if __name__ == '__main__':
    pass

app.run(debug=False)