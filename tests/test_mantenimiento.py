import unittest

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.declarative_base import Session, engine, Base
from src.modelo.mantenimiento import Mantenimiento


class MantenimientoTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
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

    def test_no_deberia_crear_mantenimiento_por_longitud_descripcion_02(self):
        self.logica.aniadir_mantenimiento("llanta", "cambiar presión de llantas, Es necesario mantener una presión de "
                                                    "inflado adecuada para lograr un desempeño óptimo de la llanta, "
                                                    "preservar la seguridad y ahorrar combustible.")
        mantenimiento = self.session.query(Mantenimiento).filter(Mantenimiento.nombre == 'llanta').first()
        self.assertIsNone(mantenimiento)
