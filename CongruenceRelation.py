## -------------------- Congruence Relation -------------------- ##

#Returns True or False, baced on weather the modulo n of a and b is same
def ConRel(a,b,n):
    if a % n == b % n:
        return True
    else:
        return False

if __name__ == '__main__':
    for i in range(-9,21):
        if ConRel(i,4,6):
            print(str(i) + ": True")