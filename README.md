# bubbleao

working from standard yocto build on Edison
make sure pip is upto date on edison
> sudo pip install --upgrade pip

download and setup tweepy in root
> pip install tweepy

(note tweepy at https://github.com/tweepy/tweepy)

clone bubbleao repo onto root of edison

> git clone https://github.com/djdunc/bubbleao.git bubbeao

To set up Bubbleao you need to edit your twitter API settings and rename the sample file to settings.py

To change the hashtags being watched edit the hastags.txt file to create a comma seperated list of hashtags

Bubbleao currently setup to switch relay on pin 3 for 10 seconds when a hashtag is observed in stream. Bubbleao sheild also has option for driving an RGB led on pins: 
R = 5 
G = 9
B = 6