"""gán 1 chuổi vào 1 chuổi , bằng lệnh <'..... %s ....'%('....')> phần gán sẽ nằm tại vị trí của %s
có thể gán 1 hoặc nhiều %s và có thể gán cho biến chuổi hoặc cho print .. ví dụ:"""
# %S và %R
a = 'my name is %s %s %s' # phần % này có thể gán ở đây hoặc ở print 
print(a%('nguyen','duc','phi')) #output:my name is nguyen duc phi

b = 'I am %s year old\nAnd am in calss %s' %('16','11/6') # %s lấy trong ngoặc %r lấy luôn dấu ngoặc
print(b) #output:I am 16 year old And am in calss 11\6

r ='ô thứ nhất:%r\nô thứ hai:%r' %([1,2,3],[3,4,5])
print(r)             # %s và %r có thể dùng cho mọi kiểu dữ liệu

# chỉ có %d và %f là bắt buộc phải kiểu dữ lệu số không có " "
# %d chỉ lấy phần nguyên,không phải làm tròn
d = '%d and %.2f'%(4.542,10/3) 
print(d) #output:4 and 3
# %f hỗ trợ cho kiểu float và chỉ có %f hỗ trợ lấy n số thập phân đứng sau với '%.nf' %('..')
f = '%.2f'%(3.141592654)
print(f) # số pi đã được làm tròn thành 2 chữ số tp:3.14
