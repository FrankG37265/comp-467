frame1 = 67
frame2 = 6767
frame3 = 676767

def timecode(frame):
    if frame < 24:
        return f"00:00:00:{frame:02}"
    
    seconds = frame // 24
    frames = frame % 24
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}:{frames:02}"

print("\nTimecodes:")
print(f"frame1({frame1}): {timecode(frame1)}")
print(f"frame2({frame2}): {timecode(frame2)}")
print(f"frame3({frame3}): {timecode(frame3)}")