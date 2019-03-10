#!/usr/bin/python3

from elftools.elf.elffile import ELFFile
import capstone
import struct

import general
import print_pretty
import categorize



# This file has routines which will get ROPChains for different exploit functions. 

payload = bytes()


# Takes in 1-instruction GadgetList (general.ALLGADGETS) and name of the vulnerable executable
def execveROPChain(GadgetList, vulnExecutable): 

    fd = open(vulnExecutable, "rb")
    elffile = ELFFile(fd)
    data_section = ".data"
    section = elffile.get_section_by_name(data_section)
    
    # We need .data section's details because we have to write "/bin//sh" into it. 
    data_section_addr = section["sh_addr"]
    data_section_size = section["sh_size"]

    syscallList = categorize.checkIfSyscallPresent(GadgetList)
    intList = categorize.checkIfIntPresent(GadgetList)

    if len(intList) == 0 and len(syscallList) == 0: 
        print("No int 0x80, no syscall, no ROP")
        print("Exiting tool :(")
        sys.exit()
    
    # This is what we have to do: 
    
    # if int 0x80 is found, 
        # rax <- 11
        # rbx <- Address of "/bin/sh"
        # rcx <- 0
        # rdx <- 0
        # int 0x80
    
    # if syscall is found, 
        # rax <- 59
        # rdi <- Address of "/bin/sh"
        # rsi <- 0
        # rdx <- 0
        # syscall
    

    # Always choose int 0x80 over syscall if int 0x80 is present because registers used are common ones and eax should be set to 11. 

    # Will always go for int 0x80(if present) because rax should be incremented only 11 times for execve()
    elif len(intList) > 0 : 
        (execveChain, payload) = case1(GadgetList)
        return (execveChain, payload)
    
    if len(syscallList) > 0: 
        (execveChain, payload) = case1(GadgetList)
        return (execveChain, payload)
    
    print("If this is getting printed, it means there are no special instructions found. So, you know what this means!")


    

# If int 0x80 is present.
def case1(GadgetList) : 

    

        
    
    
    
    
