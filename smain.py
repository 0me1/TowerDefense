start_red = '\033[31m'
start_black = '\033[30m'
end = '\033[0m'
base = '{\033[32m*\033[0m}'
rd_chnk = '[ ]' # road_chank 

def padx(num):
    start_black = '\033[30m'
    end = '\033[0m'
    a = f"{start_black}{'a'*num}{end}"
    return a

print(f"{start_black}{'a'*57}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*45}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{base}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}[{start_red}5{end}]{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk}{start_black}{'a'*21}{end}{rd_chnk}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*9 }{end}{rd_chnk*9}{start_black}{'a'*21}{end}")
print(f"{start_black}{'a'*57}{end}")
print(f"{start_black}{'a'*57}{end}")
print(f"{start_black}{'a'*57}{end}")
print(f"{padx(9)}HP[███████]",end='')
print(f"{padx(9)}Mana[█████]{padx(17)}")

# print('{', "\033[32m*\033[0m", '}', sep='')
# print('[\033[31m0\033[0m]')
# print('{rd_chnk}')
# print('{rd_chnk}')
# print('{rd_chnk}')
# print('[\033[31m0\033[0m]')
# print('{rd_chnk}')



