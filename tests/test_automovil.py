import unittest

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.auto import Auto

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
        busqueda = self.session.query(Auto).all()

        '''Borra todos los mantenimientos'''
        for auto in busqueda:
            self.session.delete(auto)

        self.session.commit()
        self.session.close()

    def test_crear_automovil_01(self):
        self.logica.crear_auto("renault", "JXL539", 1970, 3200, "negro", 2000, "gasolina")
        automovil = self.session.query(Auto).filter(Auto.placa == 'JXL539').first()
        self.assertEqual(automovil.placa, "JXL539")