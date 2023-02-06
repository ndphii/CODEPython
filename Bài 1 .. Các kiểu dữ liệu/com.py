#Số phức :<Phần thực> + <Phần ảo> + j.Trong đó <Phần thực> <Phần ảo> là số thực,j là đơn vị ảo trong toán học với  j^2= -1
#Để tạo một số phức ta dùng hàm complex
c = complex(5,-7) # tương tự như tạo 1 phân số faction,,, có thể dùng ký tự j để thay thế complex (c = 4 + 2j)
print(c)
#nếu muốn lấy phần thực : print(<tên biến>.real)
print(c.real)
#nếu muốn lấy phần ảo   : print(<tên biến>.imag)
print(c.imag)

d = complex(2,3)
#thực cộng thực ảo cộng ảo
print(d+c)
print(abs(d*c))
e=complex(0,1)
if(e*e==-1):
	print('true')
else:
	print('fasle') 