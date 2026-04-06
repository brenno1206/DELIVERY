from flask import Blueprint, current_app, render_template, flash, redirect, url_for, request
from delivery.forms.main import ContatoForm

bp_main  = Blueprint('main', __name__)

@bp_main.route("/")
@bp_main.route("/index")
def index():
    user = {'username':'brenno'}
    current_app.logger.info("O endpint 'index' foi acessado")
    return render_template('main/index.html', user=user, promocao='Segunda é dia de pizza em dobro')

@bp_main.route("/carrinho")
def carrinho():
    carrinho = {
        'itens': [
            {'id': 1, 'name': 'Pizza Calabresa', 'preco': 39.99, 'quantidade': 2},
            {'id': 2, 'name': 'Borda Recheada', 'preco': 5.932, 'quantidade': 2},
            {'id': 3, 'name': 'Refrigerante 2L', 'preco': 10.4, 'quantidade': 1}
        ]
    }
    total = sum(item['preco'] * item['quantidade'] for item in carrinho['itens'])
    current_app.logger.info("O endpoint 'carrinho' foi acessado com sucesso")
    return render_template('main/carrinho.html', titulo="Meus Pedidos", carrinho=carrinho, total=total)

@bp_main.route('/contato', methods=['GET','POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        current_app.logger(f"Mensagem recebida de {form.nome.data}")
        flash('Mensagem enviada com sucesso"', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('main/contato.html')