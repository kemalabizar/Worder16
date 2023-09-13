# Worder16
A 16-bit computer, made with Logisim and Python, with fully custom ISA.

# Features
- Main memory of 128KBytes (64KWord)
- ALU capable of bitwise logic, arithmetics & unsigned multiplication.
- 16 data registers (3 ALU + 13 general-purpose)
- 8 I/O ports, mapped for peripherals
- Equal execution cycle of every instructions (32 clock cycles)
- 26 instruction RISC architecture

# Assembly Instruction
```
Opcode    Instruction        Length       Description                                          Mathematical Representation
(Bin)
---------------------------------------------------------------------------------------------------------------------
00000     LDA    ADDR REGS     2          Load data from ADDR to REGS                          REGS = [ADDR]      
00001     STA    ADDR REGS     2          Store data to ADDR from REGS                         [ADDR] = REGS
00010     LDI    IMM8 REGS     2          Load value IMM8 to REGS                              REGS = [IMM8]
00011     MOV    REG1 REG2     1          Move data from REG1 to REG2                          REG2 = REG1
00100     JMP    ADDR          2          Jump to next instruction at ADDR                     [PC] = ADDR
00101     JIF    ADDR FLAG     2          Jump to next instruction at ADDR if FLAG is true     FLAG ?= ALUCF; [PC] = ADDR
00110     INB    ADDR PORT     2          Input to ADDR from PORT                              [ADDR] = [PORT]
00111     OUTB   ADDR PORT     2          Output from ADDR to PORT                             [PORT] = [ADDR]
01000     PUSH   REGS          1          Push data from REGS to stack                         SP = REGS: SP++
01001     POP    REGS          1          Pop data to REGS from stack                          REGS = SP: SP--
01010     NOP                  1          No operation
01011     HLT                  1          Halt CPU, reset cycle counter until interrupt
10000     ADD    REG1 REG2 C   1          Add REG1 with REG2 with C(arry)                      ACC = REG1 + REG2 + C
10001     SUB    REG1 REG2 B   1          Subtract REG1 by REG2 with B(orrow)                  ACC = REG1 - REG2 - B
10010     MUL    REG1 REG2     1          Multiply REG1 by REG2, unsigned operation            ACC = 15;8(REG1 * REG2); MUC = 7;0(REG1 * REG2)
10011     CMP    REG1 REG2     1          Compare REG1 against REG2, store flags               ALUCF = [CMP]
10100     AND    REG1 REG2     1          Logic AND REG1 with REG2                             ACC = REG1 & REG2
10101     OR     REG1 REG2     1          Logic OR REG1 with REG2                              ACC = REG1 | REG2
10110     XOR    REG1 REG2     1          Logic XOR REG1 with REG2                             ACC = REG1 +| REG2
10111     NOT    REGS          1          Logic NOT REGS                                       ACC = !REGS
11000     SHL    REG1 REG2     1          Bitwise shift left REG1 by REG2                      ACC = SHL(REG1, 4;0(REG2))
11001     SHR    REG1 REG2     1          Bitwise shift right REG1 by REG2                     ACC = SHR(REG1, 4;0(REG2))
11010     ROL    REG1 REG2     1          Bitwise roll left REG1 by REG2                       ACC = ROL(REG1, 4;0(REG2))
11011     ROR    REG1 REG2     1          Bitwise roll right REG1 by REG2                      ACC = ROR(REG1, 4;0(REG2))
11100     INC    REGS          1          Increment REGS                                       REGS = REGS++
11101     DEC    REGS          1          Decrement REGS                                       REGS = REGS--
```

# Instruction Set Architecture
## Instruction Byte Structure

Memory-Addressing Instructions (`LDA, STA, INB, OUTB`)
```
Byte 1:  XXXX XPPP RRRR 0000
X = Opcode [5b] (as specified in Assembly Instruction)
P = I/O Port [3b] (as specified in I/O Port Mapping)
R = Register [4b] (as specified in Register Addressing)

Byte 2:  MMMM MMMM MMMM MMMM
M = Memory Address [16b] (as specified in Memory Allocation)
```

Stack Operations Instructions (`PUSH, POP`)
```
Byte 1:  XXXX X000 RRRR 0000
X = Opcode [5b] (as specified in Assembly Instruction)
R = Register [4b] (as specified in Register Addressing)
```

Immediate-Value Instructions (`LDI`)
```
Byte 1:  XXXX X000 RRRR 0000
X = Opcode [5b] (as specified in Assembly Instruction)
R = Register [4b] (as specified in Register Addressing)

Byte 2:  VVVV VVVV VVVV VVVV
V = Immediate Value [16b] (ranges from 0 to 65535)
```

Double-Register Instructions (`MOV` & Math Instructions)
```
Byte 1:  XXXX X000 AAAA BBBB
X = Opcode [5b] (as specified in Assembly Instruction)
A = Register 1 [4b] (as specified in Register Addressing)
B = Register 2 [4b] (as specified in Register Addressing)
```

Address Jump Instructions (`JMP, JIF`)
```
Byte 1:  XXXX X000 000F FFFF
X = Opcode [5b] (as specified in Assembly Instruction)
F = Flags [5b] (as specified in ALU Flag Conditions)
```

## Register Addressing
```
Code   Regs     Usage
(Hex)
------------------------------------------------------------
0      ACC      Accumulator, one-way (ALU --> ACC)
1      ALB      ALU B Input, one-way (BUS --> ALB)
2      MUC      ALU Mul LSB, one-way (ALU --> MUC)
3      RDW      Register D, two-way
4      REW      Register E, two-way
5      RFW      Register F, two-way
6      RGW      Register G, two-way
7      RHW      Register H, two-way
8      RJW      Register J, two-way
9      RLW      Register L, two-way
a      RMW      Register M, two-way
b      RNW      Register N, two-way
c      RPW      Register P, two-way
d      RQW      Register Q, two-way
e      RRW      Register R, two-way
f      RSW      Register S, two-way
```
## ALU Flag Conditions
```
Code     Flag    Description
(Bin)
------------------------------------------------------------
10000    CB1    'Carry or Borrow' flag
01000    A>B    'A larger B' flag
00100    A=B    'A equal B' flag
00010    A=0    'A is zero' flag
00001    A<0    'A negative' flag
```
## I/O Port Mapping
```
BCDX    7-segment output screen (TBD)
XKEY    Hexadecimal keyboard (TBD)
BEEP    Beep spekaer output (TBD)
PIO3    Port 3, unallocated
PIO4    Port 4, unallocated
PIO5    Port 5, unallocated
PIO6    Port 6, unallocated
PIO7    Port 7, unallocated
```
