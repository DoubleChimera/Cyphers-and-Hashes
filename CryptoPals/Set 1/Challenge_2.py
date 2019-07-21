
# CryptoPals  -  Set 1  -  Challenge 2

### ! NOTES:  Hex decode string, xor it against value, should get outputCheck

### Code the solution
import codecs

originalString = '1c0111001f010100061a024b53535009181c'
xorValue = '686974207468652062756c6c277320657965'
outputCheck = '746865206b696420646f6e277420706c6179'

# First decode both strings from hex
hexDecode = codecs.decode(originalString, 'hex')
xorValDecode = codecs.decode(xorValue, 'hex')
# Perform byte-wise xor on both decoded values
hex_xor_val = bytes(a ^ b for (a, b) in zip(hexDecode, xorValDecode))
# Re-encode result as hex before comparison to outputCheck
hexXorOut = codecs.encode(hex_xor_val, 'hex').decode()


###  Check the result
print(' Expected Output: {}'.format(outputCheck))
print('Generated Output: {}'.format(hexXorOut))

if (outputCheck == hexXorOut):
    print('\nSUCCESS!')
else:
    print('\nFAILURE...')