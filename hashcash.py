# PART 1

import random
import string
import sys
from hashlib import sha256

def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
  split_token = token.split(':')
  if int(split_token[0]) != 1:
    return False
  else:
    VERSION = 1
  
    if len(date) > 6 or date != split_token[1]:
      return False
    else:
      DATE = int(date)
  
      if email != split_token[2]:
        return False
      else:
        EMAIL = email
        
        if len(split_token[-1]) <= 16:
          if binary_leading_0s(sha256(token.encode()).hexdigest()) == difficulty:
            NONCE = split_token[-1]
            return True
          else:
            return False
        else:
          return False

# PART 2

def get_random_string(length: int) -> str:
  chars = string.hexdigits[:16]
  string_to_convert = ''.join(random.choice(chars) for i in range(length))
  return string_to_convert


def minter(date: str, email: str, difficulty: int) -> str:
  VERSION = str(1)
  DATE = date
  EMAIL = email
  
  range_stop = 16
  NONCE = get_random_string(range_stop)
  token = VERSION + ':' + DATE + ':' + EMAIL + ':' + NONCE
  return token, DATE, EMAIL, difficulty

def mint(date: str, email: str, difficulty: int) -> str:
  state = False
  while state == False:
    token, d, e, diff = minter(date, email, difficulty)
    if is_valid(token, d, e, diff):
      state = True
    else:
      state = False
  return token

print(mint('081031', 'satoshin@gmx.com', 20))