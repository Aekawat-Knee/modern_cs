while True:
    user_input = input("โปรแกรมตรวจคะแนน กด Q เพื่ออกจากกลุ่ม หรือกดอื่นๆดำเนินการต่อ : ")
    
    if user_input.lower() == 'q':
        print("ออกจากลูปแล้ว!")
        break
    fname = input("First Name is : ")
    last_name = input("Last Name is : ")
    inp = int(input("input Point : "))

    if(inp >= 80):
        print(fname, last_name, " Grade A")
    elif(inp >= 70):
        print(fname, last_name, "Grade B")
    elif(inp >= 60):
        print(fname, last_name, "Grade C")
    elif(inp >= 50):
        print(fname, last_name, "Grade D")                
    else:
        print(fname, last_name, "Grade E")    