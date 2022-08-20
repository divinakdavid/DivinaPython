age = int(input("How old are you?\n"))

decades = age // 10
years = age % 10

# special operator for whole number divison = //
# % is called modulus

print("You are " + str(decades) + " decade(s) and " + str(years) + " years old.")