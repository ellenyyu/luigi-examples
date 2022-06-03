# luigi

minimal working examples using Spotify's luigi 

example 1 

1. git clone luigi repo
2. cd to directory containing python file 
3. run python -m luigi --module top_artists AggregateArtists --local-scheduler --date-interval 2012-10
4. check out new files in data directory 

<sub> https://luigi.readthedocs.io/en/stable/example_top_artists.html </sub>

example 2 

1. create a venv and install luigi and dependencies 
2. create luigi task to extract a list of books 
3. create a few more tasks 
4. define a global parameters 
5. run bottommost task python -m luigi --module word-frequency TopWords --local-schedule --GlobalParams-NumberBooks 15 --GlobalParams-NumberTopWords 750

<sub> https://www.digitalocean.com/community/tutorials/how-to-build-a-data-processing-pipeline-using-luigi-in-python-on-ubuntu-20-04 </sub>

pending
* example 3 
* requirements file 
* gitignore file 
