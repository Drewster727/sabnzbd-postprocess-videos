# sabnzbd-postprocess-videos
Post-processing videos and related files to provide you with a cleaner end-result

## This post-processing script does the following
- Removes files smaller than 60MB
- Attempts to fix obfuscated video file names (
-- only works with downloads that contain a single video file, i.e. it won't work with TV seasons or multi-part movies)
- Removes Title and Comments metadata (this is done to avoid media libraries like Plex reading from the metadata as opposed to file name)
