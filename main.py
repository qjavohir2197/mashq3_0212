#1-misol
has_a = lambda name: "a" in name.lower()

ism = input("Ismingizni kiriting: ")
print(has_a(ism))

#2-misol
capitalize_first = lambda s: s.capitalize()

matn = input("Matn kiriting: ")
print(capitalize_first(matn))

#3-misol
mod_faq = lambda x, y: abs(x - y)

a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))

print(mod_faq(a, b))

#4-misol
ikki_son = lambda a, b: a == b and a != b

x = int(input('1-sonni kiriting: '))
y = int(input('2-sonni kiriting: '))

print(ikki_son(x, y))

#5-misol
half_int = lambda x: x // 2

son = int(input("Son kiriting: "))
print(half_int(son))
