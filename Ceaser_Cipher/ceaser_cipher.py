alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    encrypted=""
    # int_text=[]
    # int_text2=[]
   
    # for i in text:
    #     int_text.append(alphabet.index(i))
    # print (int_text)
    # for i in int_text:
    #     a = i + shift
    #     if a > 25:
    #         a=a-25
    #         a-=1
    #     int_text2.append(a)
    # print (int_text2)
    # for i in int_text2:
    #     encrypted.append(alphabet[i])
    # print ("".join(encrypted))
    for i in text:
        position = alphabet.index(i)
        position = position + shift
        if position > 25:
            position=position-25
            position-=1
        encrypted+=alphabet[position]
    
    print("Your encrypted message is  " + encrypted)
   #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


def decrypt(text, shift):
    decrypted=""
    for i in text:
        position = alphabet.index(i)
        position = position - shift
        if position < 0:
            position=25+position
            position+=1
        decrypted+=alphabet[position]
    
    print("Your decrypted message is  " + decrypted)


  

if direction=="encrypt":
    encrypt(text, shift)
elif direction=="decrypt":
    decrypt(text, shift)
else: 
    print("wrong input")
