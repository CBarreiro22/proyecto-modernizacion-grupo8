import unittest

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.automovil import Automovil

from src.modelo.declarative_base import Session, engine, Base


class AutomovilTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()
        renault = Automovil(marca="renault", placa="JXL539", modelo=1970, kilometraje=3200, color="negro", cilindraje=2000,
                            combustible="gasolina")
        mini = Automovil(marca="mini", placa="JXL531", modelo=1970, kilometraje=3200, color="negro", cilindraje=2000,
                         combustible="gasolina")
        self.session.add(renault)
        self.session.add(mini)
        self.session.commit()
        self.session.close()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los matenimientos'''
        busqueda = self.session.query(Automovil).all()

        '''Borra todos los mantenimientos'''
        for auto in busqueda:
            self.session.delete(auto)

        self.session.commit()
        self.session.close()

    def test_listar_automoviles_01(self):
        autos = self.logica.dar_autos()
        self.assertEqual(len(autos), 2)

    def test_crear_automovil_01(self):
        self.logica.crear_auto("renault", "JXL530", 1970, 3200, "negro", 2000, "gasolina")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL530').first()
        self.assertEqual(automovil.placa, "JXL530")

    def test_no_deberia_crear_automovil_02(self):
        self.logica.crear_auto(None, "JXL120", None, None, None, None, None)
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL120').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_03(self):
        self.logica.crear_auto("re", "JXL530", 1970, 3200, "negro", 2000, "gasolina")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_04(self):
        self.logica.crear_auto("renault", "JX", 1970, 3200, "negro", 2000, "gasolina")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JX').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_05(self):
        self.logica.crear_auto("renault", "JXL530", 197, 3200, "negro", 2000, "gasolina")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_06(self):
        self.logica.crear_auto("renault", "JXL530", 1970, -2, "negro", 2000, "gasolina")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_07(self):
        self.logica.crear_auto("renault", "JXL530", 1970, 3200, "ne", 2000, "gasolina")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_08(self):
        self.logica.crear_auto("renault", "JXL530", 1970, 3200, "negro", -2, "gasolina")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_09(self):
        self.logica.crear_auto("renault", "JXL530", 1970, 3200, "negro", 2000, "ga")
        automovil = self.session.query(Automovil).filter(Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)
