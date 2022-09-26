import random
import unittest
import datetime
from ast import Delete

import numpy as np
import pandas as pd
from datetime import timedelta, date
from faker import Faker
from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.modelo import automovil
from src.modelo.accion import Accion
from src.modelo.automovil import Automovil
from src.modelo.declarative_base import Base, Session, engine, sessionmaker
from src.modelo.mantenimiento import Mantenimiento


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
        start_date = datetime.date(2022,1,1)
        end_date = datetime.date(2022,1,31)
        for j in range(0, 10):
           
            mantenimiento = self.data_factory.random_int(1, 10)
            kilometraje = kilometraje_anterior + \
                self.data_factory.random_int(0, 10000)
            fecha = self.data_factory.date_between_dates(start_date, end_date)
            costo = self.data_factory.random_int(0, 50000)
            self.session.add(Accion(mantenimiento=mantenimiento, kilometraje=kilometraje,
                                    fecha=fecha, costo=costo, automovil=3))
            kilometraje_anterior = kilometraje
            start_date = start_date + timedelta(days=30)
            end_date = end_date + timedelta(days=30)
        self.session.commit()

        self.session.close()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los autos'''
        autos = self.session.query(Automovil).all()
        
        acciones = self.session.query(Accion).all()
            
        for accion in acciones:
            self.session.delete (accion)
        
        '''Borra todos los autos'''
        
        for auto in autos:
            self.session.delete(auto)
                          
        mantenimientos = self.session.query(Mantenimiento).all()
        for mantenimiento in mantenimientos:
            self.session.delete(mantenimiento)
        
        
        self.session.commit()
        self.session.close()
        

    def test_validar_reporte_gastos(self):
        """
        print("probando el reporte de gastos: ")
        lista_gastos=[]
        acciones=  [elem.__dict__ for elem in self.session.query(
            Accion).filter().group_by(Accion.mantenimiento)]
       
        promedio_anio =[]
        accion_mantenimiento = []
        promedio_accion_array = []
        for accion in acciones:
           accion_mantenimientos = [elem.__dict__ for elem in self.session.query (Accion).
             filter(Accion.mantenimiento ==accion["mantenimiento"] ).order_by(Accion.fecha.desc(), Accion.kilometraje.desc()).all()]
            for i, accion_mantenimiento in accion_mantenimientos:
                    accion_mantenimiento['costo']/accion_mantenimiento['kilometraje']- accion_mantenimiento[i+1]
                
        """               
        lista_gastos, valor_kilometro  = self.logica.dar_reporte_ganancias(2)
        self.assertGreater(valor_kilometro,0)
        self.assertGreater(len (lista_gastos),0)
        
        
        
