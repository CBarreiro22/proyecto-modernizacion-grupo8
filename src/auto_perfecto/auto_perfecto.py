'''
Esta clase es tan sólo un mock con datos para probar la interfaz
'''
from datetime import datetime

from sqlalchemy import desc

from src.modelo.automovil import Automovil
from src.modelo.mantenimiento import Mantenimiento
from src.modelo.accion import Accion
from src.modelo.declarative_base import session, engine, Base
import pandas as pd


class auto_perfecto():

    def __init__(self):
        # Este constructor contiene los datos falsos para probar la interfaz
        self.autos = []
        self.mantenimientos = []
        self.acciones = []
        self.gastos = []
        Base.metadata.create_all(engine)

    def dar_autos(self):
        autos = [elem.__dict__ for elem in session.query(Automovil).filter().order_by(Automovil.placa.desc())]
        return autos

    def dar_auto(self, id_auto):
        autos = self.dar_autos()
        return autos[id_auto]

    def crear_auto(self, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
        if self.validar_crear_auto(marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
            session.add(Automovil(marca=marca, placa=placa, modelo=modelo, kilometraje=kilometraje, color=color,
                                  cilindraje=cilindraje, combustible=tipo_combustible))
            session.commit()

    def editar_auto(self, id, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
        self.autos[id]['Marca'] = marca
        self.autos[id]['Placa'] = placa
        self.autos[id]['Modelo'] = modelo
        self.autos[id]['Kilometraje'] = float(kilometraje)
        self.autos[id]['Color'] = color
        self.autos[id]['Cilindraje'] = cilindraje
        self.autos[id]['TipoCombustible'] = tipo_combustible

    def vender_auto(self, id, kilometraje_venta, valor_venta):
        auto = self.dar_auto(id)
        autoId = auto["id"]
        automovil = session.query(Automovil).filter(Automovil.id == autoId).first()
        automovil.valorVenta = valor_venta
        automovil.kilometrajeVenta = kilometraje_venta
        automovil.vendido = True
        session.commit()

    def eliminar_auto(self, id):
        autos = self.dar_autos()
        autoId = autos[id]["id"]
        acciones = session.query (Accion).filter (Accion.automovil==autoId).all()
        if (len (acciones) == 0 ):
            auto = session.query (Automovil).filter (Automovil.id == autoId).first()
            session.delete(auto)
            session.commit()
        return self.dar_autos()

    def validar_crear_editar_auto(self, id, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
        return self.validar_crear_auto(marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible)

    def validar_crear_auto(self, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
        if not marca or not placa or not modelo or not kilometraje or not color or not cilindraje or not tipo_combustible:
            return False
        elif self.valida_tipo_datos_auto(modelo, kilometraje, cilindraje) == False:
            return False
        elif int(modelo) < 1886:

            return False
        elif int(kilometraje) < 0 or int(kilometraje) > 999999999:
            return False
        elif int(cilindraje) < 0 or int(cilindraje) > 999999999:
            return False
        elif len(marca) <= 6 or len(marca) >= 10:
            return False
        elif len(placa) <= 3 or len(placa) >= 255:
            return False
        elif len(color) <= 3 or len(color) >= 255:
            return False
        elif len(tipo_combustible) <= 3 or len(tipo_combustible) >= 255:
            return False
        elif self.validar_marca_repetida(marca):
            return False
        elif self.validar_placa_repetida(placa):
            return False
        return True

    def validar_marca_repetida(self, marca):
        automovil = session.query(Automovil).filter(Automovil.marca == marca).first()
        if automovil is not None:
            return True
        return False
    def validar_placa_repetida(self, placa):
        automovil = session.query(Automovil).filter(Automovil.placa == placa).first()
        if automovil is not None:
            return True
        return False

    def valida_tipo_datos_auto(self, modelo, kilometraje, cilindraje):
        try:
            return type(int(modelo)) is int and type(int(kilometraje)) is int and type(int(cilindraje)) is int
        except:
            return False

    def validar_vender_auto(self, id, valor_venta, kilometraje_venta):
        validacion = False
        try:
            verifivcacion1 = 0 <= int(kilometraje_venta) <= 999999999
            verifivcacion2 = 0.0 <= float(valor_venta) <= 999999999.0
            if verifivcacion1 and verifivcacion2:
                validacion = True
        except ValueError:
            validacion = False

        return validacion

    def dar_mantenimientos(self):

        return [elem.__dict__ for elem in session.query(Mantenimiento).all()]

    def aniadir_mantenimiento(self, nombre, descripcion):
        if not descripcion or not nombre:
            return False
        busqueda = session.query(Mantenimiento).filter(
            Mantenimiento.nombre == nombre).all()
        if len(busqueda) == 0:
            mantenimiento = Mantenimiento(
                nombre=nombre, descripcion=descripcion)
            session.add(mantenimiento)
            session.commit()
            return True
        else:
            return False

    def editar_mantenimiento(self, id, nombre, descripcion):
        self.mantenimientos[id]['Nombre'] = nombre
        self.mantenimientos[id]['Descripcion'] = descripcion

    def eliminar_mantenimiento(self, id):
        del self.mantenimientos[id]

    def validar_crear_editar_mantenimiento(self, nombre, descripcion):
        validacion = False
        if nombre != '' and descripcion != '':
            if len(descripcion) <= 30 and len(nombre) <= 20:
                validacion = True
        return validacion

    def dar_acciones_auto(self, id_auto):
        autos = self.dar_autos()
        autoId = autos[id_auto]["id"]
        acciones = [elem.__dict__ for elem in session.query(Accion).filter(Accion.automovil == autoId).all()]
        for index in range(len(acciones)):
            accion = acciones[index]
            mantenimientoId = int(accion["mantenimiento"])
            mantenimiento = session.query(Mantenimiento).filter(Mantenimiento.id == mantenimientoId).first()
            acciones[index]["mantenimiento"] = mantenimiento.nombre
            acciones[index]["fecha"] = str(accion["fecha"])[0:10]
        return acciones

    def dar_accion(self, id_auto, id_accion):
        return self.dar_acciones_auto(id_auto)[id_accion].copy()

    def crear_accion(self, mantenimiento, id_auto, valor, kilometraje, fecha):
        autos = self.dar_autos()
        auto = autos[id_auto]
        idAuto = auto["id"]

        if (0 < kilometraje <= 99999999) and (0 < valor <= 999999999):
            accion = Accion(automovil=idAuto, mantenimiento=mantenimiento, costo=valor, kilometraje=kilometraje,
                            fecha=datetime.strptime(fecha, "%Y-%m-%d"))
            session.add(accion)
            session.commit()
            return True
        return False

    def editar_accion(self, id_accion, mantenimiento, id_auto, valor, kilometraje, fecha):
        self.acciones[id_accion]['Mantenimiento'] = mantenimiento
        self.acciones[id_accion]['Auto'] = self.autos[id_auto]['Marca']
        self.acciones[id_accion]['Valor'] = valor
        self.acciones[id_accion]['Kilometraje'] = kilometraje
        self.acciones[id_accion]['Fecha'] = fecha

    def eliminar_accion(self, id_auto, id_accion):
        marca_auto = self.autos[id_auto]['Marca']
        i = 0
        id = 0
        while i < len(self.acciones):
            if self.acciones[i]['Auto'] == marca_auto:
                if id == id_accion:
                    self.acciones.pop(i)
                    return True
                else:
                    id += 1
            i += 1

        return False

        del self.accion[id_accion]

    def validar_crear_editar_accion(self, id_accion, mantenimiento, id_auto, valor, kilometraje, fecha):
        validacion = False
        try:
            float(kilometraje)
            float(valor)
            validacion = True
        except ValueError:
            validacion = False

        return validacion

    def dar_reporte_ganancias(self, id_auto):
        autos = self.dar_autos()
        auto = autos[id_auto]
        idAuto = auto["id"]
        df = pd.read_sql_query(
            sql=session.query(Accion.fecha, Accion.costo).
            filter(Accion.automovil == idAuto).statement, con=engine
        )
        df2 = df.groupby('fecha', as_index=False)['costo'].sum()
        total = 0.0
        resumenGastos = []
        for index, row in df2.iterrows():
            tupla = (str(row["fecha"])[0:4], row['costo'])
            resumenGastos.append(tupla)
            total += row['costo']
        resumenGastos.append(("total", total))
        if len(resumenGastos) > 0:
            acciones = session.query(Accion).order_by(desc(Accion.fecha)).all()
            promedio = 0.0
            for accion in acciones:
                promedio += accion.costo
            promedioCalculado = promedio / len(acciones)
            if len(acciones) > 1:
                valorAccionMantenimiento = acciones[0].costo / (acciones[0].kilometraje - acciones[1].kilometraje)
            else:
                automovil = self.dar_auto(idAuto)
                valorAccionMantenimiento = acciones[0].costo / (acciones[0].kilometraje - automovil.kilometraje)
            return resumenGastos, promedioCalculado * valorAccionMantenimiento
        return [('Total', 0)], 0
