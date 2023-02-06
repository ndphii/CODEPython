a = 'player run know bettle ground'

b = a.split(' ',2) # cắt đều biến a với kí tự cắt là rỗng và cắt 2 lần(int)
print(b) #output ['player', 'run', 'know', 'bettle ground']
# tương tự có thể lsplit(cắt từ phải qua),rsplit(cắt từ trái qua)

c = a.partition('know') #cắt trước chữ known ra 1 phần từ , run một phần tử , phần còn lại là 1 pt
print(c) #output ('player run ', 'know', ' bettle ground')
# r , l
# khi xét không có phần tử cần tách ,tự động trả về 2 giá trị rỗng và dữ liệu nhập

d = a.count('n') #đếm phần tử n trong chuỗi
d_= a.count('r',0,10) # từ vị trí số 0 đến 10 có bao nhiêu chữ r
print(d) # output 3
print(d_) # output 2

e = a.startswith('player') # bắt đầu bằng chữ player đúng hay không (true or false)
e_= a.startswith('run',8)  # chữ run bắt đầu từ vị trí số 8 đúng không
print(e) #true
print(e_) #false
f = a.endswith('ground',23) # vị trí kết thúc của chữ ground từ vị trí 23 đúng không
print(f) #true

g = a.find('bettle')#chữ bettle xuất hiện đầu tiên từ vị trí số mấy
print(g)#16 (k tìm thấy,kết quả = -1)
# r,l
# ngoài ra còn có index(tác dụng tương tự) tuy nhiên sẽ có lỗi nếu không tìm thấy #r,l

h = a.islower()# nó có phải là chuổi viết THƯỜNG hay không(có 1 chữ hoa cũng sai)
h_= a.isupper()# nó có phải là chuổi viết HOA hay không((có 1 chữ thường cũng sai))
print(h)#true
print(h_)#false

j = a.isdigit()#chuỗi a có phải là 1 số hay không
print(j)#false

k = a.isspace()# cả chuổi có phải là 1 khoẳng trắng hay không
print(k)# false