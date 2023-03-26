# You can use tensorflow and torch with GPU enabled
# in a repl! See https://docs.replit.com/power-ups/gpus

# Run this script: python gpu.py to ensure
# GPU has been turned on in the repl.

import tensorflow as tf
print("TensorFlow version:", tf.__version__)
# Should give something like PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')
# if GPU is enabled
print("GPU device:", tf.config.list_physical_devices('GPU'))

import torch
# Should print True if GPU is enabled
print("torch.cuda", torch.cuda.is_available())