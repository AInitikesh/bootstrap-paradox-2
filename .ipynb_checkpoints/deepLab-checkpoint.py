import tensorflow as tf
import cv2
import numpy as np

class DLModel(object):
  """Class to load deeplab model and run inference."""

  INPUT_TENSOR_NAME = 'ImageTensor:0'
  OUTPUT_TENSOR_NAME = 'SemanticPredictions:0'
  INPUT_SIZE = 513
  FROZEN_GRAPH_NAME = 'frozen_inference_graph'

  
    
  def __init__(self, tarball_path):
    """Creates and loads pretrained deeplab model."""
    self.graph = tf.Graph()

    
    with self.graph.as_default():
      
      
      od_graph_def = tf.GraphDef()
      with tf.gfile.GFile(tarball_path, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')
            
		    
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.40
    self.sess = tf.Session(config=config ,graph=self.graph)


  def run(self, image):
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #image = Image.fromarray(image)
    width =image.shape[0]
    height = image.shape[1]
    resize_ratio = 1.0 * self.INPUT_SIZE / max(width, height)
    target_size = (int(resize_ratio * width), int(resize_ratio * height))
    #resized_image = image.convert('RGB').resize(target_size, Image.ANTIALIAS)
    
    resized_image = cv2.resize(image,(target_size[1],target_size[0]))
    
    
    batch_seg_map = self.sess.run(
        self.OUTPUT_TENSOR_NAME,
        feed_dict={self.INPUT_TENSOR_NAME: [np.asarray(resized_image)]})
        
        
    seg_map = batch_seg_map[0]
    seg_map[seg_map!=15]=0
    seg_map[seg_map==15]=255
    return resized_image, seg_map.astype(np.uint8)