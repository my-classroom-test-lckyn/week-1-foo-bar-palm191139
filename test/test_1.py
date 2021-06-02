import sys
sys.path.insert(1, '../')

f = __import__('1.hello_world.py')

print(f.hello_world())