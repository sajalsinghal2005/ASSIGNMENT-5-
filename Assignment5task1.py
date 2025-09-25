d1 = {'Sajal' : 100 , 'Alice' : 85 , 'Bob' : 80 , 'John' : 70}
key_to_check = input("Enter a Student Name : ")


if key_to_check in d1:
    print(f"{key_to_check} marks : {d1[key_to_check]}")
else:

    print("student not found")