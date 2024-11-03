## Video Captioning with Streamlit

This project provides a user-friendly web application for generating captions for your videos. 

**Here's a breakdown of the functionalities:**

* **Upload a Video:** You can upload a video file in various formats like mp4, mov, avi, and mkv.
* **Select Target Language (Optional):** Choose the language you want the captions to be displayed in. Currently, the app supports English, Chinese, French, German, Hindi, Italian, Malayalam, Marathi, and Spanish. (More languages can be added)
* **Generate Captions:** Once you upload a video and select the language (if desired), the app automatically extracts the audio, transcribes the speech using Whisper, and translates it to the chosen language (if applicable). The generated captions are saved in an SRT file.
* **Watch Video with Captions:** The app displays the uploaded video alongside the generated captions in a synchronized manner. The captions are displayed in a styled scrollable div for easy reading.
* **Reset and Upload Again:** If you want to caption a new video, you can click the "Upload Another Video" button. This will clear the current session and allow you to start over.

**Screenshots:**

![image](https://github.com/user-attachments/assets/3f5bd16b-2f5e-4c35-8e00-af725a50ec03)

![image](https://github.com/user-attachments/assets/696f9fa2-331e-43f4-871f-5202ee9261c4)

## Getting Started

To run this application, follow these steps:

1. **Install dependencies:** Open a terminal in your project directory and run the following command:

   ```bash
   pip install -r requirements.txt
   pip install git+https://github.com/openai/whisper.git
   ```

   This will install all the necessary libraries like Streamlit, moviepy, Whisper, srt, and deep_translator.

2. **Run the app:** Execute the following command in your terminal:

   ```bash
   streamlit run app.py
   ```

   This will launch the Streamlit app in your web browser, typically at http://localhost:8501.

**Additional Notes:**

* This app utilizes the Whisper model for audio transcription. Whisper is a powerful model by OpenAI, but it might require additional setup depending on your system. Refer to the Whisper documentation for more details: [https://platform.openai.com/docs/models/whisper](https://platform.openai.com/docs/models/whisper)
* The code utilizes `deep_translator` for translation. This library uses Google Translate for language conversion. Ensure you have a stable internet connection for translation functionality.
