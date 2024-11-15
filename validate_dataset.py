import os
from pydub import AudioSegment

# Define the folder where your audio files are located
folder_path = "tlinh_chunk/"  # Replace with your folder path

# Set the minimum length (in milliseconds)
min_length_ms = 2 * 1000  # 4 seconds in milliseconds
max_length_ms = 13 * 1000
sum = 0

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, filename)
    # Check if the file is an audio file (you can add more extensions if needed)
    if filename.endswith(".wav") or filename.endswith(".mp3"):
        try:
            # Load the audio file
            audio = AudioSegment.from_file(file_path)

            # Check the duration of the audio file
            if len(audio) < min_length_ms:
                print(f"Deleting {filename} - duration {len(audio)/1000:.2f} seconds")
                # Delete the file if it's shorter than 3 seconds
                os.remove(file_path)
                sum += 1
            if len(audio) > max_length_ms:
                print(f"Deleting {filename} - duration {len(audio)/1000:.2f} seconds")
                # Delete the file if it's shorter than 3 seconds
                os.remove(file_path)
                sum += 1
            # else:
                # print(f"Keeping {filename} - duration {len(audio)/1000:.2f} seconds")
        except Exception as e:
            print(f"Could not process file {filename}: {e}")

print("Process complete.")
print(f'Delete {sum} file')
