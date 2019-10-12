import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pandas as pd
from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///titanic.sqlite")
engine = create_engine('postgresql://postgres:postgres@localhost/Project_2')
# ("postgres://titanic.sqlite")


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route("/listings")
def listings():
    """Return a list of all passenger names"""
    listings_df = pd.read_sql("""
select lf.listing_id as Listing_ID, lf.latitude as Latitude, lf.longitude as Longituse, lf.price as Price_2018, pp.price as Price_2017,Anh.price as Price_2019
FROM listing_file lf
inner join price_prediction pp
on lf.listing_id = pp.listing_id
inner join airbnb_nyc_homes anh
on Anh.listing_id = lf.listing_id
    """, engine)
    return listings_df.to_json(orient='records')
    #jsonify()
    # return '...'



if __name__ == '__main__':
    app.run(debug=True)
