import flask
from flask import request, jsonify
import face_recognition
import time
import logging, os
import uuid
# import Image

app = flask.Flask(__name__)
app.config["DEBUG"] = True

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
UPLOAD_FOLDER_UOHMAC = '{}/uploads_uohmac/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_UOHMAC'] = UPLOAD_FOLDER_UOHMAC

@app.route('/api', methods=['POST'])
def home():
   #  import pdb;pdb.set_trace()
   
   try:
      # print(request.files)
      if 'image1' in request.files:
         # print(request.files)
         for name,x in request.files.items():
            print(name)
            print(x)
            
            extension = os.path.splitext(x.filename)[1]
            millis = int(round(time.time() * 1000))
            f_name1 = str(millis)+'_1' + extension
            f_name2 = str(millis) +'_2'+ extension
            x.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name1))

         # image1 = request.files["image1"]
         # image2 = request.files["image2"]
         # image3 = request.files["image3"]
         # image4 = request.files["image4"]
         # image5 = request.files["image5"]
         # image6 = request.files["image6"]
         # image7 = request.files["image7"]
         # image8 = request.files["image8"]
         # image9 = request.files["image9"]
         # image10 = request.files["image10"]
         
         # # image1_name = images.save(image1);
         # extension = os.path.splitext(image1.filename)[1]
         # # str(uuid.uuid4())
         # millis = int(round(time.time() * 1000))
         # f_name1 = str(millis)+'_1' + extension
         # f_name2 = str(millis) +'_2'+ extension
         # image1.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name1))
         # image2.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name2))
         
      else:
         return jsonify({'success': False, 'message': 'Error', 'data': {}, 'errors': {}})

      # known_image = face_recognition.load_image_file(image1)
      # unknown_image = face_recognition.load_image_file(image2)

      # # millis = int(round(time.time() * 1000))
      # # image1.save('./received_images/'+str(millis)+'.jpg', 'JPEG')
      
      # #face_locations = face_recognition.face_locations(known_image, number_of_times_to_upsample=2)
      # #known_encoding = face_recognition.face_encodings(known_image, known_face_locations=face_locations, num_jitters=100)[0]

      # known_encoding = face_recognition.face_encodings(known_image)[0]
      # unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

      # results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.6)
      print('before results = '+str(results[0]))
   except:
      print('An ExceptionHello world!')
      results = ['false']
   
   print(results[0])
   return jsonify({'success': True, 'message': 'Error', 'data': {}, 'errors': {}})

   
   
@app.route('/api/test', methods=['POST'])
def test2():
   try:
      if 'snap_bill' in request.files:
         image1 = request.files["snap_bill"]
         
         extension = os.path.splitext(image1.filename)[1]
         millis = int(round(time.time() * 1000))
         f_name1 = str(millis)+'_1' + extension
         image1.save(os.path.join(app.config['UPLOAD_FOLDER_UOHMAC'], f_name1))
         
      else:
         return jsonify({'res':'unable to parse json'})

   except:
      print('An ExceptionHello world!')

   return jsonify({'res':'returned response'})

   
@app.route('/', methods=['GET'])
def test():
   #import pdb;pdb.set_trace()
   # image1 = request.files["image1"]
   # image2 = request.files["image2"]
   return "hello umar"
   known_image = face_recognition.load_image_file("biden.jpg")
   unknown_image = face_recognition.load_image_file("biden2.jpg")
   biden_encoding = face_recognition.face_encodings(known_image)[0]
   unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
   results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
   return str(results[0])

app.run()