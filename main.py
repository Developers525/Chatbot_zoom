
# Importación de bibliotecas necesarias
import tkinter as tk
import webbrowser
import pyautogui
import time
import threading
import pyperclip
from datetime import datetime
from tkinter import PhotoImage
from PIL import Image, ImageTk





# Enlace de paneñista de vanessa para webinar de los jueves
lst = [
    ["https://us02web.zoom.us/w/82647658326?tk=aMekde-HJ5_GcuL_zlLXypqB30aEN_ab3wvUS3an3oA.DQYAAAATPi8vVhZ3TFAzb3ZoT1FsNndoOHZORzRyQlZRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "13:12"],
    # Agrega más elementos a la lista si es necesario
]

# Variables globales para controlar el proceso
detener_proceso = False
current_sleep_time = 5  # Valor actual de sleep
num_repeticiones = 1000  # Número de repeticiones

# Función para abrir un enlace a una hora específica y realizar acciones
def noid(link, time_schedule):
    isStarted = False
    while not isStarted:
        if datetime.now().strftime("%H:%M") == time_schedule:
            for _ in range(100):
                webbrowser.open(link)
                time.sleep(4)
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.hotkey('alt', 'h')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                time.sleep(4)
                pyautogui.hotkey('alt', 'q')  
            isStarted = True

# Función principal que inicia subprocesos para abrir enlaces
def mainq(link, time_schedule):
    thread3 = threading.Thread(target=noid, args=(link, time_schedule), daemon=True)
    thread3.start()
    thread3.join()

# Función para abrir un enlace y ejecutar acciones
def open_link_and_execute_actions(link):
    # Copiar el texto al portapapeles antes de abrir el enlace
    copiar_texto('📌 ¡INSCRÍBETE A RIQUEZA INFINITA! 📌\nHaz clic en el enlace:\n👉 https://secure.seresderiqueza.com/comenzar 👈')

    webbrowser.open(link)
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(current_sleep_time)
    pyautogui.hotkey('alt', 'h')
    time.sleep(5)

    for _ in range(num_repeticiones):
        if detener_proceso:
            break
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(current_sleep_time)
        pyautogui.press('enter')

# Función para detener el proceso
def detener_proceso_func():
    global detener_proceso
    detener_proceso = True

# Función para restablecer la función y ejecutarla en un hilo secundario
def restablecer_funcion():
    global detener_proceso
    global num_repeticiones
    detener_proceso = False

    def ejecutar_funcion():
        for _ in range(num_repeticiones):
            if detener_proceso:
                break
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(current_sleep_time)
            pyautogui.press('enter')

        ventana.after(100, actualizar_interfaz)

    def actualizar_interfaz():
        ventana.update_idletasks()
        ventana.deiconify()

    thread = threading.Thread(target=ejecutar_funcion, daemon=True)
    thread.start()

# Funciones para cambiar el tiempo de sleep y el número de repeticiones
def cambiar_tiempo(tiempo):
    global current_sleep_time
    current_sleep_time = tiempo

def cambiar_repeticiones(repeticiones):
    global num_repeticiones
    num_repeticiones = repeticiones

# Función que se ejecuta al hacer clic en el botón principal
def on_button_click():
    global detener_proceso
    print("¡Botón clickeado!")
    detener_proceso = False

    for item in lst:
        if len(item) == 2:
            link, _ = item
            thread = threading.Thread(target=open_link_and_execute_actions, args=(link,), daemon=True)
            thread.start()

    print("Todos los enlaces han sido abiertos.")

# Función para copiar texto al portapapeles
def copiar_texto(texto):
    pyperclip.copy(texto)

# Configuración y creación de la ventana tkinter
ventana = tk.Tk()
ventana.title("Vanessa V1.0")
ventana.geometry("1040x550+{}+{}".format(
    ventana.winfo_screenwidth() // 2 - 800 // 2,
    ventana.winfo_screenheight() // 2 - 650 // 2
))

# Creación de botones y configuración de la interfaz gráfica

boton_detener = tk.Button(ventana, text="Detener a Vanessa", command=detener_proceso_func, width=20, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_detener.grid(row=0, column=0, pady=(5, 20))

# ------------------- BOTONES DE COMENZAR -------------------

boton_copiar_oxxo = tk.Button(ventana, text="Mensaje Oxxo -Comenzar- ", command=lambda: copiar_texto('Genera tu ficha de Oxxo 👉 https://secure.seresderiqueza.com/genera_ficha_oxxo'), width=30, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_copiar_oxxo.grid(row=1, column=1, pady=(10, 20), padx=(10, 10))

boton_copiar_spei = tk.Button(ventana, text="Mensaje Spei -Comenzar-", command=lambda: copiar_texto('Genera tu ficha de transferencia (SPEI) 👉  https://secure.seresderiqueza.com/genera_fichas_spei'), width=30, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_copiar_spei.grid(row=2, column=1, pady=(10, 20), padx=(10, 10))

boton_copiar_ultimos_minutos = tk.Button(ventana, text="Mensaje Ultimos minutos -Comenzar-", command=lambda: copiar_texto('⏰ ÚLTIMOS MINUTOS!!! ⏰ Inscríbete ahora al programa: 👉 https://secure.seresderiqueza.com/comenzar 👈'), width=30, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_copiar_ultimos_minutos.grid(row=3, column=1, pady=(10, 20), padx=(10, 10))


# ------------------- BOTONES PARA PRENDER A VANESSA -------------------
boton = tk.Button(ventana, text="Prende a Vanessa", command=on_button_click, width=20, height=10, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton.grid(row=0, column=2, pady=(40, 20))


# ------------------- BOTONES PARA CAMBIAR EL TIEMPO -------------------

boton_tiempo_7 = tk.Button(ventana, text="7 segundos", command=lambda: cambiar_tiempo(7), width=20, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_tiempo_7.grid(row=2, column=2, pady=(10, 20), padx=(10, 10))

boton_tiempo_10 = tk.Button(ventana, text="10 segundos", command=lambda: cambiar_tiempo(10), width=20, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_tiempo_10.grid(row=3, column=2, pady=(10, 20), padx=(10, 10))

boton_tiempo_15 = tk.Button(ventana, text="15 segundos", command=lambda: cambiar_tiempo(15), width=20, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_tiempo_15.grid(row=4, column=2, pady=(10, 20), padx=(10, 10))
 


# ------------------- BOTONES DE SALES -------------------

boton_copiar_oxxo = tk.Button(ventana, text="Mensaje Oxxo -Sales- ", command=lambda: copiar_texto('Genera tu ficha de Oxxo 👉 https://seresderiqueza.mx/genera_ficha_oxxo_sl'), width=30, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_copiar_oxxo.grid(row=1, column=3, pady=(10, 20))

boton_copiar_spei = tk.Button(ventana, text="Mensaje Spei -Sales-", command=lambda: copiar_texto('Genera tu ficha de transferencia (SPEI) 👉  https://seresderiqueza.mx/genera_ficha_spei_sl'), width=30, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_copiar_spei.grid(row=2, column=3, pady=(10, 20))

boton_copiar_ultimos_minutos = tk.Button(ventana, text="Mensaje Ultimos minutos -Sales-", command=lambda: copiar_texto('⏰ ÚLTIMOS MINUTOS!!! ⏰ Inscríbete ahora al programa: 👉 https://seresderiqueza.mx/riqueza_infinita_sls 👈'), width=30, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_copiar_ultimos_minutos.grid(row=3, column=3, pady=(10, 20))


# ------------------- BOTONES PARA RESTABLECER FUNCION -------------------

boton_restablecer = tk.Button(ventana, text="Restablecer Función", command=restablecer_funcion, width=20, height=2, bg="#F5F5DC", font=("Arial", 10, "bold"))
boton_restablecer.grid(row=0, column=4, pady=(10, 20))


# Configuración de la función de cierre para detener todos los hilos antes de cerrar la ventana
ventana.protocol("WM_DELETE_WINDOW", lambda: [detener_proceso_func(), ventana.destroy()])

# Inicio del bucle principal de la interfaz gráfica
ventana.mainloop()
