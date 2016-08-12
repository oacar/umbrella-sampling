import numpy as _np
from umbrella_potential import UmbrellaPotential as _up
import func
class UmbrellaIterator(object):

    
    def __init__(self, umbrella,overlap) :
        self.umbrella=umbrella
        self.overlap=overlap
        self.rejected=[]
        self.accepted=None
        self.prev_effective_center=None
    def find_overlap(self, x2, k2=None):
        x1=self.umbrella.center
        k1=self.umbrella.spring_constant
        if k2==None:
            k2=k1
        k12=k1+k2
        x12=(k1*x1+k2*x2)/(k1+k2)
        delta12=-0.5*(k1*x1**2+k2*x2**2-k12*x12**2)
        result = _np.sqrt(k1*k2/(2*_np.pi*k12))*_np.exp(delta12)
        return result*_np.sqrt(4*_np.pi/_np.minimum(k1,k2))
    
    
    def find_next_umbrella(self): ##
        x1=self.umbrella.center
        k1=self.umbrella.spring_constant
        overlap=self.overlap
        bins=_np.arange(x1, x1+5,0.001).reshape(-1,1)
        for x in bins:
            r = self.find_overlap(x)
            if r <= overlap+0.002 and r >= overlap-0.002:
                return r[-1]


    def center_check(self):
        if(len(self.rejected)!=0):
            if(_np.abs(self.rejected[0]-self.umbrella.effective_center)>0.1):
                if(func.check_if_exists(self.rejected, self.umbrella.effective_center)):##if current effective_center is already rejected, than increase the spring constant
                    self.umbrella.spring_constant=self.umbrella.spring_constant*2
                
                self.rejected.append(self.umbrella.center)
                self.umbrella.center=self.umbrella.center+self.umbrella.center_correction ##change umbrella center adding with the center corrention value
            else:
                self.accepted=self.umbrella.center
                self.prev_effective_center=None
        else:
            if(_np.abs(self.umbrella.center_correction)<0.1):
                self.accepted=self.umbrella.center
            else:
                self.rejected.append(self.umbrella.center)
                self.umbrella.center=self.umbrella.center+self.umbrella.center_correction ##change umbrella center adding with the center corrention value
                
