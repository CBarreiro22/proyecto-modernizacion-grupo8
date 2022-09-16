import unittest
from src.modelo.automovil import Automovil
from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo.accion import Accion
from src.modelo.declarative_base import *
from datetime import datetime
from src.modelo.mantenimiento import Mantenimiento


class AccionTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = auto_perfecto()
        '''Abre la sesión'''
        self.session = Session()
        accion = Accion(mantenimiento=1, kilometraje= 200, fecha= datetime(2012, 3, 3),costo= 23.44, automovil=0 )
        mantenimiento = Mantenimiento(nombre="ventanales", descripcion="reparar sistema central")
        
        '''creación de automovil'''
        automovil = Automovil ( marca="la marca",placa="la placa",modelo=2022, kilometraje=1000,
                               color="azul",cilindraje=100, combustible="gasolina", vendido=False)
        
        self.session.add (automovil)
        
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

       
        
        self.session.commit()

        '''Consulta todos los matenimientos'''
        busquedaMatenimientos = self.session.query(Mantenimiento).all()

        '''Borra todos los mantenimientos'''
        for mantenimiento in busquedaMatenimientos:
            self.session.delete(mantenimiento)

        self.session.commit()
        self.session.close()

    def test_dar_acciones_auto_02(self):
        acciones = self.logica.dar_acciones_auto(0)
        self.assertEqual(len(acciones), 1)

    def test_no_deberia_dar_acciones_auto_03(self):
        acciones = self.logica.dar_acciones_auto(1)
        self.assertEqual(len(acciones), 0)
        
    def test_crear_accion_auto(self):
        self.logica.crear_accion(mantenimiento=1, id_auto=1, valor=2000, kilometraje=30000,fecha=datetime(2020, 3, 3))
        accion = self.session.query(Accion).filter(Accion.id==1).first()
        self.assertEqual (accion.id,1)
        
    def test_crear_accion_auto_validacion_01(self):
        self.logica.crear_accion(mantenimiento=1, id_auto=1, valor=-1, kilometraje=301,fecha=datetime.now())
        accion = self.session.query(Accion).filter(Accion.kilometraje==1).first()
        self.assertIsNone(accion)
        
    def test_crear_accion_auto_validacion_02(self):
        self.logica.crear_accion(mantenimiento=1, id_auto=1, valor=21654.23, kilometraje=-1,fecha=datetime.now())
        accion = self.session.query(Accion).filter(Accion.costo==21654.23).first()
        self.assertIsNone (accion)
        
    


