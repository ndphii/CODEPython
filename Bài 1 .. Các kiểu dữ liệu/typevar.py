#gán biến a (ví dụ a =1.122) với kiểu dữ liệu là số thực 
a = {'p','h','i'}
print(a)
#in ra màn hình kiểu dữ liệu của biến a 
print(type(a))
#ta có thể kiểm tra kiểu dữ liệu của biến bằng cú pháp (type) của tất cả các loại dữ liệu
from decimal import*
getcontext().prec = 30 #lấy 30 số thập phân
x = Decimal(10)/3
print(x)
print(type(x))