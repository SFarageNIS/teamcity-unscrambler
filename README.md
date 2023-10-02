# teamcity-unscrambler
Decrypt "scrambled" passwords from any TeamCity server  

## Background
Teamcity found it a good idea to use a global, fixed key to 'encrypt' all the secret parameters using DES3.  
That's obviously a very weak solution and suceptible to easily decrypting it.  
A company I was working with had an issue and needed to determine what the secrets were, so I found this tool and modified it to run on my machine!
