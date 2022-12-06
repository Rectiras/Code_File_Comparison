from flask import Flask
import proje
from flask import render_template

import plotly.express as px
import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
    list_file_types_number = [] #First index will be the number of python files, second one R files.
    dataframe, python_number, r_number = proje.open_files()
    list_file_names = [x[0] for x in dataframe]
    list_file_types = [x[1] for x in dataframe]
    list_file_datasets = [x[2] for x in dataframe]
    list_file_comment_numbers = [x[3] for x in dataframe]
    list_file_code_numbers = [x[4] for x in dataframe]
    list_file_libraries_number = [x[5] for x in dataframe]
    list_file_libraries = [x[6] for x in dataframe]
    list_file_types_number.append(python_number)
    list_file_types_number.append(r_number)

    return render_template("index.html", dataframe=dataframe, list_file_names=list_file_names, list_file_types=list_file_types, list_file_datasets= list_file_datasets, list_file_comment_numbers=list_file_comment_numbers, list_file_code_numbers=list_file_code_numbers, list_file_libraries_number=list_file_libraries_number, list_file_libraries=list_file_libraries, list_file_types_number=list_file_types_number)

if __name__ == "__main__":
    app.run(debug=True)