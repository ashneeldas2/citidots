# citidots

## Synopsis
CitiDots is a data visualization project created by Ashneel Das and Jason Kao. It displays the movement of bikes from NYC's bike sharing system, CitiBike. Based on borrow/return timestamps and location, it predictes the path of a dot (representative of one bike) and simulates actual bike movement. Below is a preview of our project dated November 23, 2016.  
<img src="https://github.com/ashneeldas2/citidots/blob/master/records/record-112316.gif">  

## Data
We used pandas to read CitiBike's .csv data and parsed through the necessary columns to write a sorted JSON file used by the simulation.js. The program is run in the terminal, with the arguments listed below.
 ```
 python parse_to_json.py [filename rows [clump]]
 ```
