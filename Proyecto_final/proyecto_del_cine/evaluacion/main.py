import tkinter as tk
from tkinter import messagebox
from peliculas import peliculas
from dulceria import dulceria
from clientes import Cliente

class GestorCinemex(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gestor Cinemex")
        self.master.geometry("")
        self.master.config(bg="#2E3A4E")
        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self.master, bg="#2E3A4E")
        self.container.pack(fill="both", expand=True)

        self.menu_gestion()

    def menu_gestion(self):
        self.clear_window()

        lbl_title = tk.Label(self.container, text="Menú de Gestión", font=("Arial", 22, "bold"), fg="#FFFFFF", bg="#2E3A4E")
        lbl_title.pack(pady=20)

        btn_peliculas = tk.Button(self.container, text="Gestión de Películas", font=("Arial", 16), bg="#4CAF50", fg="#FFFFFF", command=self.gestion_peliculas)
        btn_peliculas.pack(pady=10, fill="x")

        btn_dulceria = tk.Button(self.container, text="Gestión de Dulcería", font=("Arial", 16), bg="#FF9800", fg="#FFFFFF", command=self.gestion_dulceria)
        btn_dulceria.pack(pady=10, fill="x")

        btn_clientes = tk.Button(self.container, text="Gestión de Clientes", font=("Arial", 16), bg="#2196F3", fg="#FFFFFF", command=self.gestion_clientes)
        btn_clientes.pack(pady=10, fill="x")

        btn_exit = tk.Button(self.container, text="Salir", font=("Arial", 16), bg="#F44336", fg="#FFFFFF", command=self.quit)
        btn_exit.pack(pady=10, fill="x")

    def clear_window(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def gestion_peliculas(self):
        self.clear_window()

        lbl_title = tk.Label(self.container, text="Gestión de Películas", font=("Arial", 22, "bold"), fg="#FFFFFF", bg="#2E3A4E")
        lbl_title.pack(pady=20)

        self.create_pelicula_widgets()

        btn_back = tk.Button(self.container, text="Volver al Menú de Gestión", font=("Arial", 14, "bold"), bg="#9E9E9E", fg="#FFFFFF", command=self.menu_gestion)
        btn_back.pack(pady=10, fill="x")

    def create_pelicula_widgets(self):
        self.action_var = tk.StringVar(value="")

        action_frame = tk.Frame(self.container, bg="#2E3A4E")
        action_frame.pack(pady=10)

        actions = [("Insertar", "insertar"), ("Eliminar", "eliminar"), ("Actualizar", "actualizar"), ("Consultar", "consultar")]
        for text, value in actions:
            tk.Radiobutton(action_frame, text=text, variable=self.action_var, value=value, font=("Arial", 16), bg="#2E3A4E", fg="#FFFFFF", selectcolor="#4CAF50", command=self.update_pelicula_widgets).pack(anchor="w")

        self.entry_num_pelicula = self.create_entry("Número de Película", action_frame)
        self.entry_nombre = self.create_entry("Nombre", action_frame)
        self.entry_genero = self.create_entry("Género", action_frame)
        self.entry_duracion = self.create_entry("Duración", action_frame)
        self.entry_año = self.create_entry("Año", action_frame)

        self.update_pelicula_widgets()  # Update visibility based on default action

    def create_entry(self, label_text, parent_frame):
        frame = tk.Frame(parent_frame, bg="#2E3A4E")
        frame.pack(pady=5, fill="x")
        label = tk.Label(frame, text=label_text, font=("Arial", 16), fg="#FFFFFF", bg="#2E3A4E")
        label.pack(side="left")
        entry = tk.Entry(frame, font=("Arial", 16), bg="#FFFFFF", fg="#000000")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def update_pelicula_widgets(self):
        action = self.action_var.get()
        if action in ["insertar", "actualizar"]:
            self.entry_num_pelicula.pack(pady=10, fill="x")
            self.entry_nombre.pack(pady=10, fill="x")
            self.entry_genero.pack(pady=10, fill="x")
            self.entry_duracion.pack(pady=10, fill="x")
            self.entry_año.pack(pady=10, fill="x")
        elif action == "eliminar":
            self.entry_num_pelicula.pack(pady=10, fill="x")
            self.entry_nombre.pack_forget()
            self.entry_genero.pack_forget()
            self.entry_duracion.pack_forget()
            self.entry_año.pack_forget()
        elif action == "consultar":
            self.entry_num_pelicula.pack(pady=10, fill="x")
            self.entry_nombre.pack_forget()
            self.entry_genero.pack_forget()
            self.entry_duracion.pack_forget()
            self.entry_año.pack_forget()

        self.create_action_buttons(action)

    def create_action_buttons(self, action):
        if hasattr(self, 'action_buttons_frame'):
            self.action_buttons_frame.destroy()

        self.action_buttons_frame = tk.Frame(self.container, bg="#2E3A4E")
        self.action_buttons_frame.pack(pady=10)

        if action:
            btn_action = tk.Button(self.action_buttons_frame, text=action.capitalize(), font=("Arial", 16, "bold"), bg="#4CAF50" if action != "eliminar" else "#F44336", fg="#FFFFFF", command=lambda: getattr(self, f"{action}_pelicula")())
            btn_action.pack(pady=10, fill="x")

    def insertar_pelicula(self):
        num_pelicula = self.entry_num_pelicula.get()
        nombre = self.entry_nombre.get()
        genero = self.entry_genero.get()
        duracion = self.entry_duracion.get()
        año = self.entry_año.get()

        if num_pelicula and nombre and genero and duracion:
            pelicula = peliculas()
            pelicula.insertar(num_pelicula, nombre, genero, duracion, año)
            messagebox.showinfo("Éxito", "Película insertada con éxito")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

    def eliminar_pelicula(self):
        num_pelicula = self.entry_num_pelicula.get()

        if num_pelicula:
            pelicula = peliculas()
            pelicula.eliminar(num_pelicula)
            messagebox.showinfo("Éxito", "Película eliminada con éxito")
        else:
            messagebox.showerror("Error", "Debe ingresar el número de la película")

    def actualizar_pelicula(self):
        num_pelicula = self.entry_num_pelicula.get()
        nombre = self.entry_nombre.get()
        genero = self.entry_genero.get()
        duracion = self.entry_duracion.get()
        año = self.entry_año.get()

        if num_pelicula and nombre:
            pelicula = peliculas()
            pelicula.actualizar(num_pelicula, nombre, genero, duracion, año)
            messagebox.showinfo("Éxito", "Película actualizada con éxito")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

    def consultar_pelicula(self):
        num_pelicula = self.entry_num_pelicula.get()

        if num_pelicula:
            pelicula = peliculas()
            datos = pelicula.consultar(num_pelicula)
            if datos:
                self.entry_nombre.delete(0, tk.END)
                self.entry_nombre.insert(0, datos['nombre'])
                self.entry_genero.delete(0, tk.END)
                self.entry_genero.insert(0, datos['genero'])
                self.entry_duracion.delete(0, tk.END)
                self.entry_duracion.insert(0, datos['duracion'])
                self.entry_año.delete(0, tk.END)
                self.entry_año.insert(0, datos['año'])
                messagebox.showinfo("Consulta Exitosa", "Datos de la película consultados")
            else:
                messagebox.showerror("Error", "Película no encontrada")
        else:
            messagebox.showerror("Error", "Debe ingresar el número de la película")

    def gestion_dulceria(self):
        self.clear_window()

        lbl_title = tk.Label(self.container, text="Gestión de Dulcería", font=("Arial", 22, "bold"), fg="#FFFFFF", bg="#2E3A4E")
        lbl_title.pack(pady=20)

        self.create_dulceria_widgets()

        btn_back = tk.Button(self.container, text="Volver al Menú de Gestión", font=("Arial", 14, "bold"), bg="#9E9E9E", fg="#FFFFFF", command=self.menu_gestion)
        btn_back.pack(pady=10, fill="x")

    def create_dulceria_widgets(self):
        self.dulceria_action_var = tk.StringVar(value="")

        action_frame = tk.Frame(self.container, bg="#2E3A4E")
        action_frame.pack(pady=10)

        dulceria_actions = [("Insertar", "insertar_dulce"), ("Eliminar", "eliminar_dulce"), ("Actualizar", "actualizar_dulce"), ("Consultar", "consultar_dulce")]
        for text, value in dulceria_actions:
            tk.Radiobutton(action_frame, text=text, variable=self.dulceria_action_var, value=value, font=("Arial", 16), bg="#2E3A4E", fg="#FFFFFF", selectcolor="#FF9800", command=self.update_dulceria_widgets).pack(anchor="w")

        self.entry_dulce_id = self.create_entry("ID del Dulce", action_frame)
        self.entry_dulce_nombre = self.create_entry("Nombre", action_frame)
        self.entry_dulce_precio = self.create_entry("Precio", action_frame)
        self.entry_dulce_cantidad = self.create_entry("Cantidad", action_frame)

        self.update_dulceria_widgets()  # Update visibility based on default action

    def update_dulceria_widgets(self):
        action = self.dulceria_action_var.get()
        if action in ["insertar_dulce", "actualizar_dulce"]:
            self.entry_dulce_id.pack(pady=10, fill="x")
            self.entry_dulce_nombre.pack(pady=10, fill="x")
            self.entry_dulce_precio.pack(pady=10, fill="x")
            self.entry_dulce_cantidad.pack(pady=10, fill="x")
        elif action == "eliminar_dulce":
            self.entry_dulce_id.pack(pady=10, fill="x")
            self.entry_dulce_nombre.pack_forget()
            self.entry_dulce_precio.pack_forget()
            self.entry_dulce_cantidad.pack_forget()
        elif action == "consultar_dulce":
            self.entry_dulce_id.pack(pady=10, fill="x")
            self.entry_dulce_nombre.pack_forget()
            self.entry_dulce_precio.pack_forget()
            self.entry_dulce_cantidad.pack_forget()

        self.create_dulceria_action_buttons(action)

    def create_dulceria_action_buttons(self, action):
        if hasattr(self, 'dulceria_action_buttons_frame'):
            self.dulceria_action_buttons_frame.destroy()

        self.dulceria_action_buttons_frame = tk.Frame(self.container, bg="#2E3A4E")
        self.dulceria_action_buttons_frame.pack(pady=10)

        if action:
            btn_action = tk.Button(self.dulceria_action_buttons_frame, text=action.split('_')[0].capitalize(), font=("Arial", 16, "bold"), bg="#FF9800" if action != "eliminar_dulce" else "#F44336", fg="#FFFFFF", command=lambda: getattr(self, action)())
            btn_action.pack(pady=10, fill="x")

    def insertar_dulce(self):
        dulce_id = self.entry_dulce_id.get()
        nombre = self.entry_dulce_nombre.get()
        precio = self.entry_dulce_precio.get()
        cantidad = self.entry_dulce_cantidad.get()

        if dulce_id and nombre and precio and cantidad:
            dulce = dulceria()
            dulce.insertar(dulce_id, nombre, precio, cantidad)
            messagebox.showinfo("Éxito", "Dulce insertado con éxito")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

    def eliminar_dulce(self):
        dulce_id = self.entry_dulce_id.get()

        if dulce_id:
            dulce = dulceria()
            dulce.eliminar(dulce_id)
            messagebox.showinfo("Éxito", "Dulce eliminado con éxito")
        else:
            messagebox.showerror("Error", "Debe ingresar el ID del dulce")

    def actualizar_dulce(self):
        dulce_id = self.entry_dulce_id.get()
        nombre = self.entry_dulce_nombre.get()
        precio = self.entry_dulce_precio.get()
        cantidad = self.entry_dulce_cantidad.get()

        if dulce_id and nombre:
            dulce = dulceria()
            dulce.actualizar(dulce_id, nombre, precio, cantidad)
            messagebox.showinfo("Éxito", "Dulce actualizado con éxito")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

    def consultar_dulce(self):
        dulce_id = self.entry_dulce_id.get()

        if dulce_id:
            dulce = dulceria()
            datos = dulce.consultar(dulce_id)
            if datos:
                self.entry_dulce_nombre.delete(0, tk.END)
                self.entry_dulce_nombre.insert(0, datos['nombre'])
                self.entry_dulce_precio.delete(0, tk.END)
                self.entry_dulce_precio.insert(0, datos['precio'])
                self.entry_dulce_cantidad.delete(0, tk.END)
                self.entry_dulce_cantidad.insert(0, datos['cantidad'])
                messagebox.showinfo("Consulta Exitosa", "Datos del dulce consultados")
            else:
                messagebox.showerror("Error", "Dulce no encontrado")
        else:
            messagebox.showerror("Error", "Debe ingresar el ID del dulce")

    def gestion_clientes(self):
        self.clear_window()

        lbl_title = tk.Label(self.container, text="Gestión de Clientes", font=("Arial", 22, "bold"), fg="#FFFFFF", bg="#2E3A4E")
        lbl_title.pack(pady=20)

        self.create_cliente_widgets()

        btn_back = tk.Button(self.container, text="Volver al Menú de Gestión", font=("Arial", 14, "bold"), bg="#9E9E9E", fg="#FFFFFF", command=self.menu_gestion)
        btn_back.pack(pady=10, fill="x")

    def create_cliente_widgets(self):
        self.cliente_action_var = tk.StringVar(value="")

        action_frame = tk.Frame(self.container, bg="#2E3A4E")
        action_frame.pack(pady=10)

        cliente_actions = [("Insertar", "insertar_cliente"), ("Eliminar", "eliminar_cliente"), ("Actualizar", "actualizar_cliente"), ("Consultar", "consultar_cliente")]
        for text, value in cliente_actions:
            tk.Radiobutton(action_frame, text=text, variable=self.cliente_action_var, value=value, font=("Arial", 16), bg="#2E3A4E", fg="#FFFFFF", selectcolor="#2196F3", command=self.update_cliente_widgets).pack(anchor="w")

        self.entry_cliente_id = self.create_entry("ID del Cliente", action_frame)
        self.entry_cliente_nombre = self.create_entry("Nombre", action_frame)
        self.entry_cliente_correo = self.create_entry("Correo", action_frame)
        self.entry_cliente_telefono = self.create_entry("Teléfono", action_frame)

        self.update_cliente_widgets()  # Update visibility based on default action

    def update_cliente_widgets(self):
        action = self.cliente_action_var.get()
        if action in ["insertar_cliente", "actualizar_cliente"]:
            self.entry_cliente_id.pack(pady=10, fill="x")
            self.entry_cliente_nombre.pack(pady=10, fill="x")
            self.entry_cliente_correo.pack(pady=10, fill="x")
            self.entry_cliente_telefono.pack(pady=10, fill="x")
        elif action == "eliminar_cliente":
            self.entry_cliente_id.pack(pady=10, fill="x")
            self.entry_cliente_nombre.pack_forget()
            self.entry_cliente_correo.pack_forget()
            self.entry_cliente_telefono.pack_forget()
        elif action == "consultar_cliente":
            self.entry_cliente_id.pack(pady=10, fill="x")
            self.entry_cliente_nombre.pack_forget()
            self.entry_cliente_correo.pack_forget()
            self.entry_cliente_telefono.pack_forget()

        self.create_cliente_action_buttons(action)

    def create_cliente_action_buttons(self, action):
        if hasattr(self, 'cliente_action_buttons_frame'):
            self.cliente_action_buttons_frame.destroy()

        self.cliente_action_buttons_frame = tk.Frame(self.container, bg="#2E3A4E")
        self.cliente_action_buttons_frame.pack(pady=10)

        if action:
            btn_action = tk.Button(self.cliente_action_buttons_frame, text=action.split('_')[0].capitalize(), font=("Arial", 16, "bold"), bg="#2196F3" if action != "eliminar_cliente" else "#F44336", fg="#FFFFFF", command=lambda: getattr(self, action)())
            btn_action.pack(pady=10, fill="x")

    def insertar_cliente(self):
        cliente_id = self.entry_cliente_id.get()
        nombre = self.entry_cliente_nombre.get()
        correo = self.entry_cliente_correo.get()
        telefono = self.entry_cliente_telefono.get()

        if cliente_id and nombre and correo and telefono:
            cliente = Cliente()
            cliente.insertar(cliente_id, nombre, correo, telefono)
            messagebox.showinfo("Éxito", "Cliente insertado con éxito")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

    def eliminar_cliente(self):
        cliente_id = self.entry_cliente_id.get()

        if cliente_id:
            cliente = Cliente()
            cliente.eliminar(cliente_id)
            messagebox.showinfo("Éxito", "Cliente eliminado con éxito")
        else:
            messagebox.showerror("Error", "Debe ingresar el ID del cliente")

    def actualizar_cliente(self):
        cliente_id = self.entry_cliente_id.get()
        nombre = self.entry_cliente_nombre.get()
        correo = self.entry_cliente_correo.get()
        telefono = self.entry_cliente_telefono.get()

        if cliente_id and nombre:
            cliente = Cliente()
            cliente.actualizar(cliente_id, nombre, correo, telefono)
            messagebox.showinfo("Éxito", "Cliente actualizado con éxito")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

    def consultar_cliente(self):
        cliente_id = self.entry_cliente_id.get()

        if cliente_id:
            cliente = Cliente()
            datos = cliente.consultar(cliente_id)
            if datos:
                self.entry_cliente_nombre.delete(0, tk.END)
                self.entry_cliente_nombre.insert(0, datos['nombre'])
                self.entry_cliente_correo.delete(0, tk.END)
                self.entry_cliente_correo.insert(0, datos['correo'])
                self.entry_cliente_telefono.delete(0, tk.END)
                self.entry_cliente_telefono.insert(0, datos['telefono'])
                messagebox.showinfo("Consulta Exitosa", "Datos del cliente consultados")
            else:
                messagebox.showerror("Error", "Cliente no encontrado")
        else:
            messagebox.showerror("Error", "Debe ingresar el ID del cliente")


if __name__ == "__main__":
    root = tk.Tk()
    app = GestorCinemex(master=root)
    app.mainloop()