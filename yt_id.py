Link = input("Enter youtube video Link: ").strip()

if "v=" in Link:
    video_id = Link.split("v=")[1].split("&")[0]
    link = video_id.split("?")[0]
  
elif "youtu.be" in Link:
    video_id = Link.split("/")[-1]
    link = video_id.split("?")[0]
  
elif "shorts" in Link:
    video_id = Link.split("shorts/")[1].split("?")[0]
    link = video_id.split("?")[0]
  
else:
    link = "INCORRECT URL "

print("Video ID:", link)
