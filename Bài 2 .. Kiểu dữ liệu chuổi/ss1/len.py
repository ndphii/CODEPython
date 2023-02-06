"""ví dụ 1"""
strA = 'nguyen duc phi\n'
# python hỗ trợ nhân n chuổi
print(strA*2)

"""ví dụ 2"""
'''dạng kiểm tra xem trong chuổi này có tồn tại các phần tử giống
chuổi kia và output chỉ có true hoặc false ! có phân biệt hoa thường''' 
# ta sẽ có dạng kiểm tra có trong (in) hoặc không có trong (not in)
st1 = "nguyen duc phi"
st2 = "duc phi"

#có trong (in)
print(st2 in st1) # lưu ý 2 có trong 1 khác 1 có trong 2
print(st1 in st2)

#không có trong (not in)
print(st1 not in st2)
print(st2 not in st1)

""" ví dụ 3 """
#cách lấy kí tư n trong chuổi !!! và lưu ý kí tự đầu tiên nằm ở vị trí số 0,kí tự cuối cùng nằm ở vị trí n-1
place = st1[4] # kí tự thứ 4 là e
place_ = st1[-1] # chỉ có python hỗ trợ kiểu này,lấy từ dưới lên là i
print(place)
print(place_)

""" ví dụ 4 """
# độ dài của chuổi (len) 
length = len(st2)+len(st1)+len(strA)
print(length)
""" ví dụ truy cập đến pt cuối cùng của chuổi , vì là chuổi có n phần tử , nhưng phần tử đầu tiên nằm ở vi trí thứ 0 
-> pt cuối là n-1 """
length_ = st1[len(st1)-1]
print(length_)

""" ví dụ 5 """
#thao tác cắt chuổi từ trái sang phải ... vd:st1[<vị trí bắt đầu> : <vị trí kết thúc>] hàm None là hàm lấy cả chuổi <=> len(  )
catchuoi = st1[7:None] #đặt hàm None ở vị trí bất đầu nó sẽ lấy từ số 0 , nếu ở vị trí kết thúc nó sẽ lấy số cuối cùng
print(catchuoi) 
#thao tác cắt chuổi từ phải sang trái
# st1[<vị trí bất đầu> : <vị trí kết thúc> : <bước nhảy>] bước nhảy là nhảy qua bao nhiêu pt để lấy phần tử tiếp theo
catchuoi_ = st1[None:None:-1] # khi dùng bước nhảy âm không được dùng số 0 thay vào đó là None
print(catchuoi_)

#ví dụ nếu biến chứ lộn xộn giữa các pt riêng biệt và list bên trong
cc = [1,2,'p','h','i',[3,4]]
ccc= cc[5][1] # có nghĩa là trong biến cc lấy ra pt thứ 5 và trong pt thứ 4 lấy ra pt thứ 1
print(ccc)