# 数据持久性说白了就是将内存中的数据存入硬盘并保证存入、读出过程中数据不出错
# pickle是标准库包，其作用就是保证数据存入、读出的正确与方便。

import pickle


# 字典1：餐厅菜单
restaurant_menu = {
    'name': 'The Italian Bistro',
    'cuisine': 'Italian',
    'location': '123 Pasta Lane, New York, NY 10001',
    'opening_hours': {
        'monday': '11:00 AM - 10:00 PM',
        'tuesday': '11:00 AM - 10:00 PM',
        'wednesday': '11:00 AM - 10:00 PM',
        'thursday': '11:00 AM - 10:00 PM',
        'friday': '11:00 AM - 11:00 PM',
        'saturday': '12:00 PM - 11:00 PM',
        'sunday': '12:00 PM - 9:00 PM'
    },
    'menu': {
        'appetizers': [
            {'name': 'Bruschetta', 'price': 8.99, 'description': 'Toasted bread with garlic, tomatoes, and basil.'},
            {'name': 'Calamari', 'price': 12.99, 'description': 'Crispy fried squid with marinara sauce.'}
        ],
        'main_courses': [
            {'name': 'Spaghetti Carbonara', 'price': 18.99, 'description': 'Classic pasta dish with eggs, pancetta, and Parmesan.'},
            {'name': 'Margherita Pizza', 'price': 15.99, 'description': 'Thin-crust pizza with tomato sauce, mozzarella, and fresh basil.'}
        ],
        'desserts': [
            {'name': 'Tiramisu', 'price': 7.99, 'description': 'Layered coffee-soaked ladyfingers with mascarpone cream.'},
            {'name': 'Gelato', 'price': 5.99, 'description': 'Flavors of the day: vanilla, chocolate, and strawberry.'}
        ],
        'drinks': [
            {'name': 'Red Wine', 'price': 9.99, 'description': 'A selection of Italian red wines.'},
            {'name': 'Espresso', 'price': 3.99, 'description': 'Strong, rich Italian coffee.'}
        ]
    }
}


# print("\n打印字典1：\n")
# for x in restaurant_menu:
#     print(x , ":" , restaurant_menu[x])
#     print("-------------------------")


# 字典2:天气预报
weather_forecast = {
    'city': 'New York',
    'country': 'USA',
    'latitude': 40.7128,
    'longitude': -74.0060,
    'timezone': 'America/New_York',
    'current_weather': {
        'temperature': 15.2,  # in Celsius
        'humidity': 70,
        'wind_speed': 5.3,  # in m/s
        'wind_direction': 'NE',
        'condition': 'Partly Cloudy',
        'icon': 'partly_cloudy.png'
    },
    'forecast': [
        {
            'date': '2023-10-15',
            'high_temperature': 18.0,
            'low_temperature': 12.0,
            'condition': 'Sunny',
            'precipitation_probability': 0.1
        },
        {
            'date': '2023-10-16',
            'high_temperature': 20.0,
            'low_temperature': 14.0,
            'condition': 'Rainy',
            'precipitation_probability': 0.7
        },
        {
            'date': '2023-10-17',
            'high_temperature': 17.0,
            'low_temperature': 11.0,
            'condition': 'Cloudy',
            'precipitation_probability': 0.3
        }
    ]
}



# 字典3：课程信息
course = {
    'course_id': 'CS101',
    'title': 'Introduction to Computer Science',
    'instructor': {
        'name': 'Dr. Jane Smith',
        'email': 'jane.smith@university.edu',
        'department': 'Computer Science'
    },
    'credits': 4,
    'description': 'This course provides an introduction to the fundamental concepts of computer science, including programming, algorithms, and data structures.',
    'schedule': {
        'days': ['Monday', 'Wednesday', 'Friday'],
        'time': '9:00 AM - 10:15 AM',
        'location': 'Building A, Room 101'
    },
    'students': [
        {'name': 'Alice Johnson', 'student_id': 'S12345', 'email': 'alice.johnson@student.edu'},
        {'name': 'Bob Brown', 'student_id': 'S67890', 'email': 'bob.brown@student.edu'}
    ],
    'assignments': [
        {'title': 'Homework 1', 'due_date': '2023-10-15', 'points': 100},
        {'title': 'Project 1', 'due_date': '2023-11-01', 'points': 200}
    ],
    'resources': [
        {'type': 'textbook', 'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen'},
        {'type': 'lecture_notes', 'url': 'https://example.com/lecture_notes.pdf'}
    ]
}



#############################################
# 保存多个对象到同一个文件里，这里先把多个对象加到同一个对象里，然后再保存这个总对象
fname = input("请输入保存文件名(直接回车则用默认文件名): ")
if fname == "":
    fname = "P301_保存的二进制文件.pickle"

outf = open(fname, 'wb')    # 二进制写
object_1 = [restaurant_menu,weather_forecast,course]      #把上面三个字典加入同一个表对象中
pickle.dump(object_1,outf)  # 保存到硬盘文件中
outf.close()



# 显示被保存的文件
print("\n显示被保存的文件\n")
for x in object_1: 
    print(x)   
    print("-------------------------------------------")
print("===========================================================\n\n")


# 恢复被保存的文件
inf=open(fname, 'rb')   # 二进制方式只读打开文件
object_recover = pickle.load(inf)
inf.close()

# 显示恢复的文件
print("\n显示恢复的文件\n")
for x in object_recover: 
    print(x)   
    print("-------------------------------------------")