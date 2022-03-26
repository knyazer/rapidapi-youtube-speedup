# Speedup of rapid-api YouTube tracks download
### *It is proof of concept, so have no high expectations*


The problem appeared when I've found out that rapid-api for downloading sound tracks from youtube uses file changers with 0.5 seconds delay, which is inconvenient. This code sample allows to neglect this forced delay, and download a file directly from the source.


## Quick start
To install all dependencies (only requests actually, but anyway):
```
pip3 install -r requirements.txt
```
or 
```
pip install -r requirements.txt
```
And then you can run main script. Do not forget to set your API key in ```API_KEY``` varaible inside main.py (line 7):
```
python3 main.py
```
or
```
python main.py
```