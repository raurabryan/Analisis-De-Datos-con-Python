import tkinter as tk
from tkinter import messagebox
from laptop_Business import Laptop_Business

class AppLaptopBusiness:
    def __init__(self, root):
        self.root = root
        self.root.title("Crear Laptop Empresarial")

        self.laptop = None

        tk.Label(root, text="Marca:").grid(row=0, column=0, sticky="e")
        tk.Label(root, text="Procesador:").grid(row=1, column=0, sticky="e")
        tk.Label(root, text="Memoria RAM (GB):").grid(row=2, column=0, sticky="e")
        tk.Label(root, text="Almacenamiento:").grid(row=3, column=0, sticky="e")
        tk.Label(root, text="Duración Batería:").grid(row=4, column=0, sticky="e")

        self.entry_marca = tk.Entry(root)
        self.entry_procesador = tk.Entry(root)
        self.entry_memoria = tk.Entry(root)
        self.entry_almacenamiento = tk.Entry(root)
        self.entry_bateria = tk.Entry(root)

        self.entry_marca.grid(row=0, column=1)
        self.entry_procesador.grid(row=1, column=1)
        self.entry_memoria.grid(row=2, column=1)
        self.entry_almacenamiento.grid(row=3, column=1)
        self.entry_bateria.grid(row=4, column=1)

        tk.Button(root, text="Crear Laptop", command=self.crear_laptop).grid(row=5, columnspan=2, pady=10)
        tk.Button(root, text="Diagnóstico", command=self.mostrar_diagnostico).grid(row=6, column=0, pady=5)
        tk.Button(root, text="Verificar Red", command=self.verificar_red).grid(row=6, column=1, pady=5)

    def crear_laptop(self):
        try:
            marca = self.entry_marca.get()
            procesador = self.entry_procesador.get()
            memoria = int(self.entry_memoria.get())
            almacenamiento = self.entry_almacenamiento.get()
            bateria = self.entry_bateria.get()

            self.laptop = Laptop_Business(marca, procesador, memoria, almacenamiento, bateria)
            messagebox.showinfo("Éxito", "Laptop empresarial creada correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Verifica que la memoria sea un número entero.")

    def mostrar_diagnostico(self):
        if not self.laptop:
            messagebox.showwarning("Atención", "Primero crea una laptop.")
            return
        diag = self.laptop.realizar_diagnostico_sistema()
        resultado = "\n".join([f"{k}: {v}" for k, v in diag.items()])
        messagebox.showinfo("Diagnóstico del Sistema", resultado)

    def verificar_red(self):
        if not self.laptop:
            messagebox.showwarning("Atención", "Primero crea una laptop.")
            return
        net = self.laptop.verificar_conectividad_red()
        resultado = "\n".join([f"{k}: {'OK' if v else 'FALLÓ'}" for k, v in net.items()])
        messagebox.showinfo("Conectividad de Red", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppLaptopBusiness(root)
    root.mainloop()