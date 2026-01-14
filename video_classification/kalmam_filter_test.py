from vidstab import VidStab

# Initialize video stabilizer
stabilizer = VidStab()

# Stabilize input video and save to output_video.avi
stabilizer.stabilize(input_path='can_video.mp4', output_path='output_video.avi')
