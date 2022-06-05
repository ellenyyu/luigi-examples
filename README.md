# luigi examples

This repo contains minimum working examples using Spotify's luigi. The idea here is to enable a quick grasp of the technology. 

## Example 1 

This example is pulled from the luigi documention. To learn how to run a luigi task, AggregateArtists, please follow the following steps: 

1. ```git clone``` the luigi repo ```https://github.com/spotify/luigi```
2. ```cd examples``` to get to the directory contain the python file you're going to run, top_artists.py
3. run ```python -m luigi --module top_artists AggregateArtists --local-scheduler --date-interval 2012-10```
4. check out new files in the data directory 

Play with the value of the date-interval parameter and see how it affects the files in the data folder. For example, you can try ```--date-interval 2012-8``` or ```--date-interval 2011-9```. Btw, instead of specifying a PYTHONPATH as shown in the official example, I used the command ```python -m ``` to be consistent with the examples that follow. The original example is found here https://luigi.readthedocs.io/en/stable/example_top_artists.html.  

## Example 2 

This examples shows an end to end job using luigi. Please open up this tutorial and complete the following items: 

1. create a venv and install luigi and dependencies 
2. create luigi task to extract a list of books 
3. create a few more tasks 
4. define a global parameters 
5. run bottommost task ```python -m luigi --module word-frequency TopWords --local-schedule --GlobalParams-NumberBooks 15 --GlobalParams-NumberTopWords 750```

Note, I did not set up an Ubuntu server with a non-root user and sudo privileges and I forgoed Step 4 _Running the Luigi Schedule_ in the original tutorial. Link to the tutorial https://www.digitalocean.com/community/tutorials/how-to-build-a-data-processing-pipeline-using-luigi-in-python-on-ubuntu-20-04

## Example 3

This is an example of a complete job using luigi where task 1 creates the inputs for task 2. This example also shows the difference between hardcoded parameters, one parameter, and multiple parameters in luigi. To get started, git clone this repo and run the following in your command line: 

1. run ```python run_luigi_hardcoded.py SquaredNumbers --local-scheduler```
2. run ```python run_luigi_oneparam.py SquaredNumbers --local-scheduler --n 20```
3. run ```python run_luigi_twoparam.py SquaredNumbers --local-scheduler --n 45 --start 9```

The original author is https://marcobonzanini.com/2015/10/24/building-data-pipelines-with-python-and-luigi/ . I adapted his work to test adding an additional parameter. Note, both parameters are not _used_ in dependent task, SquaredNumbers, but rather are simply fed in so they can be called with SquaredNumbers. Additionally, this example inspired me to write a task similar to PrintNumbers for my work. Last but not least, this example shows how you can run luigi with a 'normal' python script consisting of ```import luigi``` and ```if __name__ == '__main__': luigi.run()``` whereas previously, we showed a virtual environment with loaded packages. Along the same lines, this time, we caleld the python script directly whereas previously, we called the sccript with ```python -m luigi```.

## Pending work

* requirements file 
* gitignore file 
