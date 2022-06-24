class Alumno:
    _nombre=""
    _nota=0
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    def isAprobo(self):
        if (self._nota >= 3):
            return "aprobó"
        else:
            return "no aprobó"

alumno = Alumno("emiro",3.8)
print("nombre:",alumno._nombre)
print("nota:",alumno._nota)
print("aprobo?:",alumno.isAprobo())




        
