import unittest
from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.accion import Accion
from src.modelo.declarative_base import *
from datetime import datetime
from src.modelo.mantenimiento import Mantenimiento


class AccionTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()
        accion = Accion(mantenimiento=1, kilometraje= 200, fecha= datetime(2012, 3, 3),costo= 23.44, automovil=0 )
        mantenimiento = Mantenimiento(nombre="ventanales", descripcion="reparar sistema central")
        self.session.add(accion)
        self.session.add(mantenimiento)
        self.session.commit()
        self.session.close()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()
        '''Consulta todas las acciones'''
        busqueda = self.session.query(Accion).all()

        '''Borra todas las acciones'''
        for accion in busqueda:
            self.session.delete(accion)

        self.session.commit()

        '''Consulta todos los matenimientos'''
        busquedaMatenimientos = self.session.query(Mantenimiento).all()

        '''Borra todos los mantenimientos'''
        for mantenimiento in busquedaMatenimientos:
            self.session.delete(mantenimiento)

        self.session.commit()
        self.session.close()

    def test_dar_acciones_auto_02(self):
        acciones = self.logica.dar_acciones_auto(0)
        self.assertEqual(len(acciones), 1)

    def test_no_deberia_dar_acciones_auto_03(self):
        acciones = self.logica.dar_acciones_auto(1)
        self.assertEqual(len(acciones), 0)




