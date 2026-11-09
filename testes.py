import tkinter as tk

def obtener_texto():
    # Extrae el texto desde el inicio (1.0) hasta el final (end)
    texto_ingresado = cuadro_texto.get("1.0", tk.END).strip()
    print("Escribiste:", texto_ingresado)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana Interactiva")
ventana.geometry("300x200")

# Crear caja de texto (Text widget)
cuadro_texto = tk.Text(ventana, height=5, width=30)
cuadro_texto.pack(pady=10)

# Crear botón de acción
boton = tk.Button(ventana, text="Imprimir Texto", command=obtener_texto)
boton.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()