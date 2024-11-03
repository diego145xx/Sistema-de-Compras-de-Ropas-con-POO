class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo privado (encapsulación)
        self._precio = precio

    def obtener_detalle(self):
        return f"{self._nombre}: ${self._precio}"
class Camisa(Producto):
        def __init__(self, nombre, precio, talla):
            super().__init__(nombre, precio)
            self._talla = talla  # Atributo específico de Camisa
            
def obtener_detalle(self):
        return f"{self._nombre} (Talla: {self._talla}): ${self._precio}"  # Sobrescritura (polimorfismo)

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def obtener_detalle(self):
        return f"{self._nombre} (Talla: {self._talla}): ${self._precio}"

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def obtener_detalle(self):
        return f"{self._nombre} (Talla: {self._talla}): ${self._precio}"

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Productos en la categoría {self.nombre}:")
        for producto in self.productos:
            print(producto.obtener_detalle())

class Tienda:
    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def realizar_compra(self):
        total = 0
        print("Realizando compra...")
        for categoria in self.categorias:
            categoria.mostrar_productos()
            for producto in categoria.productos:
                total += producto._precio  # Acceso a atributo protegido
        print(f"Total de la compra: ${total}")

# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda()

    categoria_camisetas = Categoria("Camisetas")
    categoria_camisetas.agregar_producto(Camisa("Camisa Azul", 20, "M"))
    categoria_camisetas.agregar_producto(Camisa("Camisa Roja", 25, "L"))

    categoria_pantalones = Categoria("Pantalones")
    categoria_pantalones.agregar_producto(Pantalon("Pantalón Negro", 30, "32"))
    categoria_pantalones.agregar_producto(Pantalon("Pantalón Verde", 35, "34"))

    categoria_zapatos = Categoria("Zapatos")
    categoria_zapatos.agregar_producto(Zapato("Zapato Deportivo", 50, "42"))
    categoria_zapatos.agregar_producto(Zapato("Zapato Formal", 70, "44"))

    tienda.agregar_categoria(categoria_camisetas)
    tienda.agregar_categoria(categoria_pantalones)
    tienda.agregar_categoria(categoria_zapatos)

    tienda.realizar_compra()