import unittest
from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.accion import Accion
from src.modelo.automovil import Automovil
from src.modelo.declarative_base import *
from datetime import datetime


class AccionTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()
        accion = Accion(mantenimiento=1, kilometraje= 200, fecha= datetime(2012, 3, 3),costo= 23.44, automovil=0 )
        self.session.add(accion)
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

        '''Consulta todos los autos'''
        busquedaAuto = self.session.query(Automovil).all()

        '''Borra todos los autos'''
        for auto in busquedaAuto:
            self.session.delete(auto)

        self.session.commit()
        self.session.close()

    #TODO- Delete this method, was created to test de dba
    def test_crearAccion_01(self):
        self.session.add(Accion(mantenimiento=2, kilometraje=1000,automovil=1 ))
        self.assertTrue (True) 
        self.session.commit()
        self.session.close()

    def test_dar_acciones_auto_02(self):
        self.logica.crear_auto("renault", "JXL530", 1970, 3200, "negro", 2000, "gasolina")
        acciones = self.logica.dar_acciones_auto(0)
        self.assertEqual(len(acciones), 1)




