do_you_want_to = input("Do you want to create a character (yes or no) ")

if do_you_want_to =="yes":
        print("Well let's do it")
        name = input("Well let's start with a name, what's your name? ")
        print(name, "That's a very nice name you got there ")
        age = input("Okay now we need his age what's it gonna be ")
if (age > "10") :
        print("Age", age, "for", name, "that's nice and mature of you")

elif(age < "10"):
        print("A quite young age for", name, ",so far at age", age)

else:
        print("Try that again")        

socialism = input("Now his type of socialism? (introvert or extravert) ")

if socialism == "introvert":
        print("So you consider him being alone that's fine")

elif socialism == "extravert":
        print("Wow you do like", name, "being very social that's quite good")

else:
        print("Try that again")

smarts = input("Now let's see how smart you want him to be (very smart or dumb) ")
        
if smarts == "very smart":
        print("Wow", name, "being", smarts, "with", socialism, "socialism that's nice")

elif smarts == "dumb":
        print("Okay I wouldn't prefer", name, "being", smarts)

else:
        print("Try that again")

print("So now here's a check so far")
print("Name:", name, "Age:", age, "Socialism:", socialism, "Smarts:", smarts)







        

    
