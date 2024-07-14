from flask import Flask, jsonify, request,render_template,redirect, url_for
from flask_restful import Api, Resource,reqparse
from model import pre

app = Flask(__name__)
api = Api(app)

class Detect(Resource):
    '''
    Predict endpoint pipline 
    '''
    
    def post(self):
        '''
        Post method for processing and redict to the diplay url and the input 
        from the pred url 
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('src', type=str, required=True,location='form')
        args = parser.parse_args()
        data = args['src']
        '''
        model pipline is from the model.py
        '''
        model = pre() 
        out = model.pred(data)

        return redirect(url_for('display', prediction=out)) 
    
@app.route('/pred')
def index():
    '''
    intial html render 
    '''
    return render_template('index.html')
@app.route('/display')
def display():
    '''
    final html render
    '''
    prediction = request.args.get('prediction')
    return render_template('index.html', prediction=prediction)

api.add_resource(Detect, '/pred',endpoint="Detect")

if __name__=="__main__":
    app.run(debug=True)