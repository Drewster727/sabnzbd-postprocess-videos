# sabnzbd-postprocess-videos
Post-processing videos and related files to provide you with a cleaner end-result

## This post-processing script does the following
* Flattens the contents
 * Sometimes people embed video and other file types in a crazy folder structure, first we flatten this out so we can process everything.
* Removes files smaller than 60MB
 * This is of course an arbitrary number I chose based on experience, anything smaller than that is typically NOT something we need.
* Attempts to fix obfuscated video file names 
 * Only works with downloads that contain a single video file, i.e. it won't work with TV seasons or multi-part movie downloads. In other words, there can only be one primary video file in the folder to be processed for this to work.
* Removes Title and Comments metadata
 * This is done to avoid media libraries like Plex reading from the metadata as opposed to file name. In my experience, Plex has read a file's metadata title and used that in the library as opposed to parsing the file name. This has caused some wild names to appear in my library.

## Dependencies
* python (tested with 2.7.x)
* ffmpeg (for metadata removal)

### Note: This script will remove subtitle files due to their small size. I personally do not use sub files and prefer hard subs embedded in my videos.
