from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("vid/GOPR1015.MP4")
clip2 = VideoFileClip("vid/GOPR1016.MP4")
clip3 = VideoFileClip("vid/GOPR1035.MP4")
final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("my_concatenation.mp4")