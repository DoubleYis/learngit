def cleanup_data(ReadPath, SavePath, CategoryList, window, s) #文件夹地址，保存的文件夹地址，商品类别列表[0,1,2,3,4,5,6,7]注意改成str，划分的时间长度，m=1取购买m=2取评论，
	os.makedirs(SavePath)
	for i in range(len(CategoryList))
		fileaddr = ReadPath + CategoryList[i] + ''
		files = os.listdir(fileaddr)
		os.makedirs(SavePath + CategoryList[i] + ''+'relative_time'+'')
		os.makedirs(SavePath + CategoryList[i] + ''+'interval_time'+'')
		for j in range(len(files))
			data_dict = {}
			f = open(fileaddr + files[j],'r', encoding = 'utf-8')
			for line in f.readlines()
				data = line.strip('n').split(' ')[02] + [line.strip('n').split(' ')[4]] #取出时间间隔，相对购买时间，相对评论时间
				if s is True #取相对购买时间
					if (int(float(data[0])) % window == 0) and (int(float(data[0])) != 0)
						w = int(float(data[0]))window - 1
					else
						w = int(float(data[0]))  window
					key1 = str(w)+'-'+'1' #相对评论、购买时间
					key2 = str(w)+'-'+'2' #时间间隔
					try
						data_dict[key1] = data_dict[key1] + '-' + data[0]
						data_dict[key2] = data_dict[key2] + '-' + data[2]
					except #第一个数直接赋值value，后面加“，value”
						data_dict[key1] = data[0]
						data_dict[key2] = data[2]
				else #取相对评论时间
					if int(float(data[1]))%window == 0 and int(float(data[1])) != 0
						w = int(float(data[1]))window - 1
					else
						w = int(float(data[1]))  window
					key1 = str(w) + '-' + '1'
					key2 = str(w) + '-' + '2'
					try
						data_dict[key1] = data_dict[key1] + '-' + data[1]
						data_dict[key2] = data_dict[key2] + '-' + data[2]
					except
						data_dict[key1] = data[1]
						data_dict[key2] = data[2]
			f.close()
			print(data_dict.keys())

			window_num = max(list(map(process,data_dict.keys())))
			print(window_num)
			f1 = open(SavePath + CategoryList[i] + 'relative_time' + files[j], 'w', encoding = 'utf-8')
			f2 = open(SavePath + CategoryList[i] + 'interval_time' + files[j], 'w', encoding = 'utf-8')
			for m in range(window_num + 1)
				try
					f1.write(data_dict[str(float(m)) + '-1'] + 'n')
				except
					f1.write('n')
				try
					f2.write(data_dict[str(float(m)) + '-2'] + 'n')
				except
					f2.write('n')
			f1.close()
			f2.close()