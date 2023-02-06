# kiểu list có thể chứa mọi giá trị bên trong nó bao gồm chính nó vd:["phi",12,'17 tuổi',[ng]]\
a = ['12','17','Đức',[['P'],['h'],['i']]]
a_= [r for r in range(10)]
print(a)
print(a_)

#gán công thức riêng trong list
b = [[n,n+1,n+2] for n in range(1,5)]
print(b,'với số đứng đầu trong list làm chuẩn')

#hàm list là hàm biến mọi thứ trong ngoặc thành từng phần tử
#và chỉ dành cho kiểu chuổi
c =list('ndphi')
print(c)

