a = 'NgUyEn DuC pHi'

# capitalize() dùng để viết hoa chữ cái đầu k hỗ trợ nhiều str trong biến
print(a.capitalize()) # output Nguyen duc phi

# upper() all viết hoa
print(a.upper()) # output NGUYEN DUC PHI

# lower all viết thường
print(a.lower()) # output nguyen duc phi

# swapcase trong str các kí tự hoa->thường ,thường->hoa
print(a.swapcase()) # output nGuYeN dUc PhI

#title viết hoa các chữ cái đầu theo kiểu chủ đề 
b ='nguyen duc phi'
print(b.title()) # output Nguyen Duc Phi



'''encode nó dùng để mã hóa các dạng chữ cái k thuộc chữ cái latinh
nó sẽ trả những kí tự đó về dạng mã hóa tùy loại ngôn ngữ nhập vào'''
# kiểu chuẩn vd: d_ = d.encode('encoding=  ','errors=  ')
c = 'Nguyễn Đức Phi'
d = c.encode()
print(d)
print(type(d)) # output là những đoạn mã hóa của những chữ k thuộc latinh
