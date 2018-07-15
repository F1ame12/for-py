'''
str  = "dfsfsdefsfdfse"
print(set(str))

L = [2,3,4]             
L[0:1] = [1.1,1.2]  
print(L)     
L[2:]  = [3.3,4.4,5.5]
print(L)   
L[:]   = [3,4]    
print(L)

L = [1,2,3,4,5,6]
print(L)
L[0::2] = [1.1,2.2,3.3]
print(L)
#L[0:10:2]=[1.1,2.2,3.3,4.4,5.5] 报错
#print(L)
#L[0::2]=[0.1,0.3]  报错
#print(L)
L[::2]="ABC"
print(L)
#L[::2]="ABCD" 报错
#print(L)
'''
x = [1,2,3,4,5,6]
print(len(x),max(x),min(x),sum(x),any(x),all(x))