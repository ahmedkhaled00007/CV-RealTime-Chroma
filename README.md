# 🎥 Green Screen Effect using OpenCV

This project demonstrates a **real-time green screen (chroma key) effect** using **Python** and **OpenCV**.  
It captures a background image from your webcam, then replaces **green-colored regions** in the live video feed with the captured background.

---

## 📌 Features
- Real-time webcam video processing
- Automatic background capture after 3 seconds
- Green color detection using HSV color space
- Noise removal using morphological operations
- Foreground and background blending
- Fixed output size (**500 × 500**)

---

## 🛠️ Requirements

### Python Version
- Python **3.8 or higher**


# ▶️ How It Works
The webcam opens and waits 3 seconds.

A background frame is captured and saved.

Each frame is resized to 500 × 500.

Frames are converted from BGR → HSV.

Green areas are detected using an HSV mask.

Green pixels are replaced with the captured background.

The final composited frame is displayed in real time.

# ▶️ How to Run
bash
Copy code
python green_screen.py
Press q to exit the application.

# 📷 Tips for Best Results
Use a solid green background

Avoid shadows and uneven lighting

Do not wear green clothes

Use good camera quality

# 🧠 Concepts Used
OpenCV VideoCapture

HSV color space

Color masking

Morphological operations (Open & Close)

Bitwise image operations

# 📂 Project Structure
text
Copy code
```
.
├── green_screen.py
├── requirements.txt
└── README.md
```
# 🚀 Future Improvements
Adjustable HSV range with trackbars

Custom background image or video

Edge smoothing and blur

GUI controls
