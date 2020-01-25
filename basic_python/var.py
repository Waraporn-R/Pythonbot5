#ส้ม = 3 ลูก มะนาว = 5 ลูก
# ส้ม = 3
# มะนาว = 5
# มะม่วง = 10
# ค่าแรงโน้มถ่วง = 9.8
# var1 = ส้ม / มะนาว
# var2 = ส้ม + มะนาว

# #string ตัวอักษรทั่วไป
# var3 = "ส้ม + มะนาว = "

# print("ส้ม + มะนาว = " ,var2) #แสดงผลเป็น "ส้ม + มะนาว = 8"

#Corona ไวรัส in thailand
# ไวรัส = "Corona"
# country = "thailand"
# sentence = ไวรัส + " ไวรัส in " + country
# print(sentence)
# country = "japan" 
# print(ไวรัส , " ไวรัส in " , country)

#list        index = 0     index = 1     index = 2   index = 3
#list        index = -4     index = -3   index = -2  index = -1
# viruses = ["Corona SARS","Corona MERS","Corona Wuhan","HIHV"]
# countries = ["ThaiLand","Japan","China","England"]
# print("ไวรัสที่พบในโลก : ",ไวรัส)
# print("ถูกพบในประเทศ : ",country)
#ไวรัส ..... เกิดขึ้นที่ประเทศ .....
# for virus,country in zip(viruses,countries): #state
#     print("ชื่อไวรัส : ",virus ,"เกิดขึ้นที่ประเทศ : ",country)
# new_virus = "ตับอักเสบ B"
# viruses.append(new_virus)
# print(viruses)
# viruses.pop(-1)
# print(viruses)
# print(viruses[-1])
# print(viruses[1:3])
# for character in new_virus:
#     print(character)
# for i in range(len(viruses)):
#     print("index  : ",i)
#     print("ชื่อไวรัส : ",viruses[i])

## virus .... ระบาดในประเทศ ..... จำนวนคนที่ติดเชื้อ ....จำนวนคนเสียชีวิต
# dictionary
                #key  value  pair
# Example_Dict = {"แมว":"Cat",
#                 "สุนัข":"Dog",
#                 "ปลา":"Fish"}

# print(Example_Dict["ปลา"])
# Example_Dict["นก"] = "Bird"
# print(Example_Dict)


# for ชื่อภาษาไทย , ชื่อภาษาอังกฤษ in Example_Dict.items():
#     print("ภาษาอังกฤษของคำว่า :" ,ชื่อภาษาไทย ,"คือ",ชื่อภาษาอังกฤษ)

## "virus .... ระบาดในประเทศ ..... จำนวนคนที่ติดเชื้อ ....จำนวนคนเสียชีวิต"
Virus_database = {
                    "Corona SARS" : {"ระบาดใน":"ไทย" 
                                  , "จำนวนคนที่ติดเชื้อ" : 100 
                                  , "จำนวนคนเสียชีวิต" : 20 }
                    ,"Corona MERS" : {"ระบาดใน":"ญี่ปุ่น" 
                                  , "จำนวนคนที่ติดเชื้อ" : 80 
                                  , "จำนวนคนเสียชีวิต" : 10 }
                }

# for key,value in Virus_database.items():
#     print(key)
#     print(value["ระบาดใน"])

new_virus = {"ระบาดใน":"จีน"
                     , "จำนวนคนที่ติดเชื้อ" : 1000 
                     , "จำนวนคนเสียชีวิต" : 40 }

Virus_database["Corona wuhan"] = new_virus
# print(Virus_database["Corona wuhan"])

#while loop 
# if else

# ติดเชื้อ = "ติดเชื้อ"  #boolean True False  # 0 =ติดเชื้อ , 1 = ไม่มีเชื้อ , 2 = ยังไม่ตรวจ

# if ติดเชื้อ == "ติดเชื้อ":
#     print("ติดต่อ รพ. โดยด่วน")

# elif ติดเชื้อ == "ไม่ติดเชื้อ": #false
#     print("คุณไม่มีเชื้อโรค")

# else:
#     print("ยังไม่ได้ตรวจสอบ")
# ติดเชื้อ = True
# while True:
#     รับยา = input("ท่านต้องการรับยาแก้เชื้อหรือไม่ (Yes(Y)/No(N))")
#     if รับยา == "Y":
#         print("คุณได้รับยาแก้เชื้อโรค")
#         # ติดเชื้อ = False
#         break
    
#     else :
#         print("กรุณารับยารักษาก่อนคะ")


