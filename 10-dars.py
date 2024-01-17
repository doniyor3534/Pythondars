# while orqali 1 dan 10 gacha bolgan sonlarni chiqaramiz
# son = 1
# while son < 100:
#     son +=1
#     print(son)


# promo code tayorlash //////////////////////////////////////////////////////

# from random import randint

# kodlar = [132,135,130,134]  #lists
# yangi_code = randint(130,135)

# while yangi_code in kodlar:
#     yangi_code = randint(130,135)

# print(yangi_code)




# /////////////Password code tayyorlash 2///////////////////////////////////////
# from random import choice
# codes = "qwertyuioplkjhgfdsazxcvbnm1234567890"
# lits = ["4qf5p27s2p","qiioipoby5","eyh6zh7qjh"]
# yangi_code = ''
# for x in range(1,11):
#         yangi_code += choice(codes)

# while yangi_code in lits:
#     for x in range(1,11):
#         yangi_code += choice(codes)
    

# print(yangi_code)



# //////kiritilgan sonni agar son bolmasa xatolik chiqadi
# son = input('malumot kiriting : ')
lestining = 'Xatolik !!!'

c = False
while c != True:
    son = input('malumot kiriting : ')
    if son.isdigit():
        print("Rahmat !!!")
        c = True
    else:
        print("XAtolig !!!")
        c = False
 


