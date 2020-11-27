#! Python 3.7.4
# Convert list into string with Comma  and put "and " between last  2 values
#spam = ['apples', 'bananas', 'tofu', 'cats']
#the function would return 'apples, bananas, tofu, and cats'

spam = ['apples', 'bananas']

def convert_to_string(sp):
    str1 = ''
    if len(sp)>1:
        # sp.insert(-1, 'and')
        # for i in range(len(sp)-3):
        #     str1= str1 +str(sp[i]) + ','
        # x = -3
        # while x != 0:
        #     str1 = str1 + " " +sp[x]
        #     x+=1
        str1=str( ','.join(sp[:-1]) + ' and '+ sp[-1])
    elif len(sp) == 1
        str1=sp
    else:
        break

    print("here is the string :", str1)

convert_to_string(spam)