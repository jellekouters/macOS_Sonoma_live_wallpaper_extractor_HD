# Import the libraries
import cv2
import os
import glob
import shutil
from tqdm import tqdm
import pandas as pd
cwd = os.getcwd()

# Define the number of frames to extract per .mp4
cwd = os.getcwd()
num_frames_to_extract = 15

# Rename the downloaded .mp4 files
def rename_files(cwd):
    # Pattern to match the files
    pattern = os.path.join(cwd, "macOS Sonoma wallpaper⧸screensaver collection：*.mp4")

    for file_path in glob.glob(pattern):
        # Extract the base name of the file
        base_name = os.path.basename(file_path)

        # Split the name at the colon and strip spaces
        new_name = "macOS Sonoma wallpaper - " + base_name.split("：")[-1].strip()

        # Construct the new full file path
        new_file_path = os.path.join(cwd, new_name)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed '{base_name}' to '{new_name}'")

# Call the function with your cwd
rename_files(cwd)

# Extracts a fixed number of frames from a video file and saves them as PNG images
def extract_frames(video_path, output_folder, num_frames):
    # Create a unique folder for this video
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the video
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames in the video
    
    # Calculate the interval for extracting frames
    frame_interval = total_frames // num_frames

    # Extract video filename without extension for naming the frames
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    frame_count = 0
    extracted_count = 0
    with tqdm(total=num_frames, desc=f"Extracting frames from {video_name}", unit='frame') as pbar:
        while cap.isOpened() and extracted_count < num_frames:
            ret, frame = cap.read()

            if not ret:
                break  # Break the loop if there are no frames left

            if frame_count % frame_interval == 0 and extracted_count < num_frames:
                # Save the frame as a PNG image with video name and frame count
                frame_name = os.path.join(output_folder, f'{video_name}_{extracted_count}.png')
                cv2.imwrite(frame_name, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # 0 for no compression
                pbar.update(1)
                extracted_count += 1

            frame_count += 1

    cap.release()

# Process each .mp4 file in the directory
for video_file in glob.glob(os.path.join(cwd, '*.mp4')):
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    output_folder = os.path.join(cwd, video_name)
    extract_frames(video_file, output_folder, num_frames_to_extract)
