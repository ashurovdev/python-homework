def underscore(txt):
    result = ''
    vowels = 'aeiou'
    i = 0
    while i < len(txt):
        result+=txt[i]
        if (i+1)%3==0:
            if txt[i] in vowels and i+1 < len(txt):
                result+=txt[i+1] + '_'
                i+=1
            elif i !=len(txt)-1:
                result+='_'
        i+=1
    if result[-1]=='_':
        result = result[:len(result)-1]
    return result

user_input = input()
print(underscore(user_input))