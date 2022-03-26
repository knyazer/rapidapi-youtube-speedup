# Speedup of rapid-api YouTube tracks download

The problem appeared when I've found out that rapid-api for downloading sound tracks from youtube uses file changers with 0.5 seconds delay, which is inconvenient. This code sample allows to neglect this forced delay, and download a file directly from the source.

To install all dependencies (only requests actually, but anyway):
```
pip install requirements.txt
```