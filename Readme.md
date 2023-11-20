# Documentation for Cricket Player Data Scraping
This documentation provides a detailed guide on how to scrape cricket player data from the ESPN Cricinfo website. The process involves using the website’s API to iterate through player data and store the player names along with the URL for their detailed stats in a CSV file named players_shorts.csv. The URLs in this file are then used to fetch the detailed stats which are stored in multiple files with the player_id as the primary key.
## URLs in the API
The following URLs are used in the API:
Player Base URL: https://www.espncricinfo.com/cricketers/
Teams Base API: https://hs-consumer-api.espncricinfo.com/v1/pages/team
Player URL by ID: https://hs-consumer-api.espncricinfo.com/v1/pages/player/home
Images Base URL: https://img1.hscicdn.com/image/upload/lsci
Player Query URL: https://hs-consumer-api.espncricinfo.com/v1/pages/player/search
CSV Files
The CSV files are saved in the following locations:  
Player Profile File: data/player_profiles.csv  
Player Batting Stats File: data/batting_stats.csv  
Player Bowling Stats File: data/bowling_stats.csv  
Player Short File: data/players_short.csv  
Teams File: data/teams.csv  
## Team Data Scraping
The team data is scraped using the teams_base_api and saved in the teams.csv file which includes the team_id.  
Player Shorts CSV File  
The players_shorts.csv file is scraped using the player_query_url and passing the following parameters and iterating through all the pages.  

params = {  
    'mode':'BOTH',  
    'page':page_num,  
    'records':records,  
    'filterActive':'false',  
    'filterTeamId': team_id,  
    'filterFormatLevel':"INTERNATIONAL",  
    'sort':'ALPHA_ASC'  j
}  

## Detailed Stats of Each Player
The detailed stats of each player are split into 3 files (player_profiles.csv, batting_stats.csv, bowling_stats.csv).
## PlayerProfile Class
The PlayerProfile class is used to store the profile information of a player. It includes attributes such as slug, id, long_name, gender, image_url, headshot_image_url, dob, dod, and country_team_id. The class also includes a static method from_json that creates a PlayerProfile object from a JSON object. The get_player_url method returns the URL of the player’s profile if the slug and id attributes are set.
## PlayerBattingFieldingStats Class
The PlayerBattingFieldingStats class is used to store the batting and fielding stats of a player. It includes attributes such as match_format, matches, innings, notouts, runs, hi_score, average, balls_faced, strike_rate, hundreds, fifties, fours, sixes, catches, and stumps.

## Running the script  
You can start scraping data by running the main.py file in the root folder.

