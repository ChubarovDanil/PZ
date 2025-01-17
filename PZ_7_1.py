#Дан символ C и строки S, S0. После каждого вхождения символа C в строку S
#вставить строку S0.

def zamena_simvolov(S, C, S0):
    # Заменяем каждый символ C на C + S0
    result = S.replace(C, C + S0)
    return result

S = "hello world"
C = "o"
S0 = "123"

izmenennaya_stroka = zamena_simvolov(S, C, S0)
print("Измененная строка", izmenennaya_stroka)