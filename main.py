import numpy as np
import torch

print("using", "GPU" if torch.cuda.is_available() else "CPU", "for pytorch")
print(np.zeros((2,)))