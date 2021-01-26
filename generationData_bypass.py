#coding=utf-8
import random,string
import sys
from urllib import parse

varname_min = 5
varname_max = 15
data_min = 20
data_max = 30
num_min = 1
num_max = int(sys.argv[1])
def randstr(length):
    str_list = [random.choice(string.ascii_letters) for i in range(length)]
    random_str = ''.join(str_list)
    return random_str

def main():
    data={}
    for i in range(num_min,num_max):
        data[randstr(random.randint(varname_min,varname_max))]=randstr(random.randint(data_min,data_max))
    print('&'+parse.urlencode(data)+'&')

main()
