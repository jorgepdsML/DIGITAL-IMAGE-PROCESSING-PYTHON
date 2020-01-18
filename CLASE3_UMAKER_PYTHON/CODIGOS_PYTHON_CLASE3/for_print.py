from flask import Flask
#Flask(__name__,template_folder="your folder of html")
app=Flask(__name__)
@app.route('/')
def index():
    name="PAGINA WEB umaker usando funciónes y decoradores"
    return "HOLA MUNDO TAMBIEN SE PUEDE RETORNAR UN ARCHIVO HTML U OTRo MENSAJE"
app.run()