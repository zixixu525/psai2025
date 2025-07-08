import operator
user_input,ops,bag1, bag2,target,actual_bag1=input("enter a operator:"),{'==': operator.eq,'!=': operator.ne,'<': operator.lt,'<=': operator.le,'>': operator.gt,'>=': operator.ge},[1,2,3,4,5],[1,2],4,[]
for b1 in bag1:
    if any(ops[user_input]((b1+b2),target) for b2 in bag2):
        actual_bag1.append(b1)
print(actual_bag1)
