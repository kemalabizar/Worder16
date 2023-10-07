import sys, re

OpcdDict = {"lda":0,"sta":1,"ldi":2,"mov":3,"jmp":4,"jif":5,"inb":6,"outb":7,"push":8,"pop":9,"nop":14,"hlt":15,"add":16,"sub":17,"mul":18,"cmp":19,"and":20,"or":21,"xor":22,"not":23,"shl":24,"shr":25,"rol":26,"ror":27,"inc":28,"dec":29}
RegsDict = {"acc":0,"alb":1,"muc":2,"rdw":3,"rew":4,"rfw":5,"rgw":6,"rhw":7,"rjw":8,"rlw":9,"rmw":10,"rnw":11,"rpw":12,"rqw":13,"rrw":14,"rsw":15}
FlagDict = {"carry":16,"a>b":8,"a=b":4,"a=0":2,"a<0":1}
PortDict = {"bcdx":0,"xkey":1,"p002":2,"p003":3,"p004":4,"p005":5,"p006":6,"p007":7,}

def ParseTokensInt(SplitBySpaces):
    OpcdInt = OpcdDict.get(SplitBySpaces[0])
    return [OpcdInt]

MemoryOps = [0, 1]; JumpNcOps = [4]; JumpCdOps = [5]; HaltOps = [15]
ImmvalOps = [2]; PeripheralOps = [6, 7]; TworegOps = [3, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

f = open(sys.argv[1], mode='r')
file = f.read()
LongTokens = re.split("\n", file) #1: Pisahkan (tokenize) berdasar baris '\n'
ShortTokens = []

i = 0
for i in range(0, len(LongTokens)): #2: Pisahkan (tokenize) berdasar spasi '|,'
    InstSplit = re.split(" |,", LongTokens[i])
    InstSplit[0] = OpcdDict.get(InstSplit[0])
    ShortTokens.append(InstSplit)
    i += 1

j = 0
for j in range(0, len(ShortTokens)): #3: Uraikan (parse) menjadi integer, berdasar Ops[].
    if ShortTokens[j][0] in MemoryOps:
        ShortTokens[j][1] = ShortTokens[j][1]; ShortTokens[j][2] = RegsDict.get(ShortTokens[j][2])
    if ShortTokens[j][0] in ImmvalOps:
        ShortTokens[j][1] = ShortTokens[j][1]; ShortTokens[j][2] = RegsDict.get(ShortTokens[j][2])
    if ShortTokens[j][0] in JumpNcOps:
        ShortTokens[j][1] = ShortTokens[j][1]
    if ShortTokens[j][0] in JumpCdOps:
        ShortTokens[j][1] = ShortTokens[j][1]; ShortTokens[j][2] = FlagDict.get(ShortTokens[j][2])
    if ShortTokens[j][0] in PeripheralOps:
        ShortTokens[j][1] = ShortTokens[j][1]; ShortTokens[j][2] = PortDict.get(ShortTokens[j][2])
    if ShortTokens[j][0] in TworegOps:
        ShortTokens[j][1] = RegsDict.get(ShortTokens[j][1]); ShortTokens[j][2] = RegsDict.get(ShortTokens[j][2])
    if ShortTokens[j][0] in HaltOps:
        ShortTokens[j][0] = ShortTokens[j][0]
    j += 1

k = 0
HexCode = []; Address = 0
print("\nProgram:", sys.argv[1])
print("\nv3.0 hex words addressed")
for k in range(0, len(ShortTokens)): #4: Uraikan (parse) dan tulis (writeback) sebagai hexadecimal.
    Int0, Int1 = 0, 0
    if ShortTokens[k][0] in MemoryOps:
        Int0 = (ShortTokens[k][0] * 2048) + (ShortTokens[k][2] * 16); Int1 = int(ShortTokens[k][1], base=16)
        HexCodeShort = [re.sub(" ", "0", format(Int0, '4x')), re.sub(" ", "0", format(Int1, '4x'))]
    if ShortTokens[k][0] in ImmvalOps:
        Int0 = (ShortTokens[k][0] * 2048) + (ShortTokens[k][2] * 16); Int1 = int(ShortTokens[k][1], base=16)
        HexCodeShort = [re.sub(" ", "0", format(Int0, '4x')), re.sub(" ", "0", format(Int1, '4x'))]
    if ShortTokens[k][0] in JumpNcOps:
        Int0 = (ShortTokens[k][0] * 2048); Int1 = int(ShortTokens[k][1], base=16)
        HexCodeShort = [re.sub(" ", "0", format(Int0, '4x')), re.sub(" ", "0", format(Int1, '4x'))]
    if ShortTokens[k][0] in JumpCdOps:
        Int0 = (ShortTokens[k][0] * 2048) + (ShortTokens[k][2] * 1); Int1 = int(ShortTokens[k][1], base=16)
        HexCodeShort = [re.sub(" ", "0", format(Int0, '4x')), re.sub(" ", "0", format(Int1, '4x'))]
    if ShortTokens[k][0] in PeripheralOps:
        Int0 = (ShortTokens[k][0] * 2048) + (ShortTokens[k][2] * 256); Int1 = int(ShortTokens[k][1], base=16)
        HexCodeShort = [re.sub(" ", "0", format(Int0, '4x')), re.sub(" ", "0", format(Int1, '4x'))]
    if ShortTokens[k][0] in TworegOps:
        Int0 = (ShortTokens[k][0] * 2048) + (ShortTokens[k][1] * 16) + (ShortTokens[k][2] * 1)
        HexCodeShort = [re.sub(" ", "0", format(Int0, '4x'))]
    if ShortTokens[k][0] in HaltOps:
        Int0 = (ShortTokens[k][0] * 2048)
        HexCodeShort = [re.sub(" ", "0", format(Int0, '4x'))]
    HexCode.append(HexCodeShort)
    if len(HexCodeShort) == 2:
        print(re.sub(" ", "0", format(Address, '4x'))+":", HexCodeShort[0], HexCodeShort[1]); Address += 2
    else:
        print(re.sub(" ", "0", format(Address, '4x'))+":", HexCodeShort[0]); Address += 1
    k += 1
print("\n")
