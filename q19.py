name="Sudhir Yadav"
age= 24
city= "Delhi"

str1="My name is %s, I am %a old, and I live in %s"%(name, age, city)
print(str1)

str2=f"My name is {name}, I am {age} old, and I live in {city}"
print(str2)

str3="My name is {}, I am {} old, and I live in {}".format(name, age,city)