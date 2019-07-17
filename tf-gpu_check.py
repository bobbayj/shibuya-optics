# Checks if Tensorflow-GPU accelerated is installed correctly
# For help, see:
# https://www.pugetsystems.com/labs/hpc/How-to-Install-TensorFlow-with-GPU-Support-on-Windows-10-Without-Installing-CUDA-UPDATED-1419/#Step1)SystemPreparation-NVIDIADriverUpdateandcheckingyourPATHvariable(Possible\
import tensorflow as tf

tf.enable_eager_execution()

print(tf.constant('Hello from TensorFlow ' + tf.__version__))