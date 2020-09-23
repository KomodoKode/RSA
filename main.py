"""
The Key Generation for this implementation of RSA

Possible Encryption/Decryption methods in the future
As said in the README.MD, this version of RSA is not
secure for commercial use. Do not use this to actually
send private messages between two or more individuals.
"""

import secrets
from Primes import GetRandPrime

class KeyGenerator:
  
  def __init__(self): 
    self.rng = secrets.SystemRandom()
  
  def generate_RSAkeys(bits, pub_e=65537):
    self.pub_e = pub_e
    if bits > 1024:
      raise NotImplementedError("Prime Numbers cannot currently be over 1024 Bits")
    self.p1 = GetRandPrime(bits)
    self.p2 = GetRandPrime(bits)
    self.pub_key = p1 * p2
    #Key Creation
    self.phi_pubkey = (p1 - 1) * (p2 - 1)

    self.priv_key = pow(self.pub_e, -1, self.phi_pubkey)

    """
    Calculates the modular
    inverse of e and phi_n.
    This feature is only in
    Python 3.8+, so I will
    be making a Python 3
    general version in this
    repository soon.
    """

    #Map of keys to not confuse keys
    self.key_map = 
    {"public key" : self.pub_key,
     "pub_e" : self.pub_e,
     "private key": self.priv_key}

     return self.key_map

  def Derive_SecretKey(encrypted_skey):
    """This function derives a key from a encrypted key given
    by using the Encrypt_SecretKey() method."""

    SecretKey = pow(encrypted_skey, self.priv_key, self.pub_key)
    self.skey = SecretKey
    keymap.update({"secret key" : self.skey})
    return SecretKey
    
  def GetHexValues(values="all"):
    """Gets the hexidecimal values of the keys
    default value is all values, but can be changed
    to the key values"""
    if values = "all":
      hex_keymap = {}
      for i in self.keymap:
        hex_keymap.update({i, self.keymap[i]})
      self.hexkeys = hex_keymap
      return hex_keymap
      
  def Encrypt_SecretKey(bits):
    """Generates a secret key for using in exchange.
    Since this value is special and isn't saved as a
    class variable, it automatically presents the hex
    value of the key"""
    secretkey = elf.rng.getrandbits(bits)
    return secretkey, hex(secretkey)




