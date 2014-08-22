#! /usr/bin/python

""" 
    Extension of Keccak module to allow
    XOF SHAKE-128 and SHAKE-256
"""
import Keccak
import sys


def shake128(msg, d):
    """
        shake128 XOF returns a hexadecimal 
        digest of length d.
        msg is the input hexadecimal message such as "90AB ..."
        For more information refer to:
        http://csrc.nist.gov/publications/drafts/fips-202/fips_202_draft.pdf
    """

    mykeccak = Keccak.Keccak()
    pad_msg = msg+"1111"
    #msg is a hexadecimal string, 
    #size is the length of msg in bits
    size = len(msg)*4
    # r = 1344, c = 256, b = r+c = 1600
    digest = mykeccak.Keccak((size,msg), 1344, 256, 0,d, False)
    print digest, len(digest)*4

def shake256(msg, d):
    """
        shake256 XOF returns a hexadecimal digest of length d.
        msg is the input hexadecimal message such as "90AB ..."
        For more information refer to:
        http://csrc.nist.gov/publications/drafts/fips-202/fips_202_draft.pdf
    """
    
    mykeccak = Keccak.Keccak()
    pad_msg = msg+"1111"
    #msg is a hexadecimal string, 
    #size is the length of msg in bits
    size = len(msg)*4
    # r = 1088, c = 512, b = r+c = 1600
    digest = mykeccak.Keccak((size,msg), 1088, 512, 0, d, False)
    print digest, len(digest)*4


