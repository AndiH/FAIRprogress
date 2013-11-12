# FAIRprogress

The scripts retrieve the FAIR construction site webcam's picture every 15 minutes and save them into a date-based folder structure. Every night, a GIF* is generated from the images of the previous day and displayed on the website.  
(* = Actually, two GIFs are generated: One high-res and one low-res.)

ImageMagick's `convert` is used to generated the animated GIFs from the static JPGs.

## Files
  * `getPicture.sh` - Downloads the webcam picture and, if needed, creates the corresponding folder to put it into.
  * `createGIFs.sh` - Generates the two GIFs from all JPGs in 'yesterday's folder and copies it to the display location, deleting the GIF from the day before yesterday lying there up to now.

## Todo & Ideas
  * Create monthly GIFs
  * Tidy up code
