# İçe Aktarma
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Formun sonuçları
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen görüntüyü almak
        selected_image = request.form.get('image-selector')

        # Ödev 2. Metni almak
        

        # Ödev #3. Metnin konumunu alma
       

        # Ödev #3. Metnin rengini alma
        

        return render_template('index.html', 
                               # Seçilen resmin görüntülenmesi
                               selected_image=selected_image, 

                               # Ödev #2. metni görüntüleme
                               

                               # Ödev #3. rengin gösterilmesi
                               
                               
                               # Ödev #3. Metnin konumunu görüntüleme

                               )
    else:
        # Varsayılan olarak ilk resmin görüntülenmesi
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
