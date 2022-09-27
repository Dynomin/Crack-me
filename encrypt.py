f = open('input.txt','r')

string = f.read()
#print(string)
key = "harrtshshywtreawqczbxmclpciduhdjkflfjagreihfjsnabcxfshyeorppwushahjakqewreyrtiyouiplmnvbvvxczassfdhfjglgl"


def get_ord(i,cnt):
    inte = ord(i)-ord('a')
    sum = inte + cnt
    sum = sum%26

    new_c = chr(sum + ord('a'))
    return new_c

def encrypt(key,string):
    # list_s = list(string)
    # print(list_s)

    list_k = list(key)
    # print(list_k)
    list_visited = []
    new_string = []
    for k in list_k:
        if k not in list_visited:
            list_visited.append(k)
        else:
            continue
    print(list_visited)
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

        for j in list_visited:
            if i == j:
                char_ci = get_ord(i,cnt)
                char_ci = char_ci.upper()
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

new_str = encrypt(key,string)
#print(new_str)

file1 = open('output.txt', 'w')
file1.write(''.join(new_str))
file1.close()
# ans = get_ord('a',5)
# print(ans)