from cmath import log
from flask import Flask
import sys

from housing.logger import logging  
from housing.exception import HousingException

app= Flask(__name__)


@app.route("/", methods = ["GET","POST"])
def index():
    try:
        #raise Exception("we are testing custom exception")
        logging.info("first logger")
    except Exception as e :
        housing = HousingException(e,sys)
        logging.info(housing.error_message)

    
    return "Starting first machine learning project"

if __name__=="__main__":
    app.run(debug=True)