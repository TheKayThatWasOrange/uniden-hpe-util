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
# parts of the world. Maybe Uniden would
# sell more scanners if they stopped being
# clever and stuck to CSV files the entire
# world can work with.
UNIDEN_OBFUSCATION_KEY = 0x0C
UNIDEN_BYTE_ORDER = "little"

def xor_byte(byte: bytes) -> bytes:
  byte_as_int = int.from_bytes(byte, UNIDEN_BYTE_ORDER)
  xored = byte_as_int ^ UNIDEN_OBFUSCATION_KEY

  return xored.to_bytes(1, UNIDEN_BYTE_ORDER)

def decode_hpe_file(file_path: str, cleanup: bool):
  path, _ = os.path.splitext(file_path)
  temp_gzip_file = f"{path}_tmp_decoding.gz"
  dest_file = f"{path}_decoded.txt"

  print(f"Decoding to {dest_file}...")

  try:
    # De-XOR to .gz
    with open(file_path, "rb") as source:
      with open(temp_gzip_file, "wb") as dest:
        while (byte := source.read(1)):
          dest.write(xor_byte(byte))
    
    # Gunzip to .txt
    with gzip.open(temp_gzip_file, "rb") as zipped:
      with open(dest_file, "wb") as unzipped:
        shutil.copyfileobj(zipped, unzipped)
  finally:
    if cleanup:
      os.remove(temp_gzip_file)
  
def encode_hpe_file(file_path: str, cleanup: bool):
  path, _ = os.path.splitext(file_path)
  temp_gzip_file = f"{path}_tmp_encoding.gz"
  dest_file = f"{path}_encoded.hpe"

  print(f"Encoding to {dest_file}...")

  try:
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
  finally:
    if cleanup:
      os.remove(temp_gzip_file)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Tool for dealing with Uniden's offshore cubicle software")
  parser.add_argument('operation', choices=['encode', 'decode'], help="Either 'encode' or 'decode'.")
  parser.add_argument('filename', help="Path to the file that you want to operate on.")
  parser.add_argument('--no-cleanup', action='store_true', help="Leaves intermediate .gz files in place for debugging purposes.")
  args = parser.parse_args()

  if args.operation == 'decode':
    decode_hpe_file(args.filename, args.no_cleanup == False)
  elif args.operation == 'encode':
    encode_hpe_file(args.filename, args.no_cleanup == False)

