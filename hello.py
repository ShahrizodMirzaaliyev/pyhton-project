



#bollen operatori yani mantiqiy ammallar: bajaradigan ishi mantiqiy amallarni katta va kichik sonlarni aniqlaydi

# a = True
# b = False



# print(5 == 5)#5 teng beshgabu True yani togri degani agar 5 teng olti bolgani bu False bolgan bolar edi
#ozgaruvchilar  biror bir nom ostidagi biror bir qiymatni uzgartirishda qayta tisklashda yordam beradi
#masalan


# x = 10
# print(x)# hozir a uzgaruvchi 10 qiymatda bolib turibdi agar uni
# x = 15
# print(x)#ana endi a uzgaruvchi 15 qiymatiga ega boldi
#Shart Operatori if va else bularnign vazifasi agar beriladigan son haqiqatdan bu songa teng bolsa yoki undan katta
#bolsa uni ekranga chiqaradi yani shu shartni qoyadi boleen operatori bilan uzvi bogliq

#if else shart operatorlari boleen operatori bilan uzvi bogliq siz misol yozdingiz agar u togri bolsa udastur uni
#ekranga chiqaradi yani togri bosa chiqaraman bolmasa yoq yoki notogri yozuvini yani ifni emas else ni chiqaraman deb
#shart qoyadi


# x = input('x = ')
# y = input('y = ')
# if x > y:
#  print('x')
# elif x < y:
#   print('y')
#else:
#   print('not number')

# age = int(input('yoshingizni kiriting'))
# if age >= 18:
#    print('Siz Ovoz berishga haqlisiz')
# elif age < 18:
#    print('coming nex year')


# foydalanuvchijavobi = int(input('7 * 8 ='))
# if foydalanuvchijavobi == 56:
  #  print('siz togri topdingiz')
#else:
  #  print('Afsus siz topa olmadingiz')







    #mantiqiy operatorlar and va or biz bilamizki misol yechoyatgan paytimizda 1 emas 2 yoki 3ta masala bir qatorda
    #keladi aynaan mana shunday misollar and va or yordamida yasaladi
#print(not 2 == 2)
#print(not 2 != 2)



#i = 1
#fact = 1
#n = int(input("N = "))

#while i <= n:

 #   fact = fact * i
  #  i = i + 1
#print(str(n) + "!=" + str(fact))






#cars = ["Spark", "Kaptiva", "Malibu"]
#empty_list = []
#print(empty_list)

#x = ["Biznign kurslar:","1.Android va Kotlon","2.Php,Python,C++,C#","3. visual studio","4.Unity",
#                    "Mana shular",[5, 6, 7]]
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])


# while takrorlash operatori nomidan korinib turibdiki bu operator yozilaga ozgaruvchi yoki biror bir narsani

# takrorlasda yordam beradi



# num = "programmer shahrizod"

# num = [1, 2, 3, 4, 5]
# print(num)
# num[3] = 30
# print(num * 2)

# raqamlar = [1,2,50,4]

# raqamlar.append(5) #listga qoshish
# uzunlik = len(raqamlar) # eng uzun sonni topish
# raqamlar.append(50)
# raqamlar.insert(1, 55)
# print(raqamlar.index(55))
# print(max(raqamlar))
# print(min(raqamlar))
# print(raqamlar.count(50))
# raqamlar.remove(50)
# raqamlar.remove(50)
# print(raqamlar)

# raqamlar = list(range(15, 40, 3))
# print(raqamlar)
# print(range(20) == range(0, 20))
# raqamlar.reverse()
# print(raqamlar)

# for - Loop - Progrrammer Shahrizod

# cars = ["malibu", "Spark", "Captiva"]
# for number in range(10):
#    print(number)

# a = [1, 2, 3, 4, 5]
# print(a)


# counter = 0 # 0,1,2,

#while counter < len(cars):
   # car = cars[counter]
   # print(car)
   #  counter = counter + 1

#functions - Programmer Uz
#code reuse

#DRY principle - Don't Repaet yourself

