# capitalize()
# title()
# upper()
# lower()
# split()
# join()

data = "hello world"
result = data.capitalize()
print(result)  # "Hello world"


result = data.title()
print(result)  # "Hello World"

result = data.upper()
print(result)  # HELLO WORLD

result = data.lower()
print(result)  # hello world


data = "hello world"
result = data.split()
print(result)  # ["hello", "world"]

data = "hello+world"
result = data.split("+")
print(result)  # ["hello", "world"]

result = data.split("o")
print(result)  # ["hell", "+w", "rld"]

result = data.split("l")
print(result)  # ["he", "", "o+wor", "d"]


# join()
data = ["hello", "world"]
result = " ".join(data)  # data.join(" ")
print(result)  # hello world

result = "+".join(data)
print(result)  # hello+world