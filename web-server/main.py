import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/') # decorator sintaxis | La ruta por donde llamar a este metodo
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Página de contacto</h1>
        <p>Esto es un párrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()