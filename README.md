# Luigi Examples

This repo contains minimum working examples using Spotify's luigi. The idea here is to enable a quick grasp of the technology. 

## Example 1 

This example is pulled from the luigi documentation. Using the following steps, you will run a luigi task: 

1. ```git clone``` the lugi repo ```https://github.com/spotify/luigi```
2. ```cd`` to directory containing the python file, top_artist.py
3. run ```python -m luigi --module top_artists AggregateArtists --local-scheduler --date-interval 2012-10```
4. check out new files in the data directory 

<sub> https://luigi.readthedocs.io/en/stable/example_top_artists.html </sub>

## Example 2 

1. create a venv and install luigi and dependencies 
2. create luigi task to extract a list of books 
3. create a few more tasks 
4. define a global parameters 
5. run bottommost task python -m luigi --module word-frequency TopWords --local-schedule --GlobalParams-NumberBooks 15 --GlobalParams-NumberTopWords 750

<sub> https://www.digitalocean.com/community/tutorials/how-to-build-a-data-processing-pipeline-using-luigi-in-python-on-ubuntu-20-04 </sub>

## Example 3

This is an example of a complete job using luigi where task 1 creates the inputs for task 2. This example also shows the difference between hardcoded parameters, one parameter, and multiple parameters in luigi. To get started, git clone the repo and run the following in your command line: 

1. run python run_luigi_hardcoded.py SquaredNumbers --local-scheduler
2. run python run_luigi_oneparam.py SquaredNumbers --local-scheduler --n 20
3. run python run_luigi_twoparam.py SquaredNumbers --local-scheduler --n 45 --start 9

The original author is https://marcobonzanini.com/2015/10/24/building-data-pipelines-with-python-and-luigi/ . I adapted his work to test adding an additional parameter. Note, both parameters are not _used_ in dependent task, SquaredNumbers, but rather are simply fed in so they can be called with SquaredNumbers. Additionally, this example inspired me to write a task similar to PrintNumbers for my work. Last but not least, this example shows how you can run luigi with a 'normal' python script consisting of ```import luigi``` and ```if __name__ == '__main__': luigi.run()``` whereas previously, we showed a virtual environment with loaded packages. Along the same lines, this time, we caleld the python script directly whereas previously, we called the sccript with ```python -m luigi```.

## Pending work

* requirements file 
* gitignore file 
