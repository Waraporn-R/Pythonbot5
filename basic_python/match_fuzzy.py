# print(1+1) #2
# def add(num1 , num2):
#     print("คุณได้ทำการบวกเลข 2 ตัว คือ {} และ {}".format(num1,num2))
#     result = num1+num2
#     print("ผลลัพธ์คือ {}".format(result))
#     return result

# ผลลัพธ์ = add(num1=5,num2=10)
# print(ผลลัพธ์)

from fuzzywuzzy import process
def match_fuzzy(text,text_list,score):
    Ratio = process.extractOne(text,text_list)
    print(Ratio)
    if Ratio[1] > score:
        return Ratio[0]
    else :
        return False
    
# str2Match = "apple inc"
# strOptions = ["Apple Inc.","apple park","apple incorporated","iphone"]

# print(match(text=str2Match,text_list=strOptions,score=50))
