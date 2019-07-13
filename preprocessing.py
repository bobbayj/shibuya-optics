#%%
# Setup
# https://tammo.io/cs/2017/12/07/ubuntu-cuda-gpu-keras-setup.html
import tensorflow as tf
    
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))