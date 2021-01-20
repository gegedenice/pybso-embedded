#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, render_template,url_for,request
from flask_caching import Cache
import pandas as pd
import plotly
import json
import pybso.charts as charts

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)
cache.init_app(app)

app.config.from_object('config')
port = app.config['PORT']

#util for using zip in html template
app.jinja_env.globals.update(zip=zip)

df = pd.read_csv("static/data/data.csv",sep = ',',encoding="utf-8")
functions_fig = [charts.oa_rate,charts.oa_rate_by_year,charts.oa_rate_by_publisher,charts.oa_rate_by_type,charts.oa_by_status]
functions_str = ["oa_rate","oa_rate_by_year","oa_rate_by_publisher","oa_rate_by_type","oa_by_status"]

#routing for page
@app.route('/')
def homePage():
    graphsJSON = [json.dumps(f(dataframe=df), cls=plotly.utils.PlotlyJSONEncoder) for f in functions_fig]
    #functions_str = map( lambda x: x.replace( 'charts.', ''), functions_fig)
    return render_template('home.html',functions=functions_str,plots=graphsJSON)

#routing for data API
@app.route('/api/data', methods = ['GET'])
@cache.cached(timeout=50)
def publis(): 
    if 'view' in request.args:
        if request.args.get('view') == "oa_rate":
            records= pd.crosstab(df["is_oa_normalized"], df["oa_host_type_normalized"])
        if request.args.get('view') == "oa_rate_by_year":
            records= pd.crosstab(df["year"], df["oa_host_type_normalized"])
        if request.args.get('view') == "oa_rate_by_publisher":
            records= pd.crosstab(df["publisher"], df["oa_host_type_normalized"])
        if request.args.get('view') == "oa_rate_by_type":
            records= pd.crosstab(df["genre"], df["oa_host_type_normalized"])
        if request.args.get('view') == "oa_by_status":
            records= pd.crosstab(df["year"], df["oa_status_normalized"])
    else:
        records = df
    return jsonify(records.fillna('').to_dict(orient='index'))

if __name__ == '__main__':
    app.run(debug=True,port=port)  