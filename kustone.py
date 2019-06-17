# App in ra day so cong tru ngau nhieu cho ku stone hoc toan
# vi du nhu la 4 + 5 - 2 = ketqua chay 5 dong
# day so khong qua 9
import random
print('KIỂM TRA TOÁN SOROBAN CHO KU STONE MẬP ĐỊCH ')
i = 0
while (i<5):
    so1 = 5
    random_num = random.randint(1, 3)
    congtru = random.choice(['+', '-', ])
    ketqua = eval(str(so1) + congtru + str(random_num) + congtru + str(random_num))
    print('Dãy số ku Stone : ', so1, " ",congtru," ",random_num,"",congtru," ",random_num, " = ",ketqua)
    i = i + 1
