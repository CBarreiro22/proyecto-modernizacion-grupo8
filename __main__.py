import sys
from PyQt5.QtWidgets import QApplication

from src.auto_perfecto.auto_perfecto import auto_perfecto
from src.vista.InterfazAutoPerfecto import App_AutoPerfecto
from src.auto_perfecto.Logica_mock import Logica_mock
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    # Crea la BD
    Base.metadata.create_all(engine)
    # Abre la sesión
    session = Session()

    # Punto inicial de la aplicación

    logica = Logica_mock()
    logica2 = auto_perfecto()

    app = App_AutoPerfecto(sys.argv, logica2)
    sys.exit(app.exec_())