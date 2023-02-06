# định dạng bằng f-string dùng cho trường hợp gán 1 biến cho trước hoặc đã có sẵn vào
a ='ABC'
print('1/' + a)#vẫn chưa có gì khác biệc so với chuổi bình thường 
#cho đến khi
b =f'{a}DEF'# biến a đã có sẵn
print('2/' + b)  


# join có tác dụng khá giống với f-string có tác dụng thế nhiều chuổi vào 1 chuổi và đứng đầu
# cú pháp var.join([chuổi]) 
c =' chữ cũng là thầy,'
c_= c.join(['1','2','n cũng vẫn là thầy'])
print(c_) # output 1 chữ cũng là thầy,2 chữ cũng là thầy,n cũng vẫn là thầy

# repalce thay thế thằng này , bằng thằng kia
''' cú pháp var.replace('thằng này đi ra','để thằng này thế chỗ') 
ra vào 1 hoặc nhiều đều dc tùy cách xắp sếp hợp lí'''
d = '10 14 15 16 17 18 19 20'
d_= d.replace('10','10 11 12 13') 
print(d_) 

# strip cắt bỏ các kí tự ('c') đầu và cuối  cú pháp var.strip('kí tự cần bỏ ở 2 đầu')
e = '123PHI321' 

e_= e.lstrip('123') # cắt trái
print(e_) #output PHI321

e___= e.strip('123') # cắt đều 2 bên
print(e___) #output PHI

e__= e.rstrip('123') # cắt phải
print(e__) #output 123PHI

