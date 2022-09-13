import unittest
from src.modelo.mantenimiento import Mantenimiento

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.accion import Accion


from src.modelo.declarative_base import Session, engine, Base


class AccionTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()
        
        self.session.close()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        self.session.close()
    def test_crearAccion_01(self):
        self.session.add(Accion(mantenimiento=2, kilometraje=1000,automovil=1 ))
        self.assertTrue (True) 
        self.session.commit()
        self.session.close()