#WET principle - Write Everything Twise - We Enjoy Typing...

# def programmer(word):
#    print("s " + word)

# programmer("hello")

#print('kiritilgan sonning kvadratini topuvchi dastur')
#savol = "istalgan son kiriting va enter tugmasini bosing"
#savol += " dasturni tugatish uchun 'exit' deb yozing"


#while True:
 #   qiymat = input(savol)
  #  if qiymat == '1000':
   #     break
    #else:
     #   print(float(qiymat)** 2)
#print('dastur tugadi')
input("keling bir o'yin oynaymiz unig nomi O'ylagan sonimni top. Boshlash uchun '1' deb yozing")
print('men bir 10 lik sonlar orasidan bitta son oyladim. Uni topishga harakat qilib koring')
x = int(input('raqam kiriting'))
if x == 5:
    print('Siz men oylagan sonni topdingiz. Tabriklaymiz')
    print('yana uynashni istaysizmi Yana uynamoqchi bolsangiz. Endi siz oylang men topaman. Boshlash uchun "1" deb yozing')
    input('raqam kiriting')
elif x <= 5:
    print('siz men oylagan sondan kichigini topdingiz sizdan 1 ta imkoniya ketti')
    x = int(input('Raqam kiriting'))

    if x == 5:
        print('Siz men uylagan sonni topdingiz.Tabriklaymiz')

    elif x <= 5:
        print('siz yana Topa olmadingiz')
        x = int(input('raqam kiriting'))
        if x == 5:
            print('siz topdingiz barakalla. Uyin tugadi')
    elif x <= 5:
        print('siz men oylagan sondan kichigini topdingiz sizdan 1 ta imkoniya ketti')
        x = int(input('Raqam kiriting va ohirga imkoniyat'))
        if x == 5:
            print("ana endi topdingiz. Tabriklaymiz")
        elif x <= 5:
            print('sizda yana hatolik uyin tugadi. Men uylagan son 5 edi')
        elif x >= 5:
            print('Sizda oxirgi imkoniyat ham ketti uyin tugadi. Men uylagan son 5 edi')

    elif x >= 5:
        print('siz yana notugri topdingiz 2chi imkoniyat ham ketti')
        x = int(input('raqam kiritng'))
        if x == 5:
            print('Siz endi topdingiz Uyin tugadi')
        elif x <= 5:
            print('siz yana topa olmadingiz.Men uylagan son 5 edi')
        elif x >= 5:
            print('sizda oxirgi imkoniyat ham puchga chiqdi. Uyin tugadi. Men uylagan son 5')






elif x >= 5:
    print('siz men oylagan sondan kattasini yozdingiz 1 ta imkoniya ketti')
    x = int(input('Raqam kiriting'))
    if x == 5:
        print('Siz togri topdingiz. Tabriklaymiz.Uyin Tugadi. Men uylagan son chindan ham 5 edi ')

    elif x <= 5:
        print('Sizda yana notogri son kiritdingiz. Qayta urinib koring')
        x = int(input('raqam kiriting'))
        if x == 5:
            print('Siz endi togri topdingiz. Uyin tugadi. Men uylagan son chindan ham 5 edi')
        elif x <= 5:
            print('siz men uylagan sonni topa olmadingiz. Uyin tugadi. Men uylagan son 5 edi')
        elif x >= 5:
            print('Siz yana topa olmadingiz. Uyin tugadi. Me uylagan son 5 edi')


    elif x >= 5:
        print('siz yana notogri son yozdingiz.Qayta urinib koring')
        x = int(input('raqam kiriting'))
        if x == 5:
            print('Siz endi togri topdingiz. Men uylagan son chindan ham 5 edi')
        elif x <= 5:
            print('Siz men uylagan sonni topa olmadingiz.Uyin tugadi. Men uylagan son 5 edi')
        elif x >= 5:
            print('Sizda Hatolik. uyin tugadi. Men uylagan son 5 edi')


else:
    print('siz juda kattta son yozdingiz')








