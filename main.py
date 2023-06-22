# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form results
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # getting the selected image
        selected_image = request.form.get('image-selector')

        # Assignment #2.Receiving the text
        

        # Assignment #3. Receiving the text's positioning
       

        # Assignment #3. Receiving the text's colour
        

        return render_template('index.html', 
                               # Displaying the selected  image
                               selected_image=selected_image, 

                               # Assignment #2. Displaying the text
                               

                               # Assignment #3. Displaying the colour 
                               
                               
                               # Assignment #3. Displaying the text's positioning

                               )
    else:
        # Displaying the first image by default
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
