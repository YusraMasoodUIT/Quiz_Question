print("Yusra Masood ")
print("18B-093-CS (A)")
print("Quiz Question")
print("\n")

def cost():
    cups = int(input("How many cups of tea do you want to purchase "))
    cost = 25 * cups
    print("Your total bill is " +str(cost)+"Rs")
    print("\n")
    amount = int(input("Please Enter your amount "))
    print("\n")
    while amount < cost:
        print("You've entered "+str(amount)+ "Rs")
        diff = cost - amount
        print("You've to pay " +str(diff)+ "Rs more ")
        print("\n")
        amount1 = int(input("Please Enter your amount "))
        print("\n")
        amount = amount + amount1

        if amount >= cost:
            break

    if amount == cost: 
        print("You've entered "+str(amount)+ "Rs")
        print("\n")
        print("Your change is 0Rs , Thankyou for purchasing "+str(cups)+" cups of tea")

    if amount > cost:
        print("You've entered "+str(amount)+ "Rs")
        print("\n")
        diff1 = amount - cost
        
        total = 0
        print("Your change is :- ")

        if diff1 >= 5000:
            fth = diff1 // 5000
            diff1 = diff1 % 5000
            tot = fth * 5000
            total = total + tot
            print(str(fth)+" * 5000Rs note(s) = "+str(tot))
        if diff1 >= 1000:
            th = diff1 // 1000
            diff1 = diff1 % 1000
            tot = th * 1000
            total = total + tot
            print(str(th)+" * 1000Rs note(s) = "+str(tot))
        if diff1 >= 500:
            fhun = diff1 // 500
            diff1 = diff1 % 500
            tot = fhun * 500
            total = total + tot
            print(str(fhun)+" * 500Rs note(s) = "+str(tot))
        if diff1 >= 100:
            hun = diff1 // 100
            diff1 = diff1 % 100
            tot = hun * 100
            total = total + tot
            print(str(hun)+" * 100Rs note(s) = "+str(tot))
        if diff1 >= 50:
            fif = diff1 // 50
            diff1 = diff1 % 50
            tot = fif * 50
            total = total + tot
            print(str(fif)+" * 50Rs note(s) = "+str(tot))
        if diff1 >= 20:
            twn = diff1 // 20
            diff1 = diff1 % 20
            tot = twn * 20
            total = total + tot
            print(str(twn)+" * 20Rs note(s) = "+str(tot))
        if diff1 >= 10:
            ten = diff1 // 10
            diff1 = diff1 % 10
            tot = ten * 10
            total = total + tot
            print(str(ten)+" * 10Rs note(s) = "+str(tot))
        if diff1 >= 5:
            five = diff1 // 5
            diff1 = diff1 % 5
            tot = five * 5
            total = total + tot
            print(str(five)+" * 5Rs coin(s) = "+str(tot))
        if diff1 >= 2:
            two = diff1 // 2
            diff1 = diff1 % 2
            tot = two * 2
            total = total + tot
            print(str(two)+" * 2Rs coin(s) = "+str(tot))
        if diff1 >= 1:
            one = diff1 // 1
            tot = one * 1
            total = total + tot
            print(str(one)+" * 1Rs coin(s) = "+str(tot))
            
        print("\n")
        print("Your return is "+str(total)+"Rs, Thankyou for purchasing "+str(cups)+" cups of tea")
      
        



cost()
