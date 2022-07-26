from flask import Flask, request
import sys
from housing.logger import logging
from housing.exception import HousingException
app=Flask(__name__)

#Route for home page
@app.route('/', methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    return "CI/CD pipe line is established"


if __name__=="__main__":
    app.run(debug=True)