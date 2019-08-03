import cv2
from deepLab import DLModel
import numpy as np
import imageio



DL= DLModel('data/deeplab_frozen_graph.pb')





class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = imageio.get_reader('videos/1.mp4',  'ffmpeg')
        print(self.video.get_meta_data()['size'])

    def __del__(self):
        self.video.release()

    def get_frame(self):
        for num, image in enumerate(self.video):
            #image = self.video.get_data(num)
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
            #
            image = self.process_image(image)
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
       


    def rotateclockwise(self, image):
        image = cv2.transpose(image)
        return cv2.flip(image, flipCode=1)
    
    def rotateanticlockwise(self, image):
        image = cv2.transpose(image)
        return cv2.flip(image, flipCode=0)

    def process_image(self, image):
        height = image.shape[0]
        width = image.shape[1]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        re1, re2 = DL.run(image)
        re2 = cv2.resize(re2, (width, height))
        res = cv2.bitwise_and(image,image,mask = re2)
        # res = np.hstack((image,res))
        return res

