class something: # tạo ra 1 lớp có kiểu dữ liệu theo ý bạn
      def __repr__(self): # học thuộc tới return
              return 'dùng cho khi xuất print của 1 lớp bạn vừa mới tạo'
      def __str__ (self): # học thuộc tới return
              return 'dùng cho  xuất print của 1 lớp bạn vừa mới tạo'
sthing = something()
print('%r'%(sthing))
print('%s'%(sthing))
print(type(sthing))