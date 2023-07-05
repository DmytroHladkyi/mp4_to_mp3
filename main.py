import moviepy.editor
from pathlib import Path

video_file = Path(r'C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\project8_mp4_to_mp3\6e011a2759.240.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'C:/Users/Hladkyi Dmytro/Desktop/IT Oprogromowanie/Python_Projects/project8_mp4_to_mp3/{video_file.stem}.mp3')