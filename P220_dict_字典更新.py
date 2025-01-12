faculty = {'bio': 1, 'math': "002"}         #不同数据类型的也可以改
print(faculty)

faculty.update(bio = 361, math = 109)
print("字典更新后：",faculty)
print(type(faculty))