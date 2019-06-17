import json
from flask import request, jsonify, Blueprint, abort, Flask
from flask.views import MethodView
from spacy_ner import ner_controller

app = Flask(__name__)

ner = ner_controller()
model = ner.create_model()

class NerAPI(MethodView):
 
    def get(self):
        return jsonify({'':''})
 
    def post(self):
        data = request.get_json(force=True)
        doc = model(data['text'])
        entities = [str(ent) for ent in doc.ents]
        return jsonify({'results':entities})
        

app.add_url_rule('/api', view_func=NerAPI.as_view('ner_api'), methods=['GET', 'POST'])

if __name__ == '__main__':
    pass

app.run(debug=False)