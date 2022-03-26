import requests
import json
import time

time_begin = time.time()

API_KEY = ""
ID = "vOXZkm9p_zY"

url = "https://youtube-mp3-download1.p.rapidapi.com/dl"

querystring = {"id": ID}

headers = {
	"X-RapidAPI-Host": "youtube-mp3-download1.p.rapidapi.com",
	"X-RapidAPI-Key": API_KEY
}

raw_link = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)['link']

print(f"Raw (indirect) link: {raw_link}")

text = requests.request("GET", raw_link).text

parse_starting_point = text.find("<script async>")
parse_piece = text[parse_starting_point:]

# Determine beginning and ending of coded url representation
begin = parse_piece.find("[")
end = parse_piece.find("]") + 1

codes = json.loads(parse_piece[begin:end])
offset = codes[0] - 60 # First symbol is always "<"

# Hand designed indices for the url inside the array
url_begin_index = 21
url_end_index = -15

direct_link = ""
for code in codes[url_begin_index:url_end_index]:
    direct_link += chr(code - offset)

print(f"Direct link: {direct_link}")

music_file = requests.get(direct_link)
open("file.mp3", "wb").write(music_file.content)

print(f"Done in {time.time() - time_begin} seconds")