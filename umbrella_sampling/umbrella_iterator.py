import numpy as _np
from umbrella_potential import UmbrellaPotential as _up
class UmbrellaIterator(object):
	rejected=[]
	accepted=[]
	
	def __init__(self, umbrella,overlap) :
		self.umbrella=umbrella
		self.overlap=overlap
	
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


	def find_next_umbrella(self):
		x1=self.umbrella.center
		k1=self.umbrella.spring_constant
		overlap=self.overlap
		bins=_np.arange(x1, x1+5,0.001).reshape(-1,1)
		for x in bins:
			r = self.find_overlap(x)
			if r <= overlap+0.002 and r >= overlap-0.002:
				return r[-1]	
				
	def center_check(self):
		if not (self.umbrella.center==self.umbrella.effective_center):##not exactly equal but within a range, change it accordingly
			UmbrellaIterator.rejected.append(self.umbrella.center)
			self.umbrella.center=self.umbrella.center+self.umbrella.center_correction
		else:
			UmbrellaIterator.accepted.append(self.umbrella.center)
