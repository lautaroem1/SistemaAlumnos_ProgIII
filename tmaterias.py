from materia import Materia
from functools import reduce
from bisect import insort


class TMaterias:
    def __init__(self):
        self.listado = []
        self.key_materias = [
            'Matematica',
            'Lengua',
            'Fisica',
            'Quimica',
            'Biologia',
            'Etica',
            'Historia',
            'Geografia',
            'Computacion'
        ]

    def alta(self, mat: Materia):
        if mat.get_nombre() not in self.key_materias:
            raise KeyError('El nombre de la materia es inválida.')
        else:
            for val in self.listado:
                if mat.get_nombre() == val.get_nombre() and mat.get_nro_reg() == val.get_nro_reg():
                    raise KeyError('Ya existe la materia.')
            self.listado.append(mat)

    def baja(self, nro_reg: int, nombre: str):
        for val in self.listado:
            if nro_reg == val.get_nro_reg() and nombre == val.get_nombre():
                self.listado.remove(val)
                break
        else:
            raise KeyError('La materia no se encuentra.')

    def baja_total(self, nro_reg: int):
        to_remove = []
        for val in self.listado:
            if val.get_nro_reg() == nro_reg:
                to_remove.append(val)
        for val in to_remove:
            self.listado.remove(val)

    def modificar(self, mat: Materia):
        self.baja(mat.get_nro_reg(), mat.get_nombre())
        self.alta(mat)

    def consulta(self, nro_reg: int, nombre: str):
        if nombre not in self.key_materias:
            raise KeyError('El nombre de la materia es inválida.')
        else:
            for val in self.listado:
                if nro_reg == val.get_nro_reg()and nombre == val.get_nombre():
                    return val
            else:
                raise KeyError('La materia no se encuentra.')

    def get_materias(self):
        return self.listado

    def get_materias_alumno(self, nro_reg: int):
        return list(filter(lambda m: m.get_nro_reg() == nro_reg, self.listado))
