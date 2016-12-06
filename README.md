# citidots

## Synopsis
citidots is a data visualization project created by Ashneel Das and Jason Kao. It displays the movement of bikes from NYC's bike sharing system, CitiBike. Based on borrow/return timestamps and location, it predictes the path of a dot (representative of one bike) and simulates actual bike movement. Below is a preview of our project dated November 23, 2016.
<video width="320" height="240" controls>
  <source src="img/11-23-16.mov" type="video/mp4">
</video>2
<img src="https://github.com/ashneeldas2/citidots/img/hi.jpg">
The purpose of this experiment is to be able to simulate crowdedness with machine learning.
The project is based on published dock station data taken from CitiBike's database.

## Motivation


## Process
We used pandas to read CitiBike's .csv data and parsed through the necessary columns to write a sorted JSON file used by the simulation.js. The program is run in the terminal, with the arguments listed below.
```
python parse_to_json.py [filename rows [clump]]
```
Simulation.js HTTP requests the data, and uses bike borrow/return timestamps and location to draw and guide a single blue dot (representative of one bike) to its desired destination on a Google Maps API Map. (One second is equivalent to 10 milliseconds in the simulation.)
