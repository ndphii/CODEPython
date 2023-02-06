y =r'fgh\nnvm'  # R dùng để in các kí tự giống escapesquence trong tuple
z =u'jjda\tn'    # U dùng để thêm các escapesquence trong tuple nhưng vẫn hoạt động bt
print(y)
print(z)

string = b'\xe1\xbb\x8d'
#string với mã hóa 'utf-8'
mang = bytes(string)
print(mang)