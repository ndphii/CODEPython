def xulysmatkhau(string):
	passwrod = 'DucPhi'
	len_password = len(passwrod)
	len_string = len(string)
	if (len_string != len_password):
		print('mat khau khong hop le.')
	elif (len_string < 1):
		print('mat khau khong hop le.')
	elif(len_string == len_password):
		if (len_password == string):
			print('mat khau khong hop le.')
