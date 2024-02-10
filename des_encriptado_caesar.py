try:
     import pyperclip  # pyperclip copia el texto al portapapeles.
except ImportError:
     pass  #Si pyperclip no está instalado, no se hace nada.
 
# Cada posible símbolo que puede ser cifrado/descifrado:
# También puedes añadir números y signos de puntuación para cifrar esos símbolos.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
print('Bienvenido a la versión del cifrado Caesar hecha por el usuario de github thepythonsummit.')
 # Permite al usuario ingresar si quiere encriptar o desencriptar.
while True:  #Continúa preguntando hasta que el usuario ingrese e o d.
     print('¿Quieres (e)ncriptar o (d)esencriptar?')
     response = input('> ').lower()
     if response.startswith('e'):
         mode = 'encriptar'
         break
     elif response.startswith('d'):
         mode = 'desencriptar'
         break
     print('Introduce la letra e o la letra d.')
 
 # Permite al usuario ingresar que cifrado va a utilizar:
while True:  # Continúa preguntando hasta que el usuario ingrese un cifrado válido.
     maxKey = len(SYMBOLS) - 1
     print('Introduce el número del cifrado (0 hasta {}) que vas a utilizar.'.format(maxKey))
     response = input('> ').upper()
     if not response.isdecimal():
         continue
 
     if 0 <= int(response) < len(SYMBOLS):
         key = int(response)
         break
 
 # Permite al usuario ingresar el mensaje que va a ser desencriptado o encriptado:
print('Introdcue el mensaje para {}.'.format(mode))
message = input('> ')
 
 # El cifrado Caesar solo funciona con letras mayúsculas:
message = message.upper()
 
# Almacena la forma encriptada/desencriptada del mensaje:
translated = ''
 
 #encripta/desencripta cada símbolo del mensaje:
for symbol in message:
     if symbol in SYMBOLS:
         # Obtén el número encriptado/desencriptado para este símbolo.
         num = SYMBOLS.find(symbol)  #Obten el número del símbolo.
         if mode == 'encriptar':
             num = num + key
         elif mode == 'desencriptar':
             num = num - key
 
        # Maneja el desbordamiento si num es mayor que la longitud de
        # SYMBOLS o menor que 0:
         if num >= len(SYMBOLS):
             num = num - len(SYMBOLS)
         elif num < 0:
             num = num + len(SYMBOLS)
 
         # Añade el símbolo del número encriptado/desencriptado a translated:
         translated = translated + SYMBOLS[num]
     else:
         # Simplemente añade el símbolo sin encriptar/desencriptar.
         translated = translated + symbol
 
 #Muestra la cadena encriptada/desencriptada en la pantalla:
print(translated)
 
try:
     pyperclip.copy(translated)
     if mode == 'encriptar':
         print('El texto encriptado ha sido copiado al portapapeles')
     else:
         print('El texto desencriptado ha sido copiado al potapapeles.')
except:
     pass  #No hacer nada si pyperclip no fue instalado.
