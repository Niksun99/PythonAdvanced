# 'w' = creat file or rewrite file prezapiswa
import time
from os import linesep

file = open('./w_demos.txr', 'w')
file.write('---w---')
file.write('It works!')
file.write(linesep)
file.write(str(time.time()))

# 'a' creat file or append to file - Dobavq , no ne prezapiswa

file = open('./a_demos.txr', 'a')
file.write('---a---')
file.write('It works!')
file.write(linesep)
file.write(str(time.time()))

# 'x' creat new file or raise exception
file = open('./x_demos.txr', 'x')
