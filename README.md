### **Simple Password Validator:**



##### **Project Title**

Simple Password Validator using Python



##### **Description**

This project is a simple Python program that checks whether a password satisfies basic validation requirements.



##### **The program checks:**

* Minimum password length of 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one digit
* At least one special character



**Objective:**

The objective of this project is to practice:

* Python strings
* input()
* len()
* for loop
* if conditions
* String methods such as isupper(), islower(), and isdigit()
* Basic validation using counters

###### 

###### **Technologies Used**

\- Python



###### **How the Program Works**

1\. The user enters a password.

2\. The program counts uppercase letters, lowercase letters, digits, and special characters.

3\. The program checks the password length.

4\. The program verifies all required conditions.

5\. If all conditions are satisfied, it displays "Password is valid".

6\. Otherwise, it displays "Password is invalid".



###### **Program Code**

password = input("Enter password: ")



u = 0

l = 0

d = 0

s = 0

sp = "!@#$\_"



n = len(password)



for i in password:



&#x20;   if i.isupper():

&#x20;       u = u + 1



&#x20;   if i.islower():

&#x20;       l = l + 1



&#x20;   if i.isdigit():

&#x20;       d = d + 1



&#x20;   if i in sp:

&#x20;       s = s + 1



if n >= 8 and u > 0 and l > 0 and d > 0 and s > 0:

&#x20;   print("Password is valid")

else:

&#x20;   print("Password is invalid")



###### **Validation Rules**

**Requirement**	         **Condition**

Minimum length	        8 characters

Uppercase	        At least 1

Lowercase	        At least 1

Digit	                At least 1

Special character	At least 1



###### **Sample Output**

**Valid Password**

Enter password: Hello@123

Password is valid



**Invalid Password**

Enter password: hello123

Password is invalid



**Special Characters Used**

The program accepts:

! @ # $ \_



###### **Conclusion**



This project demonstrates basic password validation using Python loops, conditions, counters, and string methods.







