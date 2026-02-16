Apart from meddling with a development drupal installation, tonight I finally got around to tweaking the shell script I wrote to update podcasts on my MP3 player. The script does the following;

Run "PodRacer" (downloads new podcast episodes)

Clean out any podcast files older than 14 days

Copy new files to the portable device

Here's the script

echo Moving to home directory...

cd ~

echo Executing Podracer...

podracer

echo Removing old files from laptop

find ~/podcasts* -mtime +14 -exec rm -fr {} ;

echo Removing old files from mobile device

find /media/0123-4567/podcasts/* -mtime +14 -exec rm -fr {} ;

echo Removing empty directories from laptop

find ~/podcasts/* -type d -empty -exec rmdir {} ;

echo Removing empty directories from mobile device

find /media/0123-4567/podcasts/* -type d -empty -exec rmdir {} ;

echo Copying from laptop to mobile device

cp -fru ~/podcasts /media/0123-4567