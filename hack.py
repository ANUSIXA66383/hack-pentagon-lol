import time
import toml
import os
import art
art.tprint('HACK')
config_file = 'config-hack.toml'
config = toml.load(config_file)
print('loading config...')
time.sleep(2)
log_file = config.get('pentagon_log')
if log_file:
    log_file = os.path.abspath(log_file)
    with open(log_file, 'a') as f:
        f.write('l')

time.sleep(5)        
print('хак пентагона начался')
print('платформа хака: atahol')
time.sleep(0.2)
print('info: trying to open log pentagon...')
time.sleep(5)
print('info: sucesfelly open log')
print('info: loading Platform hack pentagon ver 7.8.9...')
time.sleep(30)

os.system('python3 atahol.py')
