from moviepy.editor import ColorClip, AudioFileClip

def criar_video(audio_path, video_path):
    audio = AudioFileClip(audio_path)
    clip = ColorClip(size=(1080, 1080), color=(20, 20, 80), duration=audio.duration)
    clip = clip.set_audio(audio)
    clip.write_videofile(video_path, fps=24)
