f = open('output.txt','r')

string = f.read()
print(string,"string")
# print(string)
key = "harrtshshywtreawqczbxmclpciduhdjkflfjagreihfjsnabcxfshyeorppwushahjakqewreyrtiyouiplmnvbvvxczassfdhfjglgl"




def get_ord(i,cnt):
    print("cnt", cnt)
    inte = ord(i)-ord('A')
    print(inte, "inte")
    sum = inte - cnt
    sum = sum%26

    new_c = chr(sum + ord('A'))
    return new_c

def decrypt(key,string):
    # list_s = list(string)
    # print(list_s)

    list_k = list(key)
    # print(list_k)
    list_visited = []
    list_visited1 =[]
    new_string = []
    for k in list_k:
        if k not in list_visited1:
            list_visited1.append(k)
        else:
            continue
    for i in list_visited1:
        y = chr(ord(i)-32)
        list_visited.append(y)

    print(list_visited)

    # print(list_visited)
    for i in string:
        cnt = 0
        if i == ' ':
            new_string.append(' ')
            continue
        if i not in list_visited:
            # char_c = chr((ord(i)+cnt+ord(list_visited[1]))-30)
            # print(char_c)
            # new_string.append(char_c)
            new_string.append(i)
            continue

        for j in list_visited:
            print(i, "iii", j, "jjj")
            if i == j:
                char_ci = get_ord(i,cnt)
                new_string.append(char_ci)
            else:
                cnt=cnt + 1
                continue
    
    # new_str = ''.join(new_string)
    return new_string
    # print(new_str)
    # print(new_string)

    # print(list_k)

#print(encrypt(key,string))

new_str = decrypt(key,string)
#print(new_str)

file1 = open('decrypted.txt', 'w')
file1.write(''.join(new_str))
file1.close()