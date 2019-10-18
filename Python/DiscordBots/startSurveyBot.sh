#!/bin/bash

echo "Preparing to start SurveyBot.py..."
#Stop the bot if it is running
pkill -f 'SurveyBot.py'

#Wait for 1 min
sleep 1m

#Start the bot back up
python3 /home/matt/Documents/Programming/ACM-Projects/Python/DiscordBots/SurveyBot.py
echo "Started SurveyBoy.py"
