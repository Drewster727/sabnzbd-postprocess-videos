# sabnzbd-postprocess-videos
Post-processing videos and related files to provide you with a cleaner end-result

## This post-processing script does the following
* Flattens the contents
  - Sometimes uploaders embed video and other file types in a crazy folder structure, first we flatten this out so we can process everything.
* Removes files smaller than 60MB
  - This is of course an arbitrary number I chose based on experience, anything smaller than that is typically NOT something we need.
* Attempts to fix obfuscated video file names 
  - Only works with downloads that contain a single video file, i.e. it won't work with TV seasons or multi-part movie downloads. In other words, there can only be one primary video file in the folder to be processed for this to work.
* Removes Title and Comments metadata
  - This is done to avoid media libraries like Plex reading from the metadata as opposed to file name. In my experience, Plex has read a file's metadata title and used that in the library as opposed to parsing the file name. This has caused some wild names to appear in my library.

## Dependencies
* python (tested with 2.7.x)
* ffmpeg (for metadata removal)

## SABnzbd Configuration
1. Set a scripts folder under: Settings > Folders > Scripts folder

![image](https://cloud.githubusercontent.com/assets/4528753/23218188/36b603e8-f8e1-11e6-9d47-2a148701954f.png)

2. Drop the script into the folder you set and make sure sabnzbd has rights (Linux: sudo chmod +x process_videos.py)
3. Set the script to run for certain categories under: Settings > Categories (i.e. TV or Movies or any other video categories you might have)

![image](https://cloud.githubusercontent.com/assets/4528753/23218265/6fe5a5d8-f8e1-11e6-8f75-8b9567343287.png)

### Note: This script will remove subtitle files due to their small size. I personally do not use sub files and prefer hard subs embedded in my videos.
