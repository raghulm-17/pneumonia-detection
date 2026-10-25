from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the best model
model = load_model("model/vgg16_best.keras")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]
    filepath = os.path.join("static", "uploaded.jpg")
    file.save(filepath)

    # Preprocess for VGG16
    img = image.load_img(filepath, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    prediction = model.predict(img)[0][0]
    result = "Pneumonia Detected" if prediction > 0.5 else "Normal"

    return render_template("result.html", result=result, img_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)
