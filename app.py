import streamlit as st
import os
from utils import extract_audio, transcribe_audio_to_srt, save_uploaded_file

st.set_page_config(page_title="Video Captioning", layout="wide", initial_sidebar_state="collapsed")

# Paths for uploaded files and generated captions
VIDEO_DIR = "static/video/"
SRT_FILE = "static/video/captions.srt"
os.makedirs(VIDEO_DIR, exist_ok=True)

# Initialize session states if not already set
if "uploaded_video_path" not in st.session_state:
    st.session_state["uploaded_video_path"] = None
    st.session_state["generated_srt"] = False

# Screen 1: Video upload
if not st.session_state["uploaded_video_path"]:
    # Add a file uploader for the video
    st.title("Upload a Video File")
    # Add a dropdown for selecting target language
    target_language = st.selectbox("Select Target Language", ["English : en",
                                                              "Chinese : zh",
                                                              "French : fr",
                                                              "German : de",
                                                              "Hindi : hi",
                                                              "Italian : it",
                                                              "Malayalam : ml",
                                                              "Marathi : mr",
                                                              "Spanish : es"])  # Add more languages as needed
    video_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi", "mkv"])
    
    # When transcribing, pass the selected target language
    if video_file is not None:
        uploaded_video_path = save_uploaded_file(video_file, VIDEO_DIR)
        st.session_state["uploaded_video_path"] = uploaded_video_path

        # Extract audio and transcribe to generate SRT with translation
        audio_path = extract_audio(uploaded_video_path)
        transcribe_audio_to_srt(audio_path, SRT_FILE, target_language[-2:])
        st.session_state["generated_srt"] = True
        
        # Simulate rerun by updating query params (Use experimental function for now)
        st.experimental_set_query_params(rerun="1")  # Replace with st.set_query_params when supported

# Screen 2: Video with Captions on the Right
if st.session_state["uploaded_video_path"] and st.session_state["generated_srt"]:
    st.title("Video Playback with Captions")
    
    # Create two columns: left for the video, right for the captions
    col1, col2 = st.columns([1, 1])  # Adjust column ratio if needed
    
    # Display the video in the left column with a smaller width
    with col1:
        st.video(st.session_state["uploaded_video_path"], start_time=0, format="video/mp4")  # Adjust width as desired
    
    # Display the captions in the right column using a styled scrollable div
    with col2:
        with open(SRT_FILE, "r", encoding='utf-8') as srt_file:
            lines = srt_file.readlines()

        # Prepare formatted captions without numbering
        formatted_captions = ""
        for line in lines:
            # Split line into timing and text
            if '-->' in line:
                # Style for the timing
                formatted_captions += f'<span style="color: blue; font-size: 14px; font-weight: bold">{line.strip()}</span><br>'
            elif line.strip():  # Only non-empty lines for captions
                # Style for the text
                formatted_captions += f'<span style="color: black; font-size: 16px;">{line.strip()}</span><br>'
        
        # Display the captions in a styled scrollable div
        st.markdown(
            f"""
            <div style="height: 400px; overflow-y: scroll; border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
                {formatted_captions}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Reset button to start over
    if st.button("Upload Another Video"):
        st.session_state["uploaded_video_path"] = None
        st.session_state["generated_srt"] = False
        st.experimental_set_query_params(rerun="1")  # Replace with st.set_query_params when supported