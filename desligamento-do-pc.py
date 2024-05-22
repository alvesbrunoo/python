import os

# Desliga o pc em 60s
def offS():
    os.system('shutdown /s')
# Desliga o pc imediatamente
def off():
    os.system('shutdown /s /t 0')
    
# # Cancelando o desligamento
def cancel():
    os.system('shutdown/a')
    
# # Desliga em 1h
def oneHour():
    os.system('sutdown/s t3600')
    
# # Deslliga em 30min
def hafAnHour():
    os.system('shoutdown/s/t 1800')

