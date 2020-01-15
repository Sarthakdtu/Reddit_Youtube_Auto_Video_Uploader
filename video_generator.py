import os
from audio_generator import generate_audio
from moviepy.editor import *

def generate_video():
    input_audio_title = generate_audio()
    input_audio = input_audio_title["audio"]
    title = input_audio_title["title"]
    input_video = "template_video.mp4"
    video_template = VideoFileClip(input_video)

    audio_clip = AudioFileClip(input_audio)

    output_video = video_template.set_audio(audio_clip)
    video_file_name = "youtube_video.mp4"
    output_video.write_videofile(video_file_name)
    print("Video Generated")
    #os.system("start youtube_video.mp4")
    return {"video": video_file_name, "title": title}