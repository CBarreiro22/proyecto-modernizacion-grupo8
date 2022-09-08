import unittest

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.auto import Auto

from src.modelo.declarative_base import Session, engine, Base


class AutomovilTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()
        renault = Auto(marca="renault", placa="JXL539", modelo=1970, kilometraje=3200, color="negro", cilindraje=2000,
                       combustible="gasolina")
        mini = Auto(marca="mini", placa="JXL531", modelo=1970, kilometraje=3200, color="negro", cilindraje=2000,
                    combustible="gasolina")
        self.session.add(renault)
        self.session.add(mini)
        self.session.commit()
        self.session.close()

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

    def test_listar_automoviles_01(self):
        autos = self.logica.dar_autos()
        self.assertEqual(len(autos), 2)

    def test_crear_automovil_01(self):
        self.logica.crear_auto("renault", "JXL530", 1970, 3200, "negro", 2000, "gasolina")
        automovil = self.session.query(Auto).filter(Auto.placa == 'JXL530').first()
        self.assertEqual(automovil.placa, "JXL530")
