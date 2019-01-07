#!/usr/bin/env python
from random import randint

# number of iterations for Fermat primality test
accuracy = 5

class Key:
    def __init__(self, key=()):
        self.private = None
        self.public = None
        
    def __str__(self):
        s = "====PUBLIC====\n(%x, %x)\n====END PUBLIC=====\n" %(self.public[0], self.public[1])
        s += "====PRIVATE====\n(%x, %x)\n====END PRIVATE=====" %(self.private[0], self.private[1])
        return s
        

class RSA:
    def __init__(self):
        return
        
    def __del__(self):
        return
        
    def __str__(self):
        return
        
    def generate_key(self, length):
        # p and q have length of length/2 each
        p = randint(2**(length-1), 2**length-1)+1
        q = randint(2**(length-1), 2**length-1)+1
        while not self._is_prime(p):
            p = randint(2**(length-1), 2**length-1)
            
        while not self._is_prime(q):
            q = randint(2**(length-1), 2**length-1)
            
        n = p*q
        f = (p-1)*(q-1)
        
        e = self._generate_e(f)
        d = self._generate_d(e, f)
        
        key = Key()
        key.private = (d,n)
        key.public = (e,n)

        return key
        
    def encrypt(self, message, key):
        cipher = [pow(ord(char),key[0],key[1]) for char in message]
        return cipher
                
        
    def decrypt(self, cipher, key):
        plain = ''.join([chr(pow(char,key[0],key[1])) for char in cipher])
        return plain

        
    def _is_prime(self, number):
        for i in range(2, accuracy+1):
            if pow(i, number-1, number) != 1:
                return False
        return True
        
    def _gcd(self, a, b):
        while b!=0:
            a, b = b, a%b
        return a
        
    def _are_coprimes(self, num1, num2):
        return self._gcd(num1, num2)==1
        
    def _generate_e(self, f):
        e = 2**16 + 1
        while not self._are_coprimes(e, f):
            e = randint(2, f-1)
        return e
        
    def _generate_d(self, e, f):
        return self._mmi(e, 1, f)
       
    """ Solves congruence ax=b (mod n) using Extended Euclid Algorithm"""
    def _mmi(self, a, b, n):
        y0, y1 = 0,1
        r = a # rest
        d = n # divisor
        while r != 1:
            q, d, r = d/r, r, d%r
            y0, y1 = y1, y0-q*y1
        return b*y1%n


if __name__ == '__main__':
    r = RSA()
    
    k = r.generate_key(1024)
    message = raw_input("message: ")

    #print k

    cipher=r.encrypt(message, k.public)
    plain =r.decrypt(cipher, k.private)
    print cipher
    print plain



