# Takes a potential VIN as input and returns whether it's valid or not
# Only works for North American VINs

nums = "0123456789"
letters = "abcdefghjklmnprstuvwxyz"

def transcribe_vin(vin):
    numvin = [] 
    for x in vin:
        if x in nums:
            numvin.append(ord(x)-48)
        if x in letters:
            nval = (ord(x)-96) % 9
            if nval == 0:
                nval = 9
            numvin.append(nval)
    if len(numvin) != len(vin):
        print("uh oh")
        return("eek")
    return(numvin)

def check_digits(vin):
    vin = vin.lower()
    if len(vin) == 17:
        for i in range(0,17):
            if i == 8:
                if vin[i] not in nums:
                    print("digit 9 nonint")
                    return(0)
            else:
                if vin[i] not in nums+letters:
                    print("digit invalid at position ")
                    print(str(vin[i]))
                    return(0)
        numvin = transcribe_vin(vin)
        factorweights = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
        weightsum= sum([numvin[i]*factorweights[i] for i in range(0,17)])
        if numvin[8] == (weightsum % 11):
            return(1)
        else:
            print("invalid checksum")
            return(0)
    else:
        print("wrong length")
        return(0)

