''' căn lề trái: {:(c)<n}.format(c)
căn lề phải: {:(c)>n}.format(c)
căn giữa:{:(c)^n}.format(c)
#với:
c là kí tự bạn muốn thay thế vào chỗ trống,nếu để trống thì sẽ là kí tự khoảng trắng
n là số kí tự dùng để căn lề'''
a = '{:<5}{:-^10} có ma!!!'.format('aaaa',':v') # căn lề trái
print(a)
b = 'con {:!>10} '.format(' đũyy') # căn lề phải
print(b)
c = '{:-^13}'.format('The End') 
print(c)

d = 'End'# giống với kỉ thuật căn lề '{:<1 C> (<>^) <d>}'.format('<kí tự>')

# ljust (<var>.ljust(d,'') = căn lề trái: {:(c)<n}.format(c)
print(d.ljust(17,'~'))

# center (<var>.center(d,'') = căn giữa:{:(c)^n}.format(c)
print(d.center(17,'~'))

# rjust (<var>.rjust(d,'') = căn lề phải: {:(c)>n}.format(c)
print(d.rjust(17,'~'))