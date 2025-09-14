from flask import Flask, render_template, request, redirect, url_for, session
from model.personagem import Personagem
from model.raca import Raca
from model.classe import Classe
from model.atributos import Atributos

app = Flask(__name__)

app.secret_key = 'sua_chave_secreta_aqui' 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        session['nome'] = request.form['nome']
        session['idade'] = int(request.form['idade'])
        session['raca_nome'] = request.form['raca']
        session['classe_nome'] = request.form['classe']
        metodo = request.form['metodo_atributos']

        atr = Atributos()

        if metodo == 'classico':
            
            atributos_finais = atr.gerar_classico()
            session['atributos_finais'] = atributos_finais
            return redirect(url_for('resultado'))

        elif metodo == 'aventureiro':
            valores_rolados = atr.gerar_aventureiro()
            session['valores_para_distribuir'] = valores_rolados
            return redirect(url_for('distribuir'))
            
        elif metodo == 'heroico':
            valores_rolados = atr.gerar_heroico()
            session['valores_para_distribuir'] = valores_rolados
            return redirect(url_for('distribuir'))

    
    return render_template('index.html')

@app.route('/distribuir', methods=['GET', 'POST'])
def distribuir():
    if 'valores_para_distribuir' not in session:
        return redirect(url_for('index'))

    valores = session['valores_para_distribuir']
    nomes_atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

    if request.method == 'POST':
        atributos_finais = {}
        valores_escolhidos = []
        
        for nome in nomes_atributos:
            valor = int(request.form[nome])
            atributos_finais[nome] = valor
            valores_escolhidos.append(valor)
        
        # Validação: verifica se o usuário usou os valores corretos
        if sorted(valores) != sorted(valores_escolhidos):
            erro = "Valores inválidos ou repetidos foram escolhidos. Por favor, atribua cada valor rolado a um único atributo."
            return render_template('distribuir_atributos.html', valores=valores, atributos=nomes_atributos, erro=erro)

        session['atributos_finais'] = atributos_finais
        session.pop('valores_para_distribuir', None) # Limpa a session
        return redirect(url_for('resultado'))

    return render_template('distribuir_atributos.html', valores=valores, atributos=nomes_atributos)

@app.route('/resultado')
def resultado():
    if 'atributos_finais' not in session:
        return redirect(url_for('index'))

    
    p = Personagem()
    p.nome = session['nome']
    p.idade = session['idade']
    p.raca = Raca(session['raca_nome'])
    p.raca.definir_faixa_etaria(p.idade)
    p.classe = Classe(session['classe_nome'])
    p.atributos.valores = session['atributos_finais']

    
    session.clear()

    return render_template('resultado.html', personagem=p)

if __name__ == '__main__':
    app.run(debug=True)