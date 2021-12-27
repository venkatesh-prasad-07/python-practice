def mutate_string(string, position, character):
    character = list(string)
    l = character[position]
    
    string = string[:position]+c+ string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
#input: abracadabra
#pos:5 letter=k
#output=abrackdabra
