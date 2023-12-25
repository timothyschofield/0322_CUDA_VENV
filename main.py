

# CUDA 11.7
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
import torch, numpy
print("CUDA is avaliable:", torch.cuda.is_available())  # TRUE!
print(torch.version.cuda) # CUDA version 11.7
# python main.py
import numpy as np
a = np.arange(15)
print(a)