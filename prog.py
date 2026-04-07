l1=[-4,-2,0,7,8]
p_l1=[i for i in l1 if i>0]
print(p_l1)
v1=-123
print(abs(v1))
 
l1=[' abc','ok ',' org ']
c_l1=[i.strip() for i in l1]
print(c_l1)

s_1=[(x,x**2) for x in range(6)]
print(s_1)
l=[[1,2,3],[4,5,6]]
t_l=[[l[j][i] for j in range(len(l)) for i in range(len(l[0]))]]  
print(t_l)                                                           