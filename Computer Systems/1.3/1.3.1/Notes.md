# Compression, Encryption and Hashing

## Compression
Compression is used to reduce the storage space taken up the file, letting more files be stored and increasing speed of sharing, searching and downloading. 

### Run Length Encoding
Lossless compression that combines repeating values into the value followed by how many times it appears in a row. Relies on repetition in the data.

### Dictionary Encoding
Lossless compression that creates a dictionary of frequently used peices of data. When the commonly used value is found in the file it is replaced with the index of where it is in the dictionary, and can be found again in constant time. Again relies on repetition in the data, but this time the data can be repeated anywhere in the file. 

### Lossy and Lossless
Advantages of lossy
- Greater reduction in size
- Can be tuned to get to storage size you want e.g. photoshop jpg exports
- some information is not necessary and can be discarded without too noticable of an effect. e.g. very low or high frequencies in audio files.

Advantages of lossless 
- no loss in quality
- origional file can be recovered

## Encryption
Encryption is encoding data to make it harder to understand by anyone other than the intended recipient. When storing or sending **plain-text** (unscrambled) data it is encrypted into **cypher-text** and decrypted to be viewed again. Encryption keeps information secure, unreadable and confidential. It is done with hash functions.

[how hashing works](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.4/1.4.2/Notes.md#hash-tables)

Keys are typically 256 bits long, and with current computers would take lifetimes to brute force. Know as **computational security**, encryption relies on intractable problems - not being breakable in a reasonable amount of time without a key. Quantum computing makes a lot of this obsolete, so instead, quantum key distribution is being researched.

In **symmetric** encryption the same key is used for encryption and decryption. The key needs to remain private and must be already know by the sender and receiver, or secretly shared through a key exchange which must also be secure.

In **asymmetric** two keys are used, a private and a public key. The public key of the recipeint is used for encryption and the corresponding private key is used for decryption. Asymmetric encryption is also used for **sender authentication**. if you encrypt a message with your private key, only your public key can decrypt it, proving that you are the sender of a message.

### Digital signatures and certificates
A digital signature garantees the integrity of a message (that it hasn't been altered). A digital signiture is made by the sender with thier private key. If they then encrypt this with the origional message and send it, the recpeitan decrypt both the message and the signature, to check that they match. It can also include a timestamp. Emails use this so that if a message is tampered with, they'll be able to tell.

A gigital certificates verifys the sender's identity and is issued by an official certificate authority. Browsers check the certificates of websites before they are visited, to make sure the IPs match, and the certificate is in date. The cerficitates use digital signatures to make sure they are genuine. Used by Transport Layer Security encryption protocol which is used in HTTPS.

