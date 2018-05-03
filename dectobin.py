def binconv(broj):


    if broj > 1:
        rem= broj %2
        broj= broj //2
        return binconv(broj) + str(rem)
    else:
        return str(broj)

print(binconv(5.4))