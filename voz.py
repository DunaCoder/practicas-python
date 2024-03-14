#esta es una pratica con libreria de voz
from gtts import gTTS

# Texto que deseas que la máquina diga
text = "Hola mundo, soy un programa de computadora"

# Idioma del texto
language = "es"

# Velocidad de la voz (False para velocidad normal)
slow = False

# Crea una instancia de la clase gTTS
speech = gTTS(text=text, lang=language, slow=slow)

# Guarda el audio como un archivo .mp3
speech.save("texto.mp3")
