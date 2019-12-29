# ImageWatch
## Description

ImageWatch displays a group of images in a window and refreshes whenever they change. It's intended for watching graphs, plots, and machine learning output update in real-time.

## Install
Requirements:

* Python 3 (pygame)

```
pip3 install -r requirements.txt
```

## Usage
```
usage: imagewatch.py [-h] [--caption CAPTION] [--nrow NROW] [--fps FPS] images

positional arguments:
  images                glob pathname

optional arguments:
  -h, --help            show this help message and exit
  --caption CAPTION, -c CAPTION
                        window caption
  --nrow NROW, -n NROW  number of images per row
  --fps FPS, -f FPS     update framerate
```