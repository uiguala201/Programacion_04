#*Urbano Iguala*
#*Programa de Linea de Comandos*

from tkinter import ttk
from tkinter import *

import sqlite3

class MedProd:
    # conexion a la base de datos
    db_name = 'MedInventario.db'

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Sistema de Inventario')

        # Creamos un Marco
        frame = LabelFrame(self.wind, text = 'Registrar Nuevo Producto de Inventario')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Nombre del producto
        Label(frame, text = 'NombreMed: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Precio del Producto
        Label(frame, text = 'PrecioMed: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        # Guardar el producto
        ttk.Button(frame, text = 'Guardar Producto', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        # Mostrar Mensaje 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Tabla del Registro
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'NombreMed', anchor = CENTER)
        self.tree.heading('#1', text = 'PrecioMed', anchor = CENTER)

        # Opciones
        ttk.Button(text = 'Eliminar Producto', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'Editar Producto', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        # Llenando Productos
        self.get_products()

    # Consultas a las base de datos
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Obtener productos de la
    Base de Datos
    def get_MedProducts(self):
        # Limpiando la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Verificando la Tabla
        query = 'SELECT * FROM MedProd ORDER BY name DESC'
        db_rows = self.run_query(query)
        # Llenando los registros
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_MedProducts(self):
        if self.validation():
            query = 'INSERT INTO MedProd VALUES(NULL, ?, ?)'
            parameters =  (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'El Producto {} Fue agregado exitosamente'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Nombre y precio requerido'
        self.get_products()

    def delete_MedProducts(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccione el Registro'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM MedProd WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Registro {} Eliminado exitosamente'.format(name)
        self.get_products()

    def edit_Medroduct(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['Valores'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor, Selecciona un Registro'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['Valores'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar Registro'
        # Antiguo Nombre
        Label(self.edit_wind, text = 'Antiguo Nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
        # Nuevo Nombre
        Label(self.edit_wind, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Antiguo Precio 
        Label(self.edit_wind, text = 'Antiguo Precio:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        # Nuevo Precio
        Label(self.edit_wind, text = 'Nuevo Precio:').grid(row = 3, column = 1)
        new_price= Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE MedProd SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price,name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Registro {} actualizado exitosamente'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
