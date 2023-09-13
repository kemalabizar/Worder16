# Worder16
A 16-bit computer, made with Logisim and Python, with fully custom ISA.

# Features
- Main memory of 128KBytes (64KWord)
- ALU capable of bitwise logic, arithmetics & unsigned multiplication.
- 16 data registers (3 ALU + 13 general-purpose)
- 8 I/O ports, mapped for peripherals
- Equal execution cycle of every instructions (32 clock cycles)
- 25 instruction RISC architecture

# Assembly Instruction
```
LDA    ADDR REGS          Load data from ADDR to REGS                          REGS = [ADDR]
STA    ADDR REGS          Store data to ADDR from REGS                         [ADDR] = REGS
LDI    IMM8 REGS          Load value IMM8 to REGS                              REGS = [IMM8]
MOV    REG1 REG2          Move data from REG1 to REG2                          REG2 = REG1
JMP    ADDR               Jump to next instruction at ADDR                     [PC] = ADDR
JIF    ADDR FLAG          Jump to next instruction at ADDR if FLAG is true     FLAG ?= ALUCF: [PC] = ADDR
INB    ADDR PORT          Input to ADDR from PORT                              [ADDR] = [PORT]
OUTB   ADDR PORT          Output from ADDR to PORT                             [PORT] = [ADDR]
PUSH   REGS               Push data from REGS to stack                         SP = REGS: SP++
POP    REGS               Pop data to REGS from stack                          REGS = SP: SP--
NOP                       No operation
HLT                       Halt operation, reset counter until interrupt
ADD    REG1 REG2 C        Add REG1 with REG2 with C(arry)
SUB    REG1 REG2 B        Subtract REG1 by REG2 with B(orrow)
MUL    REG1 REG2          Multiply REG1 by REG2, unsigned operation
CMP    REG1 REG2          Compare REG1 against REG2, store flags
AND    REG1 REG2          Logic AND REG1 with REG2
OR     REG1 REG2          Logic OR REG1 with REG2
XOR    REG1 REG2          Logic XOR REG1 with REG2
NOT    REGS               Logic NOT REGS
SHL    REG1 REG2          Bitwise shift left REG1 by REG2
SHR    REG1 REG2          Bitwise shift right REG1 by REG2
ROL    REG1 REG2          Bitwise roll left REG1 by REG2
ROR    REG1 REG2          Bitwise roll right REG1 by REG2
INC    REGS               Increment REGS
DEC    REGS               Decrement REGS
```
# Instruction Set Architecture
