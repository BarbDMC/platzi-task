from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
#el prefijo de url indica que todas las rutas que inicien con /auth
#son dirigidas a este blueprint

from . import views