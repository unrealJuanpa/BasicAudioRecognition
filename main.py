import numpy as np
import soundfile as sf
# Joel Gramajo - 202008025


patron = sf.read('archivo4.wav', dtype='float32')[0]
m = None
idx = None

for i in range(1, 4, 1):
    x = sf.read(f'archivo{i}.wav')[0]
    r = np.max(np.correlate(patron, x, mode='full'))
    
    if type(m) == type(None):
        m = np.copy(r)
        idx = i
    elif r > m:
        m = np.copy(r) 
        idx = i


print(f'Se ha encontrado que el archivo de audio "archivo{idx}.wav" es el mas parecido al patron suministrado, con un puntaje de {m} resultado de la correlacion entre ambos.')