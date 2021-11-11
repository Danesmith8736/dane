first_numb =input ("first_numb:")
second_numb =input ("second numb:")
operator =input ("operator:")

def operate (first_numb, second_numb, operate):
    if operate == "+":
        result = first_numb + second_numb
        return result
    if operate == "-":
        result = first_numb - second_numb
        return result
    if operate == "/":
        result = first_numb / second_numb
        return result
    if operate == "*":
        result = first_numb * second_numb
        return result

result=operate (int(first_numb), int (second_numb), operator)
print (result)