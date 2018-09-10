# FirstTry
#My first python project
import urllib.request
import json
from collections import Counter as mset

CountOfIngr = 999

FirstRead = input("Введите список ингредиентов: ")
lisF = FirstRead.split();
lisF.sort()

url = "http://www.recipepuppy.com/api/?i="
for i in lisF :
    url += i
    url += ','
url = url[0:len(url)-1] + '&p='
url1 = url

i = 0
while i < 10 :

    i += 1

    url += str(i)

    res = urllib.request.urlopen(url)
    res_body = res.read()
    response = json.loads(res_body.decode("utf-8"))
    responses = str(response)
    responses = responses[103:len(responses)]

    lis = responses.split("{'title': ")

    for Recipe in lis:
        one = Recipe.split(": '")

        one[0] = one[0][0:-8]   #название
        one[1] = one[1][0:-16]  #ссылка
        one[2] = one[2][0:-14]  #игредиенты
        one.pop()               #убираем картинку

        Ingr = one[2].split(", ") #Ingr - now, lis - main

        Ingr.sort()
        lisF.sort()

        if list((mset(lisF) & mset(Ingr)).elements()) == Ingr: #проверяю кол-во элементов в ingr и если оно меньше текущего, кидаю туда

            if len(Ingr) < CountOfIngr :
                #print(one)
                #print(len(Ingr))
                BestOut = one
                CountOfIngr = len(Ingr)
    url = url1
#for qwe in BestOut:
#    print(qwe)
print("Самый простой рецепт по запросу - {}. \nОн содержит следующие ингредиенты: {} \nСсылка: {}".format(BestOut[0],BestOut[2],BestOut[1]))
