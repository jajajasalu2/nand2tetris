import sys
import re
sys_mem_locs = { 'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15':15, 'SCREEN': 16384, 'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4}
usr_def_mem_locs = {}
current_usr_mem = 16
        
def parse_jump(jump):
    jmp_code = [0] * 3
    if (jump == 'JMP'):
        jmp_code = '111'
    elif (jump == 'JLE'):
        jmp_code = '110'
    elif (jump == 'JNE'):
        jmp_code = '101'
    elif (jump == 'JLT'):
        jmp_code = '100'
    elif (jump == 'JGE'):
        jmp_code = '011'
    elif (jump == 'JEQ'):
        jmp_code = '010'
    elif (jump == 'JGT'):
        jmp_code = '001'
    return jmp_code


def parse_dest(dest):
    if (dest == 'A'):
        dest_code = '100'    
    elif (dest == 'M'):
        dest_code = '001'
    elif (dest == 'D'):
        dest_code = '010'
    elif (dest == 'AM'):
        dest_code = '101'
    elif (dest == 'MD'):
        dest_code = '011'
    elif (dest == 'AD'):
        dest_code = '110'
    elif (dest == 'AMD'):
        dest_code = '111'
    return dest_code
        

def parse_expression(expr):
    if (expr == '0'):
        alu_code = '0101010'
    elif (expr == '1'):
        alu_code = '0111111'
    elif (expr == '-1'):
        alu_code = '0111010'
    elif (expr == 'D'):
        alu_code = '0001100'
    elif (expr == 'A'):
        alu_code = '0110000'
    elif (expr == 'M'):
        alu_code = '1110000'
    elif (expr == '!A'):
        alu_code = '0110001'
    elif (expr == '!M'):
        alu_code = '1110001'
    elif (expr == '!D') :
        alu_code = '0001101'
    elif (expr == '-D'):
        alu_code = '0001111'
    elif (expr == '-A'):
        alu_code = '0110011'
    elif (expr == 'D+1' or expr == '1+D'):
        alu_code = '0011111'
    elif (expr == 'A+1' or expr == '1+A'):
        alu_code = '0110111'
    elif (expr == 'M+1' or expr == '1+M'):
        alu_code = '1110111'
    elif (expr == 'D-1'):
        alu_code = '0001110'
    elif (expr == 'A-1'):
        alu_code = '0110010'
    elif (expr == 'M-1'):
        alu_code = '1110010'
    elif (expr == 'D+A' or expr == 'A+D'):
        alu_code = '0000010'
    elif (expr == 'D+M' or expr == 'M+D'):
        alu_code = '1000010'
    elif (expr == 'D-A'):
        alu_code = '0010010'
    elif (expr == 'D-M'):
        alu_code = '1010010'
    elif (expr == 'A-D'):
        alu_code = '0000111'
    elif (expr == 'M-D'):
        alu_code = '1000111'
    elif (expr == 'D&A' or expr == 'A&D'):
        alu_code = '0000000'
    elif (expr == 'D&M' or expr == 'M&D'):
        alu_code = '1000000'
    elif (expr == 'D|A' or expr == 'A|D'):
        alu_code = '0010101'
    elif (expr == 'D|M' or expr == 'M|D'):
        alu_code = '1010101'
    return alu_code;


def binary_16(binary):
    l = len(binary)
    c = 0
    bin_16 = ''
    while (c != 16 - l):
        bin_16 += '0'
        c += 1
    bin_16 += str(binary)
    return bin_16


def get_hack_filename(file_name):
    file_name = re.match(r'(.+)\.asm',file_name).group(1)
    if (file_name == None):
       return 'error' 
    return file_name + '.hack'


hack_file = get_hack_filename(sys.argv[1])
if (hack_file == 'error'):
    print('Error in assembly file name')
    sys.exit()
f2 = open(hack_file,'w')


with open(sys.argv[1]) as f1:
    for line in f1:
        line = re.sub(r'\s+','',line)
        machine_code = '-1'
        if (len(line) == 0):
            continue
        if (line[0] == '@'):
            if line[1:] not in sys_mem_locs:
                if line[1:] not in usr_def_mem_locs:
                    usr_def_mem_locs[line[1:]] = current_usr_mem
                    current_usr_mem += 1
                binary = '{0:b}'.format((usr_def_mem_locs[line[1:]]))
            else:
                binary = '{0:b}'.format((sys_mem_locs[line[1:]]))
            machine_code = binary_16(binary)
        elif (re.match(r'^\(.*\)$',line) != None):
            if line[1:-1] not in usr_def_mem_locs:
                usr_def_mem_locs[line[1:-1]] = current_usr_mem
                current_usr_mem += 1
        elif (re.match(r'(.+)=(.+)',line) != None):
            statement = re.match(r'(.+)=(.+)',line);
            machine_code = '111' + parse_expression(statement.group(2)) + parse_dest(statement.group(1)) + '000'
        elif (re.match(r'(.+);(.+)',line) != None):
            statement = re.match(r'(.+);(.+)',line)
            machine_code = '111' + parse_expression(statement.group(1)) + '000'+ parse_jump(statement.group(2))
        if (machine_code != '-1'):
            f2.write(machine_code + '\n')

f2.close()
f1.close()
