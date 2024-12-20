from flask import Flask, send_from_directory
from flask_cors import CORS
import os
from flask import request, jsonify 
from flask_cors import cross_origin
from app.charts.attribute import *
from app.utils.data_parser import *

app = Flask(__name__, static_folder='./build')

CORS(app, support_credentials=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    
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
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'cusum_p':
                chart = AttributeCusumP(parsed_config, parsed_data)
                result = {
                    'type': 'cusum_p',
                    'corner': chart.get_corner_parameters(),
                    'mean': chart.get_average(),
                    'sigma': chart.get_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'cusum_c':
                chart = AttributeCusumC(parsed_config, parsed_data)
                result = {
                    'type': 'cusum_c',
                    'corner': chart.get_corner_parameters(),
                    'mean': chart.get_average(),
                    'sigma': chart.get_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'ma_p':
                chart = AttributeMovingAverageP(parsed_config, parsed_data)
                result = {
                    'type': 'ma_p',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'ma_c':
                chart = AttributeMovingAverageC(parsed_config, parsed_data)
                result = {
                    'type': 'ma_c',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'standartized_p':
                chart = AttributeStandartizedP(parsed_config, parsed_data)
                result = {
                    'type': 'standartized_p',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'standartized_c':
                chart = AttributeStandartizedC(parsed_config, parsed_data)
                result = {
                    'type': 'standartized_c',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'standartized_u':
                chart = AttributeStandartizedU(parsed_config, parsed_data)
                result = {
                    'type': 'standartized_u',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'c':
                chart = AttributeC(parsed_config, parsed_data)
                result = {
                    'type': 'c',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'u':
                chart = AttributeU(parsed_config, parsed_data)
                result = {
                    'type': 'u',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'np':
                chart = AttributeNP(parsed_config, parsed_data)
                result = {
                    'type': 'np',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }
            case 'standartized_np':
                chart = AttributeStandartizedNP(parsed_config, parsed_data)
                result = {
                    'type': 'standartized_np',
                    'mean': chart.get_average(),
                    'lcl': chart.get_lcl_ucl()[0],
                    'cl': chart.get_cl(),
                    'ucl': chart.get_lcl_ucl()[1],
                    'sigmas': chart.get_all_sigmas(),
                    'total_sigma': chart.get_total_sigma(),
                    'values': chart.values_for_plot()
                }

        return jsonify(result), 200
    
    except Exception as e:
       return jsonify({"error": str(e)}), 500