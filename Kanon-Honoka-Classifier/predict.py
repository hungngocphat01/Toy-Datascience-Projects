import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import sys 
import json

from web import server

if len(sys.argv) > 1:
  input_folder = sys.argv[1]
else:
  input_folder = 'input'

if not os.path.exists(input_folder):
  print('Folder does not exist:', input_folder)

# Load model from disk
print('Loading model...')
model = tf.keras.models.load_model('honokanon_model')
class_names = ['honoka', 'kanon']

def load_and_predict(filename: str):
  # Load image to array
  image = tf.keras.utils.load_img(filename)
  image = tf.image.resize(image, (192, 192), method='area')

  # Predict
  pred_vector = model.predict(tf.expand_dims(image, 0))[0]
  pred_class = int(tf.argmax(pred_vector))
  pred_label = class_names[pred_class]
  pred_prob = '%.04f' % (pred_vector[pred_class])

  return (pred_label, pred_prob)


# Load and predict each file
print('Starting prediction...')
prediction_result = dict()

for input_filename in os.listdir(input_folder):
  filename = os.path.join(input_folder, input_filename)
  # Predict each image and write result to file
  pred_label, pred_prob = load_and_predict(filename)
  prediction_result[input_filename] = {'label': pred_label, 'prob': pred_prob}

  print(filename.ljust(30), pred_label, '\t', pred_prob)

with open('result.json', mode='w') as f:
  json.dump(prediction_result, f)

server.app.run()

