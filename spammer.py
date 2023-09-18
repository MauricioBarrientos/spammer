import pyautogui
import webbrowser
import time

message = input("¿Qué mensaje deseas enviar repetidamente? (Deja esto en blanco si deseas pegar desde tu portapapeles)  ")
repeats = int(input("¿Cuántas veces deseas enviar el mensaje?  "))
delay = int(input("¿Cuántos milisegundos deseas esperar entre cada mensaje?  "))

isLoaded = input("Presiona Enter cuando tu aplicación de mensajería esté cargada.")



print("Tienes cinco segundos para enfocar el área de entrada de texto de tu aplicación de mensajería.")

time.sleep(5)


for i in range(0, repeats):         # Bucle de envío de mensajes
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

    time.sleep(delay/1000)


print("¡Hecho!\n")
