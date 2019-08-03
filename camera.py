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
        self.video = cv2.VideoCapture('videos/1.mp4')
        self.io_video = imageio.get_reader('videos/1.mp4',  'ffmpeg')
        self.metadata_size_flag = self.io_video.get_meta_data()['source_size'] == self.io_video.get_meta_data()['size']
        

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if success:
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
            #
            image = self.process_image(image)
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
        else:
            return None


    def rotateclockwise(self, image):
        image = cv2.transpose(image)
        return cv2.flip(image, flipCode=1)
    
    def rotateanticlockwise(self, image):
        image = cv2.transpose(image)
        return cv2.flip(image, flipCode=0)

    def process_image(self, image):
        
        width = image.shape[0]
        height = image.shape[1]
        if not self.metadata_size_flag:
            image = self.rotateclockwise(image)
        re1, re2 = DL.run(image)
        print(image.shape, re2.shape)
        
        re2 = cv2.resize(re2, (image.shape[1], image.shape[0]))
        print(image.shape, re2.shape)
        res = cv2.bitwise_and(image,image,mask = re2)
        # res = np.hstack((image,res))
        return res

