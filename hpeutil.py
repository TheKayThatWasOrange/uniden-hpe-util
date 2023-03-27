#!/usr/bin/env python3

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 1, March 2023

# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
 
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#  0. You just DO WHAT THE FUCK YOU WANT TO.

import argparse
import gzip
import os
import shutil

# This is what passes for clever in many
# parts of the world. 
UNIDEN_OBFUSCATION_KEY = 0xC

def xor_byte(byte: bytes) -> bytes:
  order = 'little'
  byte_as_int = int.from_bytes(byte, order)
  key_as_int = UNIDEN_OBFUSCATION_KEY
  xored = byte_as_int ^ key_as_int

  return xored.to_bytes(1, order)

def decode_hpe_file(file_path: str):
  path, _ = os.path.splitext(file_path)
  temp_gzip_file = f"{path}_tmp_decoding.gz"
  dest_file = f"{path}_decoded.txt"

  print(f"Decoding to {dest_file}...")

  # De-XOR to .gz
  with open(file_path, "rb") as source:
    with open(temp_gzip_file, "wb") as dest:
      while (byte := source.read(1)):
        dest.write(xor_byte(byte))
  
  # Gunzip to .txt
  with gzip.open(temp_gzip_file, "rb") as zipped:
    with open(dest_file, "wb") as unzipped:
      shutil.copyfileobj(zipped, unzipped)

  os.remove(temp_gzip_file)
  
def encode_hpe_file(file_path: str):
  path, _ = os.path.splitext(file_path)
  temp_gzip_file = f"{path}_tmp_encoding.gz"
  dest_file = f"{path}_encoded.hpe"

  print(f"Encoding to {dest_file}...")

  # Gzip with very minimal compression so Uniden's
  # god-awful .NET code from the 90s can handle it. 
  with open(file_path, "rb") as source:
    with gzip.open(temp_gzip_file, "wb", compresslevel=1) as zipped:
      zipped.writelines(source)

  # XOR to .hpe
  with open(dest_file, "wb") as dest:
    with open(temp_gzip_file, "rb") as zipped:
      while (byte := zipped.read(1)):
        dest.write(xor_byte(byte))

  os.remove(temp_gzip_file)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Tool for dealing with Uniden's offshore cubicle software")
  parser.add_argument('operation', choices=['encode', 'decode'])
  parser.add_argument('filename')
  args = parser.parse_args()

  if args.operation == 'decode':
    decode_hpe_file(args.filename)
  elif args.operation == 'encode':
    encode_hpe_file(args.filename)