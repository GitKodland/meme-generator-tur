# İçe aktarma
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)


# Form sonuçları
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # seçilen resmi al
        selected_image = request.form.get("image-selector")

        # Görev #2. Metne ulaş

        # Görev #3. Metnin pozisyonuna ulaş

        # Görev #3. Metnin rengine ulaş

        return render_template(
            "index.html",
            # Seçilen resmi göster
            selected_image = selected_image,
            # Görev #2. Metni göster

            # Görev #3. Rengi göster
            
            # Görev #3. Metnin posizyonunu göster
        )
    else:
        # İlk resmi varsayılan olarak ayarlamak
        return render_template("index.html", selected_image="logo.svg")


@app.route("/static/img/<path:path>")
def serve_images(path):
    return send_from_directory("static/img", path)


app.run(debug=True)
