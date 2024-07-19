from pytube import YouTube

video_url = "https://youtu.be/qgnKpbnbAdg?si=YOE_8gbUwQA_HYxr"
save_location = "./"

yt = YouTube(video_url)
stream = yt.streams.filter(res="720p", progressive=True).first()
stream.download(output_path=save_location)