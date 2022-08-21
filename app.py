
from data import test_data, Filter
from flask import Flask, render_template, redirect, url_for, send_from_directory, jsonify, request
from flask_cors import CORS


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def index():
    """запрос на выдачу таблички + простая фильтрация
    по типу больше-меньше

    Returns:
        json: табличка с ценой и весом для фронта
    """
    search_param = (request.args)
    # настройка фильтра
    f=Filter(search_param=search_param,
             data_frame=test_data)
    f.convert_args()
    output = f.filtering()
    
    return output.to_json(orient="records", lines=False)


if __name__ == "__main__":
    app.run()