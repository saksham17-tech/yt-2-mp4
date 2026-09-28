import yt_dlp

url = input("Enter URL: ")

yt_dlp.YoutubeDL({"format" : "bestvideo+bestaudio/best"}).download([url])