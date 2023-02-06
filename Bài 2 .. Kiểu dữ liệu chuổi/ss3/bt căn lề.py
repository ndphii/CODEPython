usesid = int(input('nhập id người dùng:'))
while (usesid != 201860155):
       print('ID không tồn tại!')
       usesid = int(input('enter id again:'))
else:        
       row_1 = ' {:-<20}-{:-^20}-{:->25}'.format('', '', '')
       row_2 = '| {:^20} | {:^20} | {:^20}|'.format('ID', 'Name', 'Place of birth')
       row_3 = '| {:^20} | {:^20} | {:^20}|'.format('201860155', 'Nguyen Duc Phi', 'Vietnamese')
       row_4 = ' {:-<20}-{:-^20}-{:->25}'.format('', '', '')
       print(row_1,'\n',row_2,'\n',row_3,'\n',row_4)
       

         