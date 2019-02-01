import cv2
import os

seq_number = 4
cam_number = 0

image_folder = 'Seq%02d/%02d/' % (seq_number, cam_number)
video_name = 'video_%02d_%02d.avi' % (seq_number, cam_number)

images = [img for img in os.listdir(image_folder) if img.endswith(".jp2")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width,height))

total = len(images)
for cnt, image in enumerate(sorted(images)):
	if cnt % 40 == 0:
		print("%d/%d" % (cnt + 1, total))
	video.write(cv2.imread(os.path.join(image_folder, image)))


cv2.destroyAllWindows()
video.release()