# FAIRprogress

The scripts retrieve the FAIR construction site webcam's picture every 15 minutes and save them into a date-based folder structure. Every night, a GIF* is generated from the images of the previous day and displayed on http://fair.andreasherten.de/.  
(* = Actually, two GIFs are generated: One high-res and one low-res.)

ImageMagick's `convert` is used to generated the animated GIFs from the static JPGs.

## Files
  * `getPicture.sh` — Downloads the webcam picture and, if needed, creates the corresponding folder to put it into.
  * `createGIFs.sh` — Generates the two GIFs from all JPGs in 'yesterday's folder and copies it to the display location, deleting the GIF from the day before yesterday lying there up to now.
  * `monthly.sh` — Non (properly)-working idea of a monthly GIF generating script. Might be useful for the information of how to create the first frame with ImageMagick.
  * `/site/` — `index.php` which runs http://fair.andreasherten.de, it's CSS (`style.css`) and the CSS (`style.dirlist.css`) for the directory listing PHP script (not commited).

## Cronjobs
The cronjobs, which run the scripts, are:
```
*/15 * * * * /absolute/path/to/getPicture.sh
0 3 * * * /absolute/path/to/createGIFs.sh
```

## Todo & Ideas
  * Create monthly GIFs
  * Tidy up code
