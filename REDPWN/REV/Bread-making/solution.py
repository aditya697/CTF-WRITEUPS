from pwn import *

r = remote('mc.ax', 31796)
# r = process('./bread')

r.readline()
r.sendline('add flour')
r.readline()
r.sendline('add yeast')
r.readline()
r.sendline('add salt')
r.readline()
r.sendline('add water')
r.readline()
r.readline()
r.sendline('hide the bowl inside a box')
r.readline()
r.readline()
r.readline()
r.sendline('wait 3 hours')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('work in the basement')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('preheat the toaster oven')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('set a timer on your phone')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('watch the bread bake')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('pull the tray out with a towel')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('unplug the oven')
print(r.readline())
r.sendline('unplug the fire alarm')
print(r.readline())
r.sendline('open the window')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('wash the sink')
print(r.readline())
r.sendline('clean the counters')
print(r.readline())
r.sendline('flush the bread down the toilet')
print(r.readline())
r.sendline('get ready to sleep')
print(r.readline())
print(r.readline())
print(r.readline())
r.sendline('close the window')
print(r.readline())
r.sendline('replace the fire alarm')
print(r.readline())
r.sendline('brush teeth and go to bed')
print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())
