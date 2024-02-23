# Get_Recently_Played_Spotify
Get recently played with Spotify API and store data in SQL using Python.

This script is from a personal project that I made to Data Analysis where the next objectives had to be resolved.

* Download daily your personal content about music playback and create an structured data table.
* The process must be 100% automatizate.
* What fact tables will you create and what will be the dimensional tables?
* The process can be scaleted to 10, 100, or 1000 users?

# Script Preview
The result was this:
![1](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/b48913ad-b9e5-4394-a7a3-35aaf13f98ef)

An script that recollect recently songs played from Spotify and collect the information in a Data Base.

Originally the script only collected data about the song, like id of the song, track name, and artist name:
![2](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/9c6f75e8-81af-4ec8-aa7e-5916bad3d708)

But I preferred add more information to obtain better tables, adding information like the hour was played the song, the user who played the song, and his country. Getting something like this:
![3](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/eb3b6943-7f29-4fe8-a485-85db850fe6ec)

**Note:** The hour was configured in Mexico time zone, but you can also change this configuring the timestamp in the script with your preferred time zone.

# Fact table and Dimensional tables
With the information I have compiled, I created 3 tables in total: 1 Fact table and 2 Dimensional tables:

*Fact table*

**recently_played**

This table store principally information about songs and users, having the following data:
* track_id
* user_id
* played_at
* user_country

*Dimensional tables*

**users**

This table store information about the users that have used the script and the local server, having the following data:
* user_id
* display_name
* country

**tracks**

This table store information about the tracks have been storaged in the data base, having the following data:
* track_id
* track_name
* artist_name

With these 3 tables I made the next ERD:

![4](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/0e03303a-e4d4-4646-a47d-2370ec975194)


Finally, we can respond to the objectives declared at the beginning:
* Download daily your personal content about music playback and create an structured data table.
  
  The script get the daily content calling the service of the API Spotify and created 3 tables with this information.



* The process must be 100% automatizate.

  In the section "How to use" shown below, explains the steps to automate the script.


 
* What fact tables will you create and what will be the dimensional tables?

  3 tables were created: 1 Fact table and 2 Dimensional tables


  recently_played(Fact), users(Dimensional), tracks(Dimensional)



* The process can be scaleted to 10, 100, or 1000 users?
  Yes, it can be. At the moment only can be scalated by a few users because it works locally for the moment and if these users are connected to the local red.

  To scale it to many more users it is neccesary upload the script and the Dashboard App online to be available 24 hours and reach more users.

  
# How to use
1. Download the script.
2. Install the libraries if you do not have it (sqlite3, spotipy).
3. Use your Dashboard from Spotify API and turn on your local web app (If you do not have a web app, you can create one with this tutorial: https://developer.spotify.com/documentation/web-api/howtos/web-app-profile).
4. Log in the web app (localhost:8888) to connect with the profile you want to use.
5. Copy and paste your credentials from your Dashboard App (client_id, client_secret, redirect_uri).
   ![5](https://github.com/Alfredo2501/Get_Recently_Played_Spotify/assets/65301739/06f93824-7351-467f-a12b-0e2334d94f44)

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
