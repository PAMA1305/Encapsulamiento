import tkinter as tk

class Window:
    __ancho=200
    __alto=100
    __titulo="Test"
    __resize=False

    def setDimensions(self, width, height):
        self.__ancho=width
        self.__alto=height

    def getDimensions(self):
        return [self.__ancho, self.__alto]

    def setResize(self, resize):
        self.__resize=resize
    def getResize(self):
        return self.__resize

    def setTitulo(self, titulo):
        self.__titulo=titulo
    def getTitulo(self):
        return self.__titulo

    def crear_ventana(self):
        # Crear la ventana principal

        ventana = tk.Tk()

        ventana.title(self.__titulo)

        ventana.geometry(f"{self.__ancho}x{self.__alto}")

        ventana.resizable(self.__resize, self.__resize)

        ventana.mainloop()


