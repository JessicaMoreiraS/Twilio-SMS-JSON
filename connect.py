from tinydb import TinyDB , Query
from model import usuario


db = TinyDB("Usuarios.json")
usuario=Query()

def inserir(model:usuario):
    db.insert({"nome":model.nome, "email":model.email, "telefone":model.telefone, "codigo":model.codigo, "validacao":model.validacao})
    
def update(model:usuario):
    if db.search(usuario.email==model.email):
        db.remove(usuario.email==model.email)
        db.insert({"nome":model.nome, "email":model.email, "telefone":model.telefone, "codigo":model.codigo, "validacao":model.validacao})

def deletar(model:usuario):
    if db.search(usuario.email==model.email):
        db.remove(usuario.email==model.email)
    