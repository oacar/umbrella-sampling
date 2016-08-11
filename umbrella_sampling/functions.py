import numpy as np

def check_if_exists(list_, number):
    check=False
    for i in range(len(list_)) :
        if (np.abs(list_[i]-number)<0.05):
            check= True
    return check
