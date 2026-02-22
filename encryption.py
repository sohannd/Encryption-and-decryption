

import time

current_time = time.strftime("%H:%M:%S")
print(current_time)
hr = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))
#____________________________________________________________


alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
usr_txt = input("Enter the text to Encrypt: ")
encryption_key = (hr * (min + sec))

#encryption 
print("Encryption ley: ",encryption_key)


results = []

for letter in usr_txt:
    if letter in alpha:
        index = alpha.index(letter) +1
        results.append(index * encryption_key)
print (results)


#decryption
decrypted_txt = ""
for value in results:
    original_index = value // encryption_key
    decrypted_txt += alpha[original_index -1]
print(decrypted_txt)

#____________________________________
