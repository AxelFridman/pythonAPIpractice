from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

cursos = [10,20,30,40]
@app.route('/curso', methods=['GET'])
def get():
    return jsonify({'Cursos': cursos})

@app.route('/curso/<int:course_id>', methods=['GET'])
def get_curso(course_id):
    return jsonify({'Cursos': cursos[course_id]})

if __name__ == '__main__':
    app.run(debug=True)