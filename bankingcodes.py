x=input("Enter a name: ")
print(x)
post_x=input("Enter the post of the person: ")
print(post_x)
salary=int(input("Enter salary of the person per day: "))
print(salary)
days=int(input("ENTER NUMBER OF DAYS HE WORKED: "))
print(days)
if post_x=="manager":
    sal=200*days
elif post_x=="leader":
    sal=150*days
elif post_x=="teammember":
    sal=100*days
print(sal)
overtime=int(input("Enter time he worked more: "))
print(overtime)
bonus=salary*days*overtime
print(bonus)