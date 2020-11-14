# Greatest Common Divisor function
def gcd(a,b):
    if a==0: return b
    return gcd(b%a, a)

# Check prime number function
def isPrime(n):
    if(n<2): return False
    elif (n==2): return True
    else:
        for x in range(2,n):
            if(n%x==0): return False
        return True

# generate keys for RSA
def generate_keys(p, q):
    n = p*q                                # Common key
    m = (p-1)*(q-1)                        # Totient function
    e,d = 2,1                              # initial values of encrypt and decrypt keys

    while e<m:                             # generate encrypt key
        if gcd(e,m) == 1: break
        else: e+=1

    while ((e*d)%m)!=1: d+=1               # generate decrypt key

    return [(e,n), (d,n)]

# Encrypt function
def encrypt(message):
    pub_key, pri_key = generate_keys(p,q)
    e,n = pub_key
    d,n = pri_key
    return pow(message,e,n)

# Decrypt function
def decrypt(code, d, n):
    return pow(code,d,n)

# Main function
if __name__ == '__main__':
    print("RSA encrypt-decrypt")
    print("Encrypt:(e)\nDecrypt:(d)")
    choice = input("Enter you choose: ").lower()
    if choice == 'e':
        try:
            p = int(input("Enter 1st prime no. (p): "))
            q = int(input("Enter 2nd prime no. (q): "))
            if isPrime(p) and isPrime(q):
                message = int(input("Enter the message: "))
                pub_key, pri_key = generate_keys(p,q)
                print("Public key: ",pub_key)
                print("Private key: ",pri_key)
                print("Encrypt code: ",encrypt(message))
            else: print("Please enter a valid prime integer no.")
        except: print("Please enter a valid integer no.")
    elif choice == 'd':
        try:
            code = int(input("Enter the decrypt code: "))
            d = int(input("Enter the 1st private key (d): "))
            n = int(input("Enter the 2nd private key (n): "))
            print("Decrypt message: ",decrypt(code,d,n))
        except: print("Please enter a valid integer no.")
    else: print("Invalid choice")
