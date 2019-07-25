def asalMi(say):
    if(say < 2):
        raise ValueError("Girdiğiniz sayı en az 2 olmalıdır!!!")
    else:
        for i in range(2,say):
            if((say%i) == 0):
                return False
        return True


print("Çıkmak için q 'e basın! '")
while True:
    say = input("Sayı giriniz: ")
    if(say == "q"):
        print("By By..")
        break
    elif(asalMi(int(say))):
        print("Sayımız asal sayıdır.")
    else:
        print("Asal değil")
