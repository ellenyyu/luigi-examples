# luigi

minimal working examples using Spotify's luigi 

example 1 

step 1. git clone luigi repo
step 2. cd to directory containing python file 
step 3. run python -m luigi --module top_artists AggregateArtists --local-scheduler --date-interval 2012-10
step 4. check out new files in data directory 

<font size = 8> https://luigi.readthedocs.io/en/stable/example_top_artists.html_</font>

example 2 

step 1. create a venv and install luigi and dependencies 
step 2. create luigi task to extract a list of books 
step 3. create a few more tasks 
step 4. define a global parameters 
step 5. run bottommost task python -m luigi --module word-frequency TopWords --local-schedule --GlobalParams-NumberBooks 15 --GlobalParams-NumberTopWords 750

_https://www.digitalocean.com/community/tutorials/how-to-build-a-data-processing-pipeline-using-luigi-in-python-on-ubuntu-20-04_

pending
* example 3 
* requirements file 
* gitignore file 
