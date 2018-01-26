# citidots

## Synopsis
CitiDots is a data visualization project created by Ashneel Das and Jason Kao. It displays the movement of bikes from NYC's bike sharing system, CitiBike. Based on borrow/return timestamps and location, it predicts the path of a bike (representated by a single blue dot) and simulates actual movement. Bike station data is taken from CitiBike's database. The database includes every bike transaction at different stations. We tracked bikes by bike ID and used Google Maps' direction API to predict a travelled path. An animated dot represents every bike taken or docked.

<img src="https://github.com/ashneeldas2/citidots/blob/master/demo.gif">  

## Running the app
After cloning, simply run `python -m SimpleHTTPServer` and go to `localhost:8000`.


## Data
We used pandas to read CitiBike's .csv data and parsed through the necessary columns to write a sorted JSON file used by the simulation.js. The program is run in the terminal, with the arguments listed below.
 ```
 python parse_to_json.py [filename rows [clump]]
 ```
