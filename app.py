from flask import Flask, render_template

app = Flask(__name__)

clientes = {
    'usuario1':{
        'nome': 'João Silva',
        'telefone': '(11) 1234-5678',
        'email': 'joao.silva@email.com'
    },
    'usuario2':{
        'nome': 'Maria Oliveira',
        'telefone': '(11) 9876-5432',
        'email': 'maria.oliveira@email.com'
    },
    'usuario3':{
        'nome': 'Carlos Pereira',
        'telefone': '(11) 1357-2468',
        'email': 'carlos.pereira@email.com'
    },
    'usuario4':{
        'nome': 'Ana Souza',
        'telefone': '(21) 2345-6789',
        'email': 'ana.souza@email.com'
    },
    'usuario5':{
        'nome': 'Pedro Alves',
        'telefone': '(21) 8765-4321',
        'email': 'pedro.alves@email.com'
    }
}

animais = {
    'animal01':{
    'nome_pet':'Rex',
    'tipo':'Cachorro',
    'raça':'Labrador', 
    'idade':'5', 
    'data de nasciemnto':'22/03/2019',
    'tutor':'João Silva',
    },
    'animal02':{
    'nome_pet':'Mimi',
    'tipo':'Gato',
    'raça':'Persa', 
    'idade':'2', 
    'data de nasciemnto':'15/07/2022',
    'tutor':'João Silva',
    },
    'animal03':{
    'nome_pet':'Bolota',
    'tipo':'Hamster',
    'raça':'Sírio', 
    'idade':'1', 
    'data de nasciemnto':'05/01/2023',
    'tutor':'Maria Oliveira',
    },
    'animal04':{
    'nome_pet':'Buddy',
    'tipo':'Cachorro',
    'raça':'Golden', 
    'idade':'3', 
    'data de nasciemnto':'10/10/2021',
    'tutor':'Carlos Pereira',
    },
    'animal05':{
    'nome_pet':'Luna',
    'tipo':'Gato',
    'raça':'Siamês', 
    'idade':'4', 
    'data de nasciemnto':'05/08/2020',
    'tutor':'Carlos Pereira'
    },
    'animal06':{
    'nome_pet':'Pingo',
    'tipo':'Pássaro',
    'raça':'Canário', 
    'idade':'1', 
    'data de nasciemnto':'02/14/2023',
    'tutor':'Ana Souza',
    },
    'animal07':{
    'nome_pet':'Thor',
    'tipo':'Cachorro',
    'raça':'Bulldog', 
    'idade':'6', 
    'data de nasciemnto':'11/25/2018',
    'tutor':'Pedro Alves',
    },
    'animal08':{
    'nome_pet':'Bela',
    'tipo':'Cachorro',
    'raça':'Poodle', 
    'idade':'4', 
    'data de nasciemnto':'09/30/2020',
    'tutor':'Pedro Alves',
    },
    'animal09':{
    'nome_pet':'Nina',
    'tipo':'Gato',
    'raça':'Maine Coon', 
    'idade':'3', 
    'data de nasciemnto':'06/17/2021',
    'tutor':'Pedro Alves',
    },
    'animal10':{
    'nome_pet':'Spike',
    'tipo':'Cachorro',
    'raça':'Beagle', 
    'idade':'7', 
    'data de nasciemnto':'12/01/2017',
    'tutor':'Pedro Alves',
    },
}

atendentes = {
1:{
    'nome':'Lucas Almeida',
    'telefone':'(11) 9988-7766',
    'email':'lucas.almeida@petshop.com',
    'turno':'Manhã',
},
2:{
    'nome':'Camila Santos',
    'telefone':'(11) 9977-6655',
    'email':'camila.santos@petshop.com',
    'turno':'Tarde',
},
3:{
    'nome':'Roberto Lima',
    'telefone':'(11) 9966-5544',
    'email':'roberto.lima@petshop.com',
    'turno':'Noite',
}
}



@app.route('/')
def home():
    return 'Bem-vindo ao Petshop!'

@app.route('/clientes')
def get_clientes():
    return clientes

@app.route('/animais')
def get_animais():
    return animais

@app.route('/atendentes')
def get_atendentes():
    return atendentes

@app.route('/clientes/<cliente>')
def get_cliente(cliente):
    return clientes[cliente]

@app.route('/animais/<animal>')
def get_animal(animal):
    return animais[animal]

@app.route('/atendentes/<atendente>')
def get_atendente(atendente):
    atendente = int(atendente)
    #print(atendente, type(atendente))
    return atendentes[atendente]

if __name__ == '__main__':
    app.run(debug=True)