import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Считываем из входные данные из input.txt
input = open('input.txt', 'r')
s = input.read()
input.close()
s = s.split("\n")
coord_a =  [int(item) for item in s[0].split(" ")]
coord_b =  [int(item) for item in s[1].split(" ")]
df_orders = list()
orders_amount = int(s[2])
#Парсим массив заказов
for i in range(3, orders_amount*2+3,2):
    a = [int(item) for item in s[i].split(" ")]
    b = [int(item) for item in s[i+1].split(" ")]
    df_orders.append(np.array([[a[0],b[0]],[a[1],b[1]]]))
#Выстраиваем точки пути водителя
way = np.linspace(coord_a, coord_b, dtype=int, axis=0)
unique=[]
for i in way:
    if list(i) not in unique:
        unique.append(list(i))

way=np.array(unique)    
n=0
x, y = way.T
output = open('output.txt', 'w')
#Вычисляем оптимален ли заказ(представим что заказ оптимален если он по пути, а начало заказа начинается не дальше одной клетки)
for u in df_orders:
    order_a,order_b=u.T
    for j in way[1::]:
        if list(order_b) == list(j):
            for i in way[np.where(way == j)[0][0]::-1]:
                if order_a[0] == list(i)[0] or order_a[0]+1 == list(i)[0] or order_a[0]-1 == list(i)[0]:
                    if order_a[1] == list(i)[1] or order_a[1]+1 == list(i)[1] or order_a[1]-1 == list(i)[1]:
                        output.write(f"Order with coordinates {order_a}:{order_b} is optimal \n")
                        n+=1
                        break
#Записываем количество оптимальных заказов в output.txt
output.write(f"Amount of optimal orders:{n}")
output.close()
plt.plot(x,y, '-r') 
for i in df_orders:
    plt.plot(i[0],i[1]) 
plt.xticks (range(0, 11)) #Возьмем поле с размером 10х10
plt.yticks (range(0, 11))
plt.grid ( True )
plt.show()