
from sqlalchemy import text
from conexion import MyWeb , db





@MyWeb.route('/')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return 'Conexión exitosa a la base de datos!'
    except Exception as e:
        return f'Error de conexión: {str(e)}'



@MyWeb.route('/datos')
def ver_cursos():
    try:
        result = db.session.execute(text('SELECT * FROM estudiante'))
        cursos = result.fetchall()
        return str(cursos)  # Convierte los resultados a string para mostrarlos
    except Exception as e:
        return f'Error: {str(e)}'



if __name__ == '__main__':
    MyWeb.run(debug=True)
