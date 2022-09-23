
import unittest

from faker import Faker
from src.modelo.mantenimiento import Mantenimiento
from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.automovil import Automovil
from src.modelo.accion import Accion
from src.modelo.declarative_base import Session


class AutomovilTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()

        '''Crea una isntancia de Faker'''
        self.data_factory = Faker()
        Faker.seed(1000)

        renault = Automovil(marca=self.data_factory.company(), placa=self.data_factory.license_plate(),
                            modelo=self.data_factory.random_int(1886, 2022),
                            kilometraje=self.data_factory.random_int(0, 10000), color=self.data_factory.color_name(),
                            cilindraje=self.data_factory.random_int(0, 1000),
                            combustible="gasolina")
        mini = Automovil(marca=self.data_factory.company(), placa=self.data_factory.license_plate(),
                         modelo=self.data_factory.random_int(1886, 2022),
                         kilometraje=self.data_factory.random_int(0, 10000), color=self.data_factory.color_name(),
                         cilindraje=self.data_factory.random_int(0, 1000),
                         combustible="gasolina")
        self.session.add (Automovil(marca=self.data_factory.company(), placa="to_test_delete_1234",
                         modelo=self.data_factory.random_int(1886, 2022),
                         kilometraje=self.data_factory.random_int(0, 10000), color=self.data_factory.color_name(),
                         cilindraje=self.data_factory.random_int(0, 1000),
                         combustible="gasolina"))
        ford = Automovil(marca=self.data_factory.company(), placa="to_test_delete_123",
                         modelo=self.data_factory.random_int(1886, 2022),
                         kilometraje=self.data_factory.random_int(0, 10000), color=self.data_factory.color_name(),
                         cilindraje=self.data_factory.random_int(0, 1000),
                         combustible="gasolina")
        nombre_mantenimiento = self.data_factory.unique.name()
        self.session.add(Mantenimiento(nombre=nombre_mantenimiento,
                                       descripcion=self.data_factory.unique.text()))

        self.session.add(ford)
        mantenimiento = self.session.query(Mantenimiento).filter(
            Automovil.placa == 'to_test_delete_123').first()

        ford = self.session.query(Automovil).filter(
            Mantenimiento.nombre == nombre_mantenimiento).first()

        for i in range(0, 10):
            self.session.add(Accion(mantenimiento=mantenimiento.id,
                                    kilometraje=self.data_factory.random_int(
                                        1, 99999999),
                                    fecha=self.data_factory.date_between(),
                                    costo=self.data_factory.random_int(
                                        1, 99999999),
                                    automovil=ford.id))

        self.session.add(renault)

        self.session.add(mini)

        self.session.commit()

        self.session.close()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los autos'''
        acciones = self.session.query(Accion).all()
        for accion in acciones:
            self.session.delete(accion)

        mantenimientos = self.session.query(Mantenimiento).all()
        for mantenimiento in mantenimientos:
            self.session.delete(mantenimiento)

        autos = self.session.query(Automovil).all()
        for auto in autos:
            self.session.delete(auto)

        self.session.commit()
        self.session.close()

    def test_verificar_existencia_listar_automoviles_01(self):
        autos = self.logica.dar_autos()
        self.assertIsNotNone(autos)

    def test_deberia_crear_automovil_01(self):
        self.logica.crear_auto("reault5", "JXL530", self.data_factory.random_int(1886, 2022),
                               self.data_factory.random_int(
                                   0, 10000), self.data_factory.color_name(),
                               self.data_factory.random_int(0, 1000), "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL530').first()
        self.assertEqual(automovil.placa, "JXL530")

    def test_no_deberia_crear_automovil_valores_nulos_02(self):
        self.logica.crear_auto(None, "JXL120", None, None, None, None, None)
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL120').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_modelo_invalido_03(self):
        self.logica.crear_auto("500", "JXL74983", "A2020*/!#",
                               self.data_factory.random_int(
                                   0, 10000), self.data_factory.color_name(),
                               self.data_factory.random_int(0, 1000), "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL74983').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_placa_invalida_04(self):
        self.logica.crear_auto(self.data_factory.company(), "JX", self.data_factory.random_int(1886, 2022),
                               "-1", self.data_factory.color_name(), self.data_factory.random_int(0, 1000), "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JX').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_cilindraje_invalido_05(self):
        self.logica.crear_auto(self.data_factory.company(), "JXL74", self.data_factory.random_int(1886, 2022),
                               self.data_factory.random_int(
                                   0, 1000), self.data_factory.color_name(), "RFS2000",
                               "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL74').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_kilometrjae_invalido_06(self):
        self.logica.crear_auto("", "", "1971", "-2",
                               self.data_factory.color_name(), self.data_factory.random_int(0, 1000), "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.modelo == '1971').first()
        self.assertIsNone(automovil)

    def test_no_deberia_crear_automovil_cilindraje_invalido_07(self):
        self.logica.crear_auto("KIA", self.data_factory.license_plate(), self.data_factory.random_int(1886, 2022),
                               self.data_factory.random_int(
                                   0, 10000), self.data_factory.color_name(), "-23",
                               "gasolina")
        automovil = self.session.query(Automovil).filter(
            Automovil.marca == 'KIA').first()
        self.assertIsNone(automovil)

    def test_deberia_vender_auto_17(self):
        chevrolet = Automovil(marca=self.data_factory.company(), placa="JXL77777",
                              modelo=self.data_factory.random_int(1886, 2022),
                              kilometraje=self.data_factory.random_int(0, 10000), color=self.data_factory.color_name(),
                              cilindraje=self.data_factory.random_int(0, 1000), combustible="gasolina", vendido=True)
        self.session.add(chevrolet)
        self.session.commit()
        self.logica.vender_auto(2, 4000, 83.200)
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL77777').first()
        self.assertEqual(automovil.vendido, True)
        self.assertEqual(automovil.valorVenta, 83.200)
        self.assertEqual(automovil.kilometrajeVenta, 4000)

    def test_validar_vender_auto_ok_18(self):
        validacion = self.logica.validar_vender_auto(2, 999999999.0, 999999999)
        validacion2 = self.logica.validar_vender_auto(2, 83.200, 4000)
        self.assertTrue(validacion)
        self.assertTrue(validacion2)

    def test_validar_vender_auto_fail_parametros_invalidos_19(self):
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

    def test_deberia_editar_auto_30(self):
        chevrolet2 = Automovil(marca=self.data_factory.company(), placa="JXL77776",
                               modelo=self.data_factory.random_int(1886, 2022),
                               kilometraje=self.data_factory.random_int(0, 10000), color=self.data_factory.color_name(),
                               cilindraje=self.data_factory.random_int(0, 1000), combustible="gasolina", vendido=True)
        self.session.add(chevrolet2)
        self.session.commit()
        self.logica.editar_auto(0, "renualt", "JXL77777", "2000", "3000", "blanco", "3000", "diesel55")
        automovil = self.session.query(Automovil).filter(
            Automovil.placa == 'JXL77777').first()
        self.assertEqual(automovil.combustible, "diesel55")

    def test_borrar_auto_exitoso(self):

        self.logica.eliminar_auto(1)

        autoEliminado = self.session.query(Automovil).filter(
            Automovil.placa == 'to_test_delete_123').first()
        self.assertIsNone (autoEliminado)
        
    def test_borrar_auto_con_acciones(self):

        self.logica.eliminar_auto(0)

        autoEliminado = self.session.query(Automovil).filter(
            Automovil.placa == 'to_test_delete_1234').first()
        self.assertIsNotNone (autoEliminado)

    def test_verificar_orden_lista_32(self):
        autos = self.logica.dar_autos()
        self.assertEqual(autos[0]["placa"], "to_test_delete_1234")
        self.assertEqual(autos[1]["placa"], "to_test_delete_123")
        
        
        
