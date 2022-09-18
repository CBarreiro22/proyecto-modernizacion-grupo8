import unittest

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.declarative_base import Session
from src.modelo.mantenimiento import Mantenimiento
from faker import Faker

class MantenimientoTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()

        '''Crea una isntancia de Faker'''
        self.data_factory = Faker()
        Faker.seed(1000)

        '''Abre la sesión'''
        self.session = Session()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los matenimientos'''
        busqueda = self.session.query(Mantenimiento).all()

        '''Borra todos los mantenimientos'''
        for mantenimiento in busqueda:
            self.session.delete(mantenimiento)
        self.session.commit()
        self.session.close()

    def test_crear_mantenimiento_01(self):
        self.logica.aniadir_mantenimiento("llanta", "cambiar presión de llantas")
        mantenimiento = self.session.query(Mantenimiento).filter(Mantenimiento.nombre == 'llanta').first()
        self.assertEqual(mantenimiento.nombre, "llanta")

    def test_no_deberia_crear_mantenimiento_por_nulos_02(self):
        self.logica.aniadir_mantenimiento("llanta", "")
        mantenimiento = self.session.query(Mantenimiento).filter(Mantenimiento.nombre == 'llanta').first()
        self.assertIsNone(mantenimiento)

    def test_no_deberia_crear_mantenimiento_por_nulos_03(self):
        self.logica.aniadir_mantenimiento("", "perfecta")
        mantenimiento = self.session.query(Mantenimiento).filter(Mantenimiento.descripcion == 'perfecta').first()
        self.assertIsNone(mantenimiento)

    def test_no_deberia_crear_mantenimiento_por_nulos_04(self):
        self.logica.aniadir_mantenimiento("llanta", "cambiar presión de llantas")
        self.assertFalse(self.logica.aniadir_mantenimiento("llanta", "cambiar presión de llantas traseras"))


