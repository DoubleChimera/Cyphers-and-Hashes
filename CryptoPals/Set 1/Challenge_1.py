
# CryptoPals  -  Set 1  -  Challenge 1

### ! NOTES:    Had to remove the trailing '\n' character from the base64 encoded message 
### !           otherwise string equivalence won't work since it compares utf-8 chars

### Code the solution
import codecs

hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
outputCheck = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode().replace('\n', '')

###  Check the result
print(' Expected Output: {}'.format(outputCheck))
print('Generated Output: {}'.format(b64))

if (outputCheck == b64):
    print('\nSUCCESS!')
else:
    print('\nFAILURE...')