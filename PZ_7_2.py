#Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
#расположенную между первым и вторым пробелом исходной строки. Если строка
#содержит только один пробел, то вывести пустую строку.
str = "hello world dota 2"
perviy_probel = str.find(' ') + 1 
vtoroy_probel = str.find(' ', perviy_probel)
if vtoroy_probel != -1:
    print (str[perviy_probel:vtoroy_probel])