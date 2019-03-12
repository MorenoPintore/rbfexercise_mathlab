import numpy as np
class Inverse_multiquadric:
    eps = 1
    
    def __call__(self,x):
        r=np.linalg.norm(x)
        return 1/np.sqrt(1+self.eps*self.eps*r*r)

a=Inverse_multiquadric()
