# discord-minesweeper
## setup

- make sure you have the requests library ```py -m pip install requests```
- put your discord token in ```token``` variable. [(how to get a discord token)](https://pcstrike.com/how-to-get-discord-token/)
- run script ```py dc_minesweeper.py```

every 20 minutes the script will make a new map

you can change map size and mine count with these variables: ```width```, ```height```, ```mines```<br>
but keep in mind that discord allows only 190 characters in a bio

every field has 5 characters (```||③||```), and new line (```\n```) counts as one character
