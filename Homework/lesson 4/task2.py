phone_number: str = "8050222333"
if phone_number.isdigit() and 11 < len(phone_number):
    print("error")
elif phone_number.isdigit() and 9 > len(phone_number): #якщо написати замість "and" - "not", то  "len"  пропадає, why?
    print("try one more")
elif phone_number.isdigit() or 10 <= len(phone_number):
    print("correct")


phone_number = str(input('phone numbers'))
if phone_number.isdigit() and 11 <= len(phone_number):
    print("not correct")
elif phone_number.isdigit() and 9 >= len(phone_number):
    print("try one more")
elif phone_number.isdigit() and 10 == len(phone_number):
    print("correct")




