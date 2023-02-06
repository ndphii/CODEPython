# vài hàm dưới đây có thể dùng cho kiểu chuổi

a = [1,2,3,4,5,6,7,8,9]
b = a.count(7) # đếm số lần suất hiện phần tử số 7
b_= a.index(7) # vị trí xuất hiện số 7 đầu tiên ( nếu kiểm tra 1 pt k tồn tại sẽ có lỗi)
print(a) # 1->9
print(b) # 1
print(b_) # 6
# hàm count và index dùng cho kiểu list và kiểu chuổi đều được

c = a.copy() # hàm copy chỉ nhân bảng biến a nhưng không làm thay đổi biến ban đầu
c[6] = 'bảy' 
print(c) #[1, 2, 3, 4, 5, 6, 'bảy', 8, 9]

a.append(5) # cuối list a thêm số 5
c.append(['mười','mười một']) # cuối list a thêm list['mười','mười một']
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
print(c) #[1, 2, 3, 4, 5, 6, 'bảy', 8, 9, ['mười', 'mười một']]

a.extend([10,11,12,[13,14]]) # lấy từng phần tử 10 11 12 gán lần lượt vào biến a
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[13,14]]

a.insert(0,'một') # tại vị trí 0 thay đổi bằng 'một'
print(a) # ['một', 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 10, 11, 12, [13, 14]]



a1 = [1,2,3,4,5]
a1.pop(0) # gọi pt số 0 đi ra khỏi list và thay đổi luôn biến ban đầu
print(a1) #[2,3]

a1.remove(5) # xóa số 5 nếu không có số một sẽ bị lỗi
print(a1) # [2,3,4] do số 1 đã bị hàm pop gọi về an nghỉ :v

a1.reverse() # đảo ngược list
print(a1) # [4,3,2]

a1.sort() # sắp sếp từ nhỏ tới lớn, và nó có thể sắp sếp cả bảng chữ cái miễn là cùng kiểu dữ liệu
print(a1) # [2,3,4]

aa1 = a.clear() # xóa sạch và thay đổi luôn biến a 
print(aa1)




 




