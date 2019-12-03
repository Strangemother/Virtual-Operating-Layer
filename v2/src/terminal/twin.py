from winpty import PtyProcess
# Low level usage using the raw `PTY` object
from winpty import PTY
from time import sleep

proc = PtyProcess.spawn('cmd')
proc.write('dir\r\n')
proc.write('exit()\r\n')
while proc.isalive():
    print(proc.readline())

def _read():
    #sleep(.1)
    c=0
    while proc.isalive():
        v = proc.read()
        if len(v) == 0:
            c+=1
            sleep(.1)
            if c == 5:
                break
        print(v.decode('utf'))
        #sleep(.001)
    sleep(.01)

_read()

# Start a new winpty-agent process of size (cols, rows)
cols, rows = 80, 25
proc = PTY(cols, rows)

# Spawn a new console proc, e.g., CMD
kd = proc.spawn(r'C:\Windows\System32\cmd.exe')

_read()

# Write input to console (Unicode)
proc.write(u'dir\r\n')

_read()

proc.write(u'pwd\r\n')

_read()

# Resize console size
new_cols, new_rows = 90, 30
proc.set_size(new_cols, new_rows)

# Know if the proc is alive
alive = proc.isalive()

# Close console pipes
# proc.close()

# End winpty-agent proc
# del proc
