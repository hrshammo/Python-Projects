import cv2
import os

def convert_images_to_video(image_folder, output_file, frame_duration=1000):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()  # Sort the images alphabetically

    frame_width, frame_height = 0, 0
    frames = []

    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)
        height, width, _ = frame.shape

        if frame_width == 0 and frame_height == 0:
            frame_width = width
            frame_height = height

        if width != frame_width or height != frame_height:
            frame = cv2.resize(frame, (frame_width, frame_height))

        frames.append(frame)

    # Create a VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video = cv2.VideoWriter(output_file, fourcc, 1 / (frame_duration / 1000), (frame_width, frame_height))

    for frame in frames:
        video.write(frame)

    video.release()

if __name__ == "__main__":
    input_folder = "a"  # Replace with the path to your image folder
    output_video = "output_slideshow.avi"       # Output video file name

    convert_images_to_video(input_folder, output_video)
