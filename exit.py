import os

from peachpy import *
from peachpy.x86_64 import *

from bronzebeard.elf import ELF

# User-level applications use as integer registers for passing the sequence:
# %rdi, %rsi, %rdx, %rcx, %r8 and %r9

code = bytearray()
code.extend(MOV(rax, 60).encode())
code.extend(MOV(rdi, 42).encode())
code.extend(SYSCALL().encode())

elf = ELF(code)
with open('output.elf', 'wb') as f:
    f.write(elf.build())

os.chmod('output.elf', 0o775)