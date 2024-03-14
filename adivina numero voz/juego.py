import random
from gtts import gTTS
import os



idioma = "es"


def generar_saludo():
    saludos = ["¡Hola humano! ", "¡Vaya, vaya! ¿Te atreves a desafiarme? "]
    return random.choice(saludos)


def generar_frases():
    frases_bruja = [
     "Vaya, vaya, parece que estás teniendo dificultades.",
     "Que triste, jajaja.",
     "Hmm, tal vez deberías intentar usar tu cerebro.",
     "¿Estás seguro de que eres lo suficientemente inteligente para esto?",
     "Jajaja, esto es demasiado divertido!",
]
    return random.choice(frases_bruja)



def generar_derrota():
    frases_derrota = [
       "QUE!!?? haz salido del bulcle!!! NOOOO!!! *explota y muere*",
       "¡No puede ser! Has logrado salir del bucle... ¿Cómo es posible?",
        "¡Imposible! Tu astucia ha superado mis expectativas. Me has vencido.",
        "¡Maldición! Tus habilidades son formidables. Has conseguido escapar.",
        "¡Eres un ser excepcional! Tu mente brillante ha triunfado.",
        "¡Felicidades! Has logrado burlar mi ingenio y salir victorioso.",
        "¡Te has ganado mi respeto! Tu tenacidad y perspicacia te han llevado a la victoria."
       
]
    return random.choice(frases_derrota)

secreto = range(1, 10)
texto = generar_saludo() + "haz caido en mi bucle jajaja ahora\ndeberas saber en que numero estoy pensando si deseas ser libre!!!: "
while True:
    numero = int(input("ingresa un numero: "))
    tts = gTTS(text=texto, lang=idioma)
    tts.save("bruja_saludo.mp3")
    os.system("start bruja_saludo.mp3")
    bruja = random.choice(secreto)
    if numero == bruja:
        print(generar_derrota())
        False
        break
    else:
        numero = int(input(generar_frases()+ " ingresa un numero: "))
