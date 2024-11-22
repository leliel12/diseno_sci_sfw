import bonobo
import requests

def extract_users():
    """Extrae usuarios de una API"""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    yield from response.json()

def transform_user(user):
    """Transforma los datos del usuario"""
    return {
        'name': user['name'].upper(),
        'email': user['email'].lower(),
        'company': user['company']['name']
    }

def load_user(user):
    """Carga (en este caso, imprime) el usuario"""
    print(f"Processed User: {user['name']}, {user['email']}, {user['company']}")

def get_graph():
    """Define el grafo de transformación"""
    graph = bonobo.Graph()
    graph.add_chain(
        extract_users,
        transform_user,
        load_user,
    )
    return graph

if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(get_graph(**options))
