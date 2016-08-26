import numpy as _np
from umbrella_potential import UmbrellaPotential as _up
import func
class UmbrellaIterator(object):

    
    def __init__(self, umbrella,overlap) :
        self.umbrella=umbrella
        self.overlap=overlap
        self.rejected=[]
        self.accepted=None
        self.check=0
r"""overlap is calculated by integrating product of 2 gaussian functions, i.e. umbrella distributions
if k2 is not given then it will be assumed same spring constants for both umbrellas"""

    def find_overlap(self, x2, k2=None):
        x1=self.umbrella.effective_center
        k1=self.umbrella.spring_constant
        if k2==None:
            k2=k1
        k12=k1+k2
        x12=(k1*x1+k2*x2)/(k1+k2)
        delta12=-0.5*(k1*x1**2+k2*x2**2-k12*x12**2)
        result = _np.sqrt(k1*k2/(2*_np.pi*k12))*_np.exp(delta12)
        return result*_np.sqrt(4*_np.pi/_np.minimum(k1,k2))
    
    
    def find_next_umbrella(self, direction): ##
        x1=self.umbrella.effective_center
        k1=self.umbrella.spring_constant
        overlap=self.overlap
        if (direction=="positive"):
            bins=_np.arange(x1, x1+5,0.001).reshape(-1,1)
        else:
            bins=_np.arange(x1-5, x1,0.001).reshape(-1,1)
        for x in bins:
            r = self.find_overlap(x)
            if r <= overlap+0.003 and r >= overlap-0.003:
                return round(x[-1],3)

r"""center_check function takes an umbrella iterator object
It compares the effective center and given center of umbrella, if they differ more than 0.1 then 
the center will be rejected and new center will be assigned to this umbrella operator object"""
    def center_check(self):
        if(len(self.rejected)!=0):
            if(_np.abs(self.rejected[0]-self.umbrella.effective_center)>0.01):
                if(f.check_if_exists(self.rejected[1:-1], self.umbrella.center) and self.check!=3):##if current center is already rejected, than increase the spring constant
                    self.umbrella.spring_constant=self.umbrella.spring_constant*2
                    self.umbrella.center=self.rejected[0]
                    rejected=[]
                    self.check+=1
                else:
                    self.rejected.append(self.umbrella.center)
                    self.umbrella.center=self.rejected[0]+self.umbrella.center_correction ##change umbrella center adding with the center corrention value
            else:
                self.accepted=self.umbrella.center
        else:
            if(_np.abs(self.umbrella.center_correction)<0.1):##
                self.accepted=self.umbrella.center
            else:
                self.rejected.append(self.umbrella.center)
                self.umbrella.center=self.umbrella.center+self.umbrella.center_correction ##change umbrella center adding with the center corrention value

                
r"""Inputs:
rangemin:Minimum coordinate of reaction coordinate
rangemax:Maximum coordinate of reaction coordinate
overlap:Overlap value which the umbrellas should have
first_umbrella:the first umbrella position should be placed by user
spring_constant:Spring constants of the umbrellas needed for overlap calculation
direction: can take string values positive or negative. Enter it in "" marks. 

returns theoretical umbrella positions with given inputs in the given direction
"""

def predict_umbrella_locations(rangemin, rangemax, overlap, first_umbrella, spring_constant, direction):
    us=_up(first_umbrella,spring_constant)
    ui=UmbrellaIterator(us,overlap)
    ui.umbrella.effective_center=first_umbrella
    locations=[first_umbrella]
    while ui.find_next_umbrella(direction)<rangemax and ui.find_next_umbrella(direction)>rangemin:
        locations.append(ui.find_next_umbrella(direction))
        ui.umbrella.effective_center=locations[-1] 
    return locations

def check_if_exists(list_, number):
    check=False
    for i in range(len(list_)) :
        if (np.abs(list_[i]-number)<0.01):
            check= True
    return check
