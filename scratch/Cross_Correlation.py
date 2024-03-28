import numpy as np
from scipy import signal as sp
from time import time
np.random.seed(42)
ip=np.random.rand(3,28,28)
kernel = np.random.rand(3,20,20)

n,m,p=kernel.shape

w,h,l=ip.shape

bias   = np.random.rand(1,h-m+1,l-p+1)

def correlation(ip,kernel):  
    n,m,p=kernel.shape
    w,h,l=ip.shape
    output=np.zeros((1,h-m+1,l-p+1))
    i=0
    j=0
    
    for i in range(l-p+1):
       
        for j in range(h-m+1):
            val=0
            for o in range(w):
                sum_ip=ip[o,i:i+p,j:j+m]
            
                sum_ker=kernel[o]
        
               
                val+=np.sum(np.sum(sum_ip*sum_ker,axis=0),axis=0)
            output[0,i,j]=val
    return output

final=np.copy(bias)
out=np.copy(bias)
print(out.shape)
start_time=time()
final+=correlation(ip,kernel)
end=time()
my=end-start_time
print("Time Taken by my code:",end-start_time)
start_time=time()
out+=sp.correlate(ip,kernel,mode='valid')
end=time()
scp=end-start_time
print("Time Taken by scipy:",end-start_time)
print(out)
print("Here")
print(final)

    

            
                
            
        


# def xcorela(ip_mat,kernel,bias):
    