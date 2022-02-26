import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def get_index():
  # Read result file
  with open('result.json') as f:
    pred_result = f.read()
  pred_result = json.loads(pred_result)

  return render_template('index.html', result=pred_result)

@app.route('/image/<path:filename>')
def get_image(filename):
  return send_from_directory(
    '../input', filename
  )