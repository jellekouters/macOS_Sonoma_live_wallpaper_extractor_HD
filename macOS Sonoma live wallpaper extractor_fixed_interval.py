# Import the libraries
import cv2
import os
import glob
import shutil
from tqdm import tqdm
cwd = os.getcwd()

# Define the interval in seconds for frame extraction
interval_seconds = 15

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

# Function to extract frames from a video file
def extract_frames(video_path, output_folder, interval_seconds):
    # Create a unique folder for this video
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the video
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frame rate of the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames in the video
    frame_interval = int(fps * interval_seconds)  # Calculate the interval in terms of frames

    # Extract video filename without extension for naming the frames
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    frame_count = 0
    with tqdm(total=total_frames // frame_interval, desc=f"Extracting frames from {video_name}", unit='frame') as pbar:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break  # Break the loop if there are no frames left

            if frame_count % frame_interval == 0:
                # Save the frame as a PNG image with video name and frame count
                frame_name = os.path.join(output_folder, f'{video_name}_frame_{frame_count}.png')
                cv2.imwrite(frame_name, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # 0 for no compression
                pbar.update(1)

            frame_count += 1

    cap.release()

# Process each .mp4 file in the directory
for video_file in glob.glob(os.path.join(cwd, '*.mp4')):
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    output_folder = os.path.join(cwd, video_name)
    extract_frames(video_file, output_folder, interval_seconds)
