# Get_Recently_Played_Spotify
Get recently played with Spotify API and store data in SQL using Python.

This script is from a personal project that I made to Data Analysis where the next objectives had to be resolved.

* Download daily your personal content about music playback and create an structured data table.
* The process must be 100% automatizate.
* What fact tables will you create and what will be the dimensional tables?
* The process can be scaleted to 10, 100, or 1000 users?

And the result was this:
![1](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/b48913ad-b9e5-4394-a7a3-35aaf13f98ef)

An script that recollect recently songs played from Spotify and collect the information in a Data Base.

Originally the script only collected data about the song, like id of the song, track name, and artist name:
![2](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/9c6f75e8-81af-4ec8-aa7e-5916bad3d708)

But I preferred to add more information to obtain better tables, adding information like the hour was played the song, the user who played the song, and his country. Getting something like this:
![3](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/eb3b6943-7f29-4fe8-a485-85db850fe6ec)

**Note:** The hour was configured in Mexico time zone, but you can also change this configuring the timestamp in the script with your preferred time zone

# How to use
1. Download the script.
2. Install the libraries if you do not have it (sqlite3, spotipy).
3. Use your Dashboard from Spotify API and turn on your local web app (If you do not have a web app, you can create one with this tutorial: https://developer.spotify.com/documentation/web-api/howtos/web-app-profile).
4. Log in the web app (localhost:8888) to connect with the profile you want to use.
5. Copy and paste your credentials from your Dashboard App (client_id, client_secret, redirect_uri).
6. Run the script, when it finish you should see this text in the console "Recently played tracks saved to (db name)", and the file will be found in the root of the script.
7. Open the file with a DGBA (Data Base Management System) and now you can see the last 50 songs played from the account at the time the script was executed, every time the script was executed, new data will be added without deleting previous data.

# Automatization of the script
If you do not want to execute manually the script, you can also automatize the script.

From Windows:
1. Create a .bat file.
2. Copy and paste the following code in the .bat file:
   @echo off
   python (Directory of the file)\(name of the script).py

   For example: 
   @echo off
   python C:\Users\user\Desktop\Recently_Played\main.py
3. Use Task Scheduler from Windows and schedule the .bat file at the desired interval.

From Unix-like:
1. Create a .sh file.
2. Copy and paste the following code in the .bat file:
   @echo off
   python (Directory of the file)\(name of the script).py

   For example: 
   @echo off
   python C:\Users\user\Desktop\Recently_Played\main.py

3. Use Cron from Unix and schedule the .sh file at the desired interval.
4. Make sure the .sh file have permissions to manage the permissions of files or directories.
   If it does not have it, you can execute the next command: "chmod +x (name of Shell Script).sh".
