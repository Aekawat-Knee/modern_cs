stack = []
pairs = { ')':'(',']':'[','}':'{' }

opens = set(pairs.values())
expr = input("Enter expression with brackets: ")
valid = True
for ch in expr:
    if ch in opens:
        stack.append(ch)
        print("push : ", ch, " stack : ", stack)

    elif ch in pairs:
        if not stack:
            print("Error : stack empty bu found clossing brackst" , ch)
            valid = False
        
        top = stack.pop()
        print("pop : ", top, "for clossing " , ch, " stack : ", stack)

        if top != pairs[ch]:
            print("Error: bracket not match -> ", top , " vs ", ch )
            valid = False
            break

# -----------------------------
# ฟังก์ชันคำนวณ
# -----------------------------
def precedence(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    return 0


def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b


def calculate(expr):
    values = []
    ops = []
    i = 0

    while i < len(expr):

        # ข้ามช่องว่าง
        if expr[i] == ' ':
            i += 1
            continue

        # รองรับเลขติดลบ
        if expr[i] == '-' and (i == 0 or expr[i-1] == '('):
            num = '-'
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            values.append(float(num))
            continue

        # ถ้าเป็นตัวเลข
        if expr[i].isdigit():
            num = ""
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            values.append(float(num))
            continue

        # ถ้าเป็น (
        elif expr[i] == '(':
            ops.append(expr[i])

        # ถ้าเป็น )
        elif expr[i] == ')':
            print(expr[:i+1])
            while ops and ops[-1] != '(':
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                result = apply_op(a, b, op)
                print(f"{a} {op} {b}")
                print("=", result)
                values.append(result)
            ops.pop()

        # ถ้าเป็น operator
        elif expr[i] in "+-*/":
            while (ops and precedence(ops[-1]) >= precedence(expr[i])):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                result = apply_op(a, b, op)
                print(f"{a} {op} {b}")
                print("=", result)
                values.append(result)
            ops.append(expr[i])

        i += 1

    # ทำส่วนที่เหลือ
    while ops:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        result = apply_op(a, b, op)
        print(f"{a} {op} {b}")
        print("=", result)
        values.append(result)

    return values[0]

if valid:
    if stack:
        print("Error : still ", stack)
        valid = False

if valid:
    print("result : valid")
else:
    print("result : invalid")

if valid:
    final = calculate(expr)
    print("Final Result =", final)
else:
    print("Invalid brackets")