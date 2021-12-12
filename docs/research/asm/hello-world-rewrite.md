# ASM Writer

The end goal is to have the fastest app. Compiling the higher-level source to _as low as possible_ is the best bet. With an ASM language we can potentially optimise for the lowest form in micro apps.


The _upper level_ linguistics may utilise the builtin AST, with a simplifier and transpiler into ASM, and finally into `.o` or `com` entities. As VOL has its own methodology, there is room to adapt the builtin language.

## Concepts.


The intention will be both _upper_ and _lower_ exposure of ASM. Defining data should be a painless process:


```asm
SECTION .data
                ; we can modify this now without having to update anywhere else in the program
msg     db      'Hello, brave new world!', 0Ah
```

We can optimise thus:

```py
msg = 'Hello, brave new world!' #new line
msg = r'Hello, brave new world!' # no new line
msg = bytes(msg) # as literal

section.data.add(msg)
```

## Global (and continuation)

The `global` definition after the

```asm
SECTION .text
global  _start

_start:

    mov     edx, 13
    mov     ecx, msg
    mov     ebx, 1
    mov     eax, 4
    int     80h

    mov     ebx, 0      ; return 0 status on exit - 'No Errors'
    mov     eax, 1      ; invoke SYS_EXIT (kernel opcode 1)
    int     80h
```


## A _real_ function call.

In this example a core linux "sys_write"

1. The _function_ accepts the output (fd), the content (\*buf), and _size_ (count)
2. apply into the OPCODE `4`; designated the _write_ function

The function accepts these values into the register positions assigned. In `x86` this is:

+ `EAX`: opcode,
+ `EBX`: fd
+ `ECX`: buf
+ `EDX`: count

Applied as a list of linear executions:

+ size of "message" into the _count_ `EDX`
+ the _msg_ content into the buffer `ECX`
+ the output (file descriptor) std_out to `EAX`
+ perform an 'interrupt'

```
    mov     edx, 13     ; number of bytes to write - one for each letter plus 0Ah (line feed character)
    mov     ecx, msg    ; move the memory address of our message string into ecx
    mov     ebx, 1      ; write to the STDOUT file
    mov     eax, 4      ; invoke SYS_WRITE (kernel opcode 4)
    int     80h
```
## ASM Source


```asm
; Hello World Program (Calculating string length)
; Compile with: nasm -f elf helloworld-len.asm
; Link with (64 bit systems require elf_i386 option): ld -m elf_i386 helloworld-len.o -o helloworld-len
; Run with: ./helloworld-len

SECTION .data
msg     db      'Hello, brave new world!', 0Ah ; we can modify this now without having to update anywhere else in the program

SECTION .text
global  _start

_start:

    mov     ebx, msg        ; move the address of our message string into EBX
    mov     eax, ebx        ; move the address in EBX into EAX as well (Both now point to the same segment in memory)

nextchar:
    cmp     byte [eax], 0   ; compare the byte pointed to by EAX at this address against zero (Zero is an end of string delimiter)
    jz      finished        ; jump (if the zero flagged has been set) to the point in the code labeled 'finished'
    inc     eax             ; increment the address in EAX by one byte (if the zero flagged has NOT been set)
    jmp     nextchar        ; jump to the point in the code labeled 'nextchar'

finished:
    sub     eax, ebx        ; subtract the address in EBX from the address in EAX
                            ; remember both registers started pointing to the same address (see line 15)
                            ; but EAX has been incremented one byte for each character in the message string
                            ; when you subtract one memory address from another of the same type
                            ; the result is number of segments between them - in this case the number of bytes

    mov     edx, eax        ; EAX now equals the number of bytes in our string
    mov     ecx, msg        ; the rest of the code should be familiar now
    mov     ebx, 1
    mov     eax, 4
    int     80h

    mov     ebx, 0
    mov     eax, 1
    int     80h
```
