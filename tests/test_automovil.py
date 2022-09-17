import unittest
import random
import numpy as np

from src.modelo import automovil
from src.modelo.accion import Accion
from src.modelo.mantenimiento import Mantenimiento

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.automovil import Automovil
from faker import Faker


from src.modelo.declarative_base import Session, engine, Base


class AutomovilTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()

        renault = Automovil(marca="renault", placa="JXL539", modelo=1970, kilometraje=3200, color="negro",
                            cilindraje=2000,
                            combustible="gasolina")
        mini = Automovil(marca="mini", placa="JXL531", modelo=1970, kilometraje=3200, color="negro", cilindraje=2000,
                         combustible="gasolina")

        ford = Automovil(marca="ford", placa="JXL534", modelo=1970, kilometraje=0, color="negro", cilindraje=2000,
                         combustible="gasolina")

        renault = self.session.add(renault)

        self.session.add(mini)
        self.session.add(ford)

        '''Crea una isntancia de Faker'''
        self.data_factory = Faker()
        Faker.seed(1000)

        for i in range(0, 10):
            nombre = self.data_factory.unique.name()
            descripcion = self.data_factory.unique.text()
            self.session.add(Mantenimiento(
                nombre=nombre, descripcion=descripcion))

        kilometraje_anterior = 0
        for j in range(0, 10):

            mantenimiento = self.data_factory.random_int(1, 10)
            kilometraje = kilometraje_anterior + \
                self.data_factory.random_int(0, 10000)
            fecha = self.data_factory.date_between()
            costo = self.data_factory.random_int(0, 50000)
            self.session.add(Accion(mantenimiento=mantenimiento, kilometraje=kilometraje,
                                    fecha=fecha, costo=costo, automovil=3))
            kilometraje_anterior = kilometraje

        self.session.commit()

        self.session.close()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los autos'''
        busqueda = self.session.query(Automovil).all()

        '''Borra todos los autos'''
        # for auto in busqueda:
        #    self.session.delete(auto)

        self.session.commit()
        self.session.close()

    def test_listar_automoviles_01(self):
        autos = self.logica.dar_autos()
        self.assertEqual(len(autos), 2)

    def test_crear_automovil_01(self):
        self.logica.crear_auto("renault", "JXL530", 1970,
                               3200, "negro", 2000, "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL530').first()
        self.assertEqual(automovil.placa, "JXL530")

    def test_no_deberia_crear_automovil_02(self):
        self.logica.crear_auto(None, "JXL120", None, None, None, None, None)
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL120').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_03(self):
        self.logica.crear_auto("500", "JXL530", "A2020*/!#",
                               "3200", "negro", "2000", "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_04(self):
        self.logica.crear_auto("renault", "JX", "2020",
                               "-1", "negro", "2000", "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JX').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_05(self):
        self.logica.crear_auto("renault", "JXL530", "2020",
                               "3200", "Azul", "RFS2000", "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL530').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_06(self):
        self.logica.crear_auto("", "", "1971", "-2",
                               "negro", "2000", "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.modelo == '1971').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_07(self):
        self.logica.crear_auto("KIA", "ASF488", "1971",
                               "200", "negro", "-23", "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.marca == 'KIA').first()
        self.assertIsNone(automovil)

    def test_dar_automovil_08(self):
        auto = self.logica.dar_auto(1)
        placa = auto["placa"]
        self.assertEqual(placa, "JXL531")

    def test_vender_auto_17(self):
        chevrolet = Automovil(marca="chevrolet", placa="JXL222", modelo=1970, kilometraje=3200, color="negro",
                              cilindraje=2000, combustible="gasolina", vendido=False)
        self.session.add(chevrolet)
        self.session.commit()
        self.logica.vender_auto(2, 4000, 83.200)
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL222').first()
        self.assertEqual(automovil.vendido, True)
        self.assertEqual(automovil.valorVenta, 83.200)
        self.assertEqual(automovil.kilometrajeVenta, 4000)

    def test_validar_vender_auto_ok_18(self):
        validacion = self.logica.validar_vender_auto(2, 999999999.0, 999999999)
        validacion2 = self.logica.validar_vender_auto(2, 83.200, 4000)
        self.assertTrue(validacion)
        self.assertTrue(validacion2)

    def test_validar_vender_auto_fail_19(self):
        validacion = self.logica.validar_vender_auto(2, 83.200, -4000)
        validacion2 = self.logica.validar_vender_auto(2, -83.200, 4000)
        validacion3 = self.logica.validar_vender_auto(
            2, 8343141341324124.200, 4000)
        validacion4 = self.logica.validar_vender_auto(
            2, 24.200, 413413241324123)
        self.assertFalse(validacion)
        self.assertFalse(validacion2)
        self.assertFalse(validacion3)
        self.assertFalse(validacion4)

    def test_validar_reporte_gastos(self):
        print("probando el reporte de gastos: ")

        acciones = self.session.query(Automovil).filter(
            Automovil.id == 1).first().acciones

        total_gastos = 0

        costos = []

        for accion, i in acciones:
            total_gastos += accion.costo
            costos[i] = accion.costo

        print(total_gastos)
        promedio = np.mean(costos)
        self.assertEqual(True, True)
