Code Uses Pi MusicBox and Mopidy as underlying apps - instructions for installation can be found here:https://helen.blog/2019/12/building-a-swipe-card-jukebox-using-a-raspberry-pi/

The Main script is read_rfid_test_csv.py - this reads the RFID card and plays the album/track/playlist
interruptpushbutton.py handles the buttons for play/pause, next track and last track
led_on.py simply turns on the LEDs on boot-up
updatelist.sh downloads the latest version of the RFID cards and albums/tracks at bootup from github. User can modify the RFID cards and albums, add new ones etc on github. 

All scripts are run at bootup:

/etc/profile runs the following: (appended to the end of the file):
sudo /root/updatelist.sh
sudo python /root/ledon.py
sudo python /root/read_rfid_test_csv.py


crontab runs the following: (again appended to the end of the file)
@reboot sudo python /root/interruptpushbutton.py &

Maybe these could all be put in /etc/profile but I had some difficulty getting things to run at bootup. This worked and I haven't bothered to try conslidate into a single location (crontab or /etc/profile)







