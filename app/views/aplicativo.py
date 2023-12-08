from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Servidor
from ..database import db

aplicativo_bp = Blueprint('aplicativo', __name__, template_folder='templates')

@aplicativo_bp.route('/')
def index():
    return render_template('index.html')