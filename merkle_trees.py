# PART 1

from hashlib import sha256

def hash_it(two_str: list) -> str:
  return sha256((two_str[0]+two_str[1]).encode()).hexdigest()


def chunk_it(layer: list) -> list:
  for i in range(0, len(layer), 2):
    yield layer[i: i+2]
  

def recur_traverse(non_base_layer: list):
  if len(non_base_layer) == 1:
    return non_base_layer[0]
    
  else:
    chunked_layer = list(chunk_it(non_base_layer))
    node_acc = []
    for j in chunked_layer:
      if len(j) == 2:
        node_acc.append(hash_it(j))
      else:
        node_acc.append(sha256((j[0]+'\x00').encode()).hexdigest())
    return recur_traverse(node_acc)
    

def merkleize(sentence: str) -> str:
  split_sentence = sentence.split(" ")
  base_merkle = []
  for i in split_sentence:
    base_merkle.append(sha256(i.encode()).hexdigest())

  merkle_root = recur_traverse(base_merkle)
  return merkle_root

# PART 2

from enum import Enum

class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
  data_hash = sha256(data.encode()).hexdigest()
  
  if len(proof) == 0:
    single_hash = sha256((data_hash+'\x00').encode()).hexdigest()
    return data_hash == root
  else:
    proof_hash = data_hash
    for p in proof:
      if p[1] == Side.LEFT:
        proof_hash = sha256((p[0] + proof_hash).encode()).hexdigest()
      else:
        proof_hash = sha256((proof_hash + p[0]).encode()).hexdigest()
    return proof_hash == root