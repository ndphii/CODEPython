# cũng là chèn vào như kiểu % nhưng là 1 kiểu chèn khi dữ liệu chưa có
# với cú pháp '{n},{n}'.format(...,...) cho tất cả kiểu dữ liệu như %s , %r
a = 'seven:{1}\neight:{0}\nnice:{2}'.format(8,7,9)
# nếu ko đánh thứ tự vào các ngoặc nhọn format sẽ điền vào theo thứ tự(8,7,9)
print(a)
b ='only one value: {1}'.format(1,2)# ta có thể format dư nhưng k được thiếu
print(b)
c ='two same value: {0},{1}'.format(1,2)# và có thể lặp lại n lần
print(c)
# nếu vẫn chưa thõa mãn sự rỏ ràng format vẫn chiều lòng bạn
d = 'số 10 = {ten}, số 1 = {one}'.format(ten = 'mười', one = 'một')
print(d)