A list of scripts that I wrote for personal use. These are particularly tailored to my needs and often come with no documentation, but may be of inspiration to some of you.

#### Bash
- [count.sh](https://github.com/fexed/scripts/blob/main/bash/count.sh) is a script that enumerates files in the current dir with a depth of 2 and lists how many files are in each directory. I use this to see how many photo I take each month, so I run in a directory with a three sort of like this:
```
  .
  |- 2020
  |   |- 01_Gennaio
  |   |- 02_Febbraio
  |   | ...
  |
  ...
```
Getting an output like
```
.                   67040
./2020              11589
./2020/01_Gennaio   418
./2020/02_Febbraio  156
...
```
I use this in a more CSV format, import to a spreadsheet and make some graphs
![image](https://github.com/fexed/scripts/assets/5090316/f2a23625-b2c5-46ed-9da4-82d44a3d6d6c)

- [diskstats.sh](https://github.com/fexed/scripts/blob/main/bash/diskstats.sh) gathers data from the disks on my home server and puts in some easy-to-reach files, which I then use to plot the available space on the landing page of my personal home server.

#### Python

- [photohandler.py](https://github.com/fexed/scripts/blob/main/python/photohandler.py) runs each time I send a photo to my Telegram bot, placing it in my photo directory tree in the right folder. For example, a photo named `PXL_20231026_105444.jpg` will be placed inside `photos/2023/10_Ottobre/20231026/`
- [photo_tiles.py](https://github.com/fexed/scripts/blob/main/python/photo_tiles.py) produces a grid of tiles like GitHub's contributions per month, based on an hardcoded dataset. Example below
![photos](https://github.com/fexed/scripts/assets/5090316/ea14e053-6303-4566-aa14-1aaaf0c173f7)
- [piwigo/piwigo_fixer.py](https://github.com/fexed/scripts/blob/main/python/piwigo/piwigo_fixer.py) fixes the missing creation dates of my piwigo database, filling with the date corresponding to the parent folder. E.g., the previous photo would be assigned a creation date of October 26, 2023.
- [piwigo/piwigo_howmanywithouttag.py](https://github.com/fexed/scripts/blob/main/python/piwigo/piwigo_howmanywithouttag.py) prints the number of photos in my piwigo database that have no tag
- [piwigo/piwigo_randomwithouttag.py](https://github.com/fexed/scripts/blob/main/python/piwigo/piwigo_randomwithouttag.py) prints the absolute path of a photo with no tag from my piwigo database

