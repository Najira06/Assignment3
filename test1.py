text = input("Enter a sentence: ")
broken = input("Enter the broken letter: ")
for char in text:
    if char == broken:
        print ("Can Not Type")
        break
    else:
        print ("Can Type")

