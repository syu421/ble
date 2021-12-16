import machine
import ubinascii
num = ubinascii.hexlify(machine.unique_id()).decode('utf-8')
print(num)
##'fcf5c4210cdc'+2 = 'fcf5c4210cde'