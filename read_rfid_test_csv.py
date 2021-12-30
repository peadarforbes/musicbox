#!/usr/bin/python

#This scrip enters into a while loop waiting for an RFID card to be tapped. Once tapped it matches the RFID card number to a spotify playlist or album and plays that album
#This script is run on bootup in /etc/profile

import os
import subprocess #Needed to translate mopidy bash commands for use in python
import csv #Needed to work with csv files

subprocess.call(["mpc", "clear"]) # Clears whatever is already playing (in case I manually played something during debug)



while 1: #While loop waiting for an RFIC card to be tapped
	card_number = raw_input("Tap Card"); #Takes input from command line of card tapped
	print ('Card Number is: ', card_number);
	subprocess.call(["mpc", "clear"]) #A card has been tapped. Clear the previous playlist
	
	#read csv, and split on "," the line
	csv_file = csv.reader(open('spotify_listtest.csv', "r"), delimiter=",")

#Because playlists are not currently supported, these need to be handled manually. Next lines store the playlist as variables
#First Playlist	
	playlistone = ('0004169296') # This is the card number for "playlistone"
	rocketman_uri = ('spotify:track:3gdewACMIVMEWVbyb8O9sY') # These are the spotify URIs for each song in the playlist
	wagonwheel_uri = ('spotify:track:359krpyCKcFF8SFvqWES9L')
	neverrains_uri = ('spotify:track:6tunhVGD8C05MZNjSVIsjw')
	folsomprison_uri = ('spotify:track:0LTSNmOLBt25GMjHlxp9OR')
	fieldsgold_uri = ('spotify:track:0I1DJdLt9BKOb7GWmWxCjo')
	westawake_uri = ('spotify:track:3icfTVaCWTksAXwyYEFKC5')
	westawakeinst_uri = ('spotify:track:3WAzk6lsNVu75wxWgzjsu5')

#Second Playlist
	discoplaylist = ('0004169289')
	shakeitup_uri = ('spotify:track:0cqRj7pUJDkTCEsJkx8snD')
	watermelon_uri = ('spotify:track:6UelLqGlWMcVH1E5c4H7lY')

#Third Playlist
	laurieberknerband = ('0004168734')
	laurieberknerband_uri = ('spotify:album:4XbuNhXriszF4L1V4mYBfV')
	goldfish_uri = ('spotify:track:601M9QaiJ2Kmx0h0qaMwXx')


#Next check if the card number tapped is one of the playlists, or alternativly search for the card number in the "spotify_listtest.csv" file
#The file is downloaded on reboot from github via the "updatelist.sh" script which is run in /etc/profile
	if card_number == discoplaylist:
                print('You tapped Discoplaylist!')
                subprocess.call(["mpc", "add", shakeitup_uri]) #adds a song to the playlist
                subprocess.call(["mpc", "add", watermelon_uri])
		subprocess.call(["mpc", "play"]) # plays the playlist
 	elif card_number == laurieberknerband:
                print('You tapped Laurie Berkner!')
                subprocess.call(["mpc", "add", goldfish_uri])
                subprocess.call(["mpc", "add", laurieberknerband_uri])
		subprocess.call(["mpc", "play"])
	elif card_number == playlistone:
                print('You tapped PlayList 1!')
                subprocess.call(["mpc", "add", wagonwheel_uri])
		subprocess.call(["mpc", "add", rocketman_uri])
		subprocess.call(["mpc", "add", neverrains_uri])
		subprocess.call(["mpc", "add", fieldsgold_uri])
		subprocess.call(["mpc", "add", westawake_uri])
		subprocess.call(["mpc", "add", westawakeinst_uri])
		subprocess.call(["mpc", "add", folsomprison_uri])
                subprocess.call(["mpc", "play"])
	else:
		#loop through the csv list
		for row in csv_file:
    		#if current rows 1st  value (0) is equal to card number, print that row and then add the spotify uri stored in row[1] to play
    			if card_number == row[0]:
        			print (row)
        			print (row[1])
        			subprocess.call(["mpc", "add", row[1]]) #adds the spotify URI corresponding the card_number to the playlist
        			subprocess.call(["mpc", "play"]) # plays the playlist


