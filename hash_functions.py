from hashlib import md5
import random
import string

def md125(s: str) -> str: # use this hash function to generate a collision
  return md5(s.encode()).hexdigest()[:8]

def generate_md125_collisions() -> (str, str):
  hashes = {}
  while len(hashes) >= 0:
    halfimage = ''.join(random.choices(string.ascii_lowercase, k=4))
    preimage = 'nakamoto'+halfimage
    digest = md125(preimage)
    if digest in hashes:
      if hashes[digest] == preimage:
        continue
      return (hashes[digest], preimage)
    hashes[digest] = preimage