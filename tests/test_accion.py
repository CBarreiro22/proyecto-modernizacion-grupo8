import unittest
from src.modelo.automovil import Automovil
from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.accion import Accion
from src.modelo.declarative_base import *
from datetime import datetime
from src.modelo.mantenimiento import Mantenimiento
from faker import Faker


class AccionTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()

        '''Crea una isntancia de Faker'''
        self.data_factory = Faker()
        Faker.seed(1000)

        accion = Accion(mantenimiento=1, kilometraje=self.data_factory.random_int(0, 10000),
                        fecha=self.data_factory.date_between(), costo=self.data_factory.random_int(0, 50000),
                        automovil=2)
        mantenimiento = Mantenimiento(nombre=self.data_factory.unique.name(),
                                      descripcion=self.data_factory.unique.text())

        '''creación de automovil'''
        automovil = Automovil(marca=self.data_factory.company(), placa="JKL444",
                              modelo=self.data_factory.random_int(1886, 2022),
                              kilometraje=self.data_factory.random_int(0, 10000),
                              color=self.data_factory.color_name(), cilindraje=self.data_factory.random_int(0, 1000),
                              combustible="gasolina", vendido=self.data_factory.boolean(chance_of_getting_true=50))
        automovil2 = Automovil(marca=self.data_factory.company(), placa="JKL333",
                               modelo=self.data_factory.random_int(1886, 2022),
                               kilometraje=self.data_factory.random_int(0, 10000),
                               color=self.data_factory.color_name(), cilindraje=self.data_factory.random_int(0, 1000),
                               combustible="gasolina", vendido=self.data_factory.boolean(chance_of_getting_true=50))

        self.session.add(automovil)
        self.session.add(automovil2)
        self.session.add(accion)
        self.session.add(mantenimiento)
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
        '''Consulta todos los matenimientos'''
        busquedaMatenimientos = self.session.query(Mantenimiento).all()
        '''Borra todos los mantenimientos'''
        for mantenimiento in busquedaMatenimientos:
            self.session.delete(mantenimiento)
        '''Consulta todos los autos'''
        busquedaAutos = self.session.query(Automovil).all()
        '''Borra todos los autos'''
        for auto in busquedaAutos:
            self.session.delete(auto)
        self.session.commit()
        self.session.close()

    def test_dar_acciones_auto_02(self):
        acciones = self.logica.dar_acciones_auto(1)
        self.assertEqual(len(acciones), 1)

    def test_no_deberia_dar_acciones_auto_03(self):
        acciones = self.logica.dar_acciones_auto(0)
        self.assertEqual(len(acciones), 0)

    def test_crear_accion_auto(self):
        self.logica.crear_accion(mantenimiento=1, id_auto=0, valor=self.data_factory.random_int(0, 50000),
                                 kilometraje=self.data_factory.random_int(0, 10000),
                                 fecha="2020-03-03")
        accion = self.session.query(Accion).filter(Accion.id == 1).first()
        self.assertEqual(accion.id, 1)

    def test_crear_accion_auto_validacion_01(self):
        self.logica.crear_accion(mantenimiento=1, id_auto=0, valor=-1,
                                 kilometraje=self.data_factory.random_int(0, 10000), fecha=datetime.now())
        accion = self.session.query(Accion).filter(Accion.kilometraje == 1).first()
        self.assertIsNone(accion)

    def test_crear_accion_auto_validacion_02(self):
        self.logica.crear_accion(mantenimiento=1, id_auto=0, valor=21654.23, kilometraje=-1, fecha=datetime.now())
        accion = self.session.query(Accion).filter(Accion.costo == 21654.23).first()
        self.assertIsNone(accion)

    def test_deberia_editar_accion_caso10(self):
        self.logica.editar_accion(0, 1, 1, self.data_factory.random_int(0, 50000), 4000, "2020-03-02")
        accion = self.logica.dar_accion(1, 0)
        self.assertEqual(accion["kilometraje"], 4000)
        self.assertEqual(accion["fecha"], "2020-03-02")

    def test_no_deberia_editar_accion_caso11(self):
        self.logica.editar_accion(0, 1, 1, self.data_factory.random_int(0, 50000), 40000000000000, "2020-03-02")
        accion = self.logica.dar_accion(1, 0)
        self.assertNotEqual(accion["fecha"], "2020-03-03")
