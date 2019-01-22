Analysis of computation time for Dikstra's Algorithm on randomly generated networks
README file

------------------------------------------------------------------------------------

This project contains all of the source files used to generate the data and figures used in the Main Analysis document. 
All of the analysis is done in the PDF document, and may be read on it's own.

NB: To RunTimer.py and graphing.py, Dill, NumPy and PyPlot are required external libraries.

For further information, the contained files are as follows:

------------------------------------------------------------------------------------
MainAnalysis.PDF
    This is the write up of the project. It describes the process as a whole and 
    contains the analysis of the data.

------------------------------------------------------------------------------------
FullScriptSingleRun.py
    This script was written in such a way that it runs on it's own. [No external scripts needed]
    It shows how the main script works. When run, after following the input prompts,
    a single network is generated and Dijkstra's algorithm is run on it.
    Each step of this process is described and printed as an output in the terminal.

------------------------------------------------------------------------------------
RunTimer.py
    This is the main script which was run in order to generate the data used in graphing.py
    To control the number of iterations done, vary the Counter1Max value in classes.py
    This script will generate pickled Output.dict and Raw.out files which are used in graphing.py

------------------------------------------------------------------------------------
Classes.py
    This file is used to allow the same data structures to be used in both graphing.py and RunTimer.py
    Also contains Counter1Max, which controls the number of iterations done in RunTimer.py

------------------------------------------------------------------------------------
graphing.py
    This script was writen to generate the figures used in the main analysis
    NB: If using your own generated data, some of the figures will need to be adjusted to make them fit the new data correctly
    as the x and y axes are limited on several to make the data as easily visible as possible in the figures

------------------------------------------------------------------------------------
Output.dict and raw.out
    These are the pickled output data files from RunTimer.py 
    The original files are included here so that graphing.py has data to work with
    You may run RunTimer.py on your own computer, and new Output.dict and raw.out files will be made
    Graphing.py will work with these new files, but some of the figures may need to have their ranges adjusted to show the data more clearly.


This project was done mostly to practice using Python to work with large data sets.

Thanks for reading!

Erik