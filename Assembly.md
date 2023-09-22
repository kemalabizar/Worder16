# Worder16 Assembly Instructions Structure
Example: `Fibonacci.w16asm`
```
!FILENAME<FIBONACCI.W16ASM>
;VARIABLE
  X = 0x0000
  Y = 0x0001
  Z = 0x0000
  L = 0xB798
;CODESEGMENT
  INIT:
    LDA X[0] RDW
    LDA Y[0] REW
    LDA Z[0] RFW
    LDA L[0] RGW
    STA X[1] RDW
    STA Y[1] REW
    STA Z[1] RFW
    STA L[1] RGW
  LOOP:
    STA X[1] RDW
    STA Y[1] REW
    STA Z[1] RFW
    OUT X[1] BCDX
    ADD RDW REW
    MOV ACC RFW
    MOV REW RDW
    MOV RFW REW
    CMP RGW RDW
  WHILE_MORE:
    JIF LOOP A>B
    JMP INIT
END;
```
## Variable Memory Allocation
The assembler would look at the  `;CODESEGMENT` part, and parse each variable and its assigned values into a variable table.
After a variable table has been generated, an address generator unit would assign each values into corresponding memory locations.
