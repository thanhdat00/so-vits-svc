import streamlit as st
import os
import shutil
import subprocess
from pathlib import Path
from pydub import AudioSegment
import random

# Create directories if they don't exist
raw_folder = "raw"
results_folder = "results"

Path(raw_folder).mkdir(parents=True, exist_ok=True)
Path(results_folder).mkdir(parents=True, exist_ok=True)

st.title("Singing voice conversion")
key = st.selectbox("Dieu chinh cao do", range(0, 11))

speaker  = st.selectbox("Chon giong ca si ban thich", ['Huong ly', 'tlinh'])

speaker_mapping = {
    'Huong ly': 'huongly',
    'tlinh': 'tlinh'
}

# File uploader
uploaded_file = st.file_uploader("Tai doan nhac ban muon chuyen doi", type=["wav", "mp3", "ogg", "flac"])

if uploaded_file is not None:
    # Save the uploaded file to the raw folder
    raw_audio_path = os.path.join(raw_folder, uploaded_file.name)
    with open(raw_audio_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Audio file saved to {raw_folder} as {uploaded_file.name}")

    # Display audio player for uploaded file
    st.audio(raw_audio_path, format="audio/wav")

    # Button to start processing
    if st.button("Process Audio"):
        with st.spinner("Processing..."):
            # Simulate processing time (for demo purposes)
            # Here you should place the command you want to execute
            process_cmd = f"python3 inference_main.py -t {key} -m logs/44k/G_47200.pth -c configs/config.json -n {uploaded_file.name} -s {speaker_mapping[speaker]} -wf wav -dm logs/44k/diffusion/model_4000.pt -shd"
            print("Do : " + process_cmd)
            # Start subprocess to run the external command
            process = subprocess.Popen(process_cmd, shell=True)
            process.wait()
 
        final_file_name = f'{uploaded_file.name}_G_47200_{key}key_{speaker_mapping[speaker]}_sovdiff_pm.wav'
        # After processing, move file to results folder (assuming processing creates a result file)
        result_audio_path = os.path.join(results_folder, final_file_name)
        print(result_audio_path)
        if os.path.exists(result_audio_path):
            st.success(f"Audio processed successfully! Saved to {results_folder}")
            
            # Display audio player for processed audio
            st.audio(result_audio_path, format="audio/wav")
        else:
            st.error("Failed to process audio. Please check the command or file output.")
