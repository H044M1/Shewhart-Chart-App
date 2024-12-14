from flask import Flask
from flask_cors import CORS
from flask import request, jsonify 
from flask_cors import cross_origin
from app.charts.attribute import *
from app.utils.data_parser import *

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/process', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*')
def process_request():
    try:
        req = request.get_json()
        if not req:
            return jsonify({"error": "Invalid JSON input"}), 400

        config = req.get('config')
        data = req.get('data')
        
        parsed_config = parse_config(config)
        parsed_data = parse_data(data)
        
        if config is None or data is None:
            return jsonify({"error": "Missing required parameters"}), 400

        match config['chart']:
            case 'p':
                chart = AttributeP(parsed_config, parsed_data)
                result = {
                    'type': 'p',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'values': chart.values_for_plot()
                }
            case 'cusum_p':
                chart = AttributeCusumP(parsed_config, parsed_data)
                result = {
                    'type': 'cusum_p',
                    'corner': chart.get_corner_parameters,
                    'mean': chart.get_average(),
                    'sigma': chart.get_sigma(),
                    'values': chart.values_for_plot()
                }

        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500