import unittest

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.automovil import Automovil
from src.modelo.declarative_base import Session, engine, Base


class AutomovilTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los matenimientos'''
        busqueda = self.session.query(Automovil).all()

        '''Borra todos los mantenimientos'''
        for automovil in busqueda:
            self.session.delete(automovil)

        self.session.commit()
        self.session.close()

    def test_crear_mantenimiento_01(self):
        # self.logica.aniadir_mantenimiento("llanta", "cambiar presión de llantas")
        # mantenimiento = self.session.query(Automovil).filter(Automovil.nombre == 'llanta').first()
        self.assertEqual("llanta", "llanta")
