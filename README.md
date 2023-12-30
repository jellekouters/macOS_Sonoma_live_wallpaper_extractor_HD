# macOS Sonoma live wallpaper extractor (HD)

## Overview
This repository is designed to extract and convert macOS Sonoma live wallpapers into high-resolution PNG images for independent use. There are two options: run `macOS Sonoma live wallpaper extractor_fixed_amount.py` to extract a fixed number of photos per video (default setting is 15 photos per video), or run `macOS Sonoma live wallpaper extractor_fixed_interval.py` for extracting images at regular intervals (default interval is every 15 seconds).

## How to use
- Clone this repository to your local machine. 
- Open your terminal and type: `pip install -r requirements.txt` and hit enter. All necessary libaries will be installed.
- Download your desired `.mp4` files from the provided YouTube playlist ([bit.ly/41DCAoy](http://bit.ly/41DCAoy)), using youtube-dl-gui ([youtube-dl-gui on GitHub](https://github.com/jely2002/youtube-dl-gui)). It's not necessary to download all videos; feel free to choose only those you prefer. For optimal quality, select the highest available resolution, preferably 4K. Once downloaded, add all videos to the current working directory (cwd) of the repository on your local machine.
- Modify your desired settings directly within the Python scripts (`num_frames_to_extract`) or (`interval_seconds`), and then execute either `macOS Sonoma live wallpaper extractor_fixed_amount.py` or `macOS Sonoma live wallpaper extractor_fixed_interval.py` as per your requirement.
- For each `.mp4` file, a separate folder is created containing the extracted images. Please note that the extraction process can take some time, depending on the length of the video.




