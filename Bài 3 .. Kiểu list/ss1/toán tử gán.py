# chỉ có thể gán cùng kiểu dữ liệu
a=[1,2]
a+=['one','two'] # vẫn là biến a nhưng được gán thêm dữ liệu\
print(a)

#với kiểu list để thay đổi pt của list chỉ cần gọi pt đó ra và gán cho nó giá trị mới
a[0] = list('một')
print(a)

#với list a truy xuất đến pt thứ nhất và trong pt thứ nhất truy xuất tiếp pt thứ 3
print(a[0][2])