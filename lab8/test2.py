import re

def parse_config(config_file):
    iter = 0
    result = {}
    with open(config_file) as f:
        lns = f.readlines()
        for line in lns:
            if line =='\n':
                continue
            elif line[0] == '#':
                continue 
            else:
                index = 0
                for i in range(len(line)):
                    if line[i] == '=':
                        index = i
                        break
                if line[-1] == '/n' or '\n':
                    result[re.sub("",line[:index])] = re.sub("",line[index+1:-1])
                else:
                    result[line[:index]] = line[index+1:]
                
        return result 



print(parse_config('test.txt'))