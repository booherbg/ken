import urllib2

url = "http://www.lyrics.com/somebody-that-i-used-to-know-lyrics-gotye.html"

request = urllib2.Request(url)

handle = urllib2.urlopen(request)

content = handle.read()

splitted_page = content.split("<div id=\"lyric_space\">", 1)

splitted_page = splitted_page[1].split("</div>", 1)

f = open("Song.txt", "w")
f.write(splitted_page[0])
f.close()
f = open("Song.txt", "r")
f.read()
