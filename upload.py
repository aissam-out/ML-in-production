from flask import Flask, render_template, request
# if you encounter dependency issues using 'pip install flask-uploads'
# try 'pip install Flask-Reuploaded' 
from flask_uploads import UploadSet, configure_uploads, IMAGES
from keras.preprocessing.image import load_img
# the pretrained model
from model import process_image, predict_class

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

# path for saving uploaded images
app.config['UPLOADED_PHOTOS_DEST'] = './static/img'
configure_uploads(app, photos)

# professionals have standards :p
@app.route('/home', methods=['GET', 'POST'])
def home():
    welcome = "Hello, World !"
    return welcome

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])

        image = load_img('./static/img/'+filename, target_size=(224, 224))
        image = process_image(image)
        prediction, percentage = predict_class(image)

        answer = "For {} : <br>The prediction is : {} <br>With probability = {}".format(filename, prediction, percentage)
        return answer
    return render_template('upload.html')


if __name__ == '__main__':
	#app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
