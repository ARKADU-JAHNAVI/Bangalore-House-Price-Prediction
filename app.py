from flask import Flask, render_template, request, jsonify
import util  

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('app.html')


@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    locations = util.get_location_names()  
    return jsonify({'locations': locations})

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        location = request.form['location']

        
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        return jsonify({'estimated_price': estimated_price})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    util.load_saved_artifacts()  
    app.run(debug=True)
