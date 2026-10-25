# Pneumonia Detection Using Chest X-Ray Images

## About the Project

This project is a web-based pneumonia detection application that analyzes chest X-ray images using image processing and deep learning. It uses a VGG16 model with transfer learning to classify uploaded images into pneumonia and normal categories.

The application is developed using Flask, providing a simple interface for users to upload an X-ray image and view the model's prediction.

## Features

- Upload chest X-ray images through a web interface.
- Analyze images using a trained VGG16 model.
- Display the predicted classification.
- Simple and user-friendly interface.
- Designed as a low-cost prototype for exploring accessible pneumonia screening support.

## Technologies Used

- **Python** — application logic
- **Flask** — web application framework
- **TensorFlow / Keras** — model loading and inference
- **VGG16** — transfer learning architecture
- **NumPy** — numerical operations
- **HTML and CSS** — user interface

## Project Structure

```text
pneumonia-detection/
├── app.py
├── model/
│   ├── pneumonia_vgg16.keras
│   └── vgg16_best.keras
├── static/
│   └── uploaded.jpg
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python installed on your system
- Git
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/raghulm-17/pneumonia-detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pneumonia-detection
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the Flask application:

```bash
python app.py
```

Open the local address displayed in your terminal in a web browser. In a typical Flask development setup, this is `http://127.0.0.1:5000/`.

## Model Information

The project uses VGG16 with transfer learning. The pretrained convolutional base is used to extract image features, followed by additional classification layers trained for the project's binary classification task.

The repository includes two saved Keras model files:
- `pneumonia_vgg16.keras`
- `vgg16_best.keras`

## Intended Use and Limitations

This project is an educational prototype for chest X-ray image classification. Its predictions are not a medical diagnosis and should not replace assessment by a qualified healthcare professional. The model requires further clinical validation before any real-world medical use.

## Future Improvements

- Improve input validation and error handling.
- Add model evaluation metrics and test documentation.
- Enhance the user interface and accessibility.
- Explore secure deployment options for healthcare environments.

## Author

**Raghul M**

GitHub: [raghulm-17](https://github.com/raghulm-17)

---

If you find this project useful, feel free to explore the repository and its implementation.