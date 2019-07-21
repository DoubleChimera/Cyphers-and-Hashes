##################################################
#####         Reverse Cipher Example         #####
##################################################

message = 'This is program to demo the reverse cipher.'
revcipher = '' #cipher text is stored in this variable
i = len(message) - 1

while i >= 0:
   revcipher = revcipher + message[i]
   i = i - 1
print('The cipher text is : {}'.format(revcipher))

##################################################
#####         Caeser Cipher Example          #####
##################################################
