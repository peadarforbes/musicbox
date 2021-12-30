#!/bin/bash

#This script downloads the latest list of card numbers and albums from github. First it backs up the previous version
echo "Updating Spotify List"

cp spotify_listtest.csv spotify_listtest.csv_old
rm spotify_listtest.csv
wget https://raw.githubusercontent.com/peadarforbes/musicbox/main/spotify_listtest.csv

