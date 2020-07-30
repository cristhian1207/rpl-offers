import csv
from flask import Flask, make_response
app = Flask(__name__)

@app.route('/products')
def getProducts():
  output = ''
  with open('data/data.csv') as csv_file:
    output = make_response(csv_file.read())
    output.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    output.headers['Content-type'] = 'text/csv'
  return output
app.run()