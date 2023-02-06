#  dấu nhấy đơn và dấu nhấy kép như nhau 
# trong chuổi xuất hiện nháy đơn thì phải bọc dấu nháy kép ở ngoài,else
# trong chuổi vừa có nháy đơn và nháy kép thì bọc ngoài 3 đơn or 3 kép
# có thể dùng 3 dấu nháy {('')("")} dùng cho chuổi nhiều dòng
strings1 = " I'm Phi "
strings4 = ''' I'm Phi: class 11/6\n '''
''' (\n) là xuống dòng '''
strings5 ="""nguyen duc phi\n   hoc sinh trung hoc pho thong\n   lop 11/6 """
strings6 ='''nguyen duc phi\n   hoc sinh trung hoc pho thong\n   lop 11/6 '''
print(strings4,strings5,strings6)