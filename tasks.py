from invoke import task
from datetime import datetime
import os
import zipfile
import shutil

def load_env(env: str):
    """
    Carrega o arquivo .env correspondente ao ambiente.
    Ex: dev, test, prod
    """
    env_file = f".env.{env}"

    if os.path.exists(env_file):
        load_dotenv(env_file, override=True)
        print(f"[ENV] Carregado: {env_file}")
    else:
        raise FileNotFoundError(f"{env_file} nao encontrado")

@task
def install(c, dev=True):
    """
    Instala o projeto.
    """
    if dev:
        c.run('pip install -e ".[dev,test]"', echo=True)
    else:
        c.run("pip install .", echo=True)


@task
def uninstall(c):
    """
    Remove o pacote instalado.
    """
    c.run("pip uninstall -y delivery", echo=True)


@task
def run(c):
    """
    Executa a aplicacao Flask.
    """
    c.run("flask run")
    

@task
def prod(c):
    """
    Executa a aplicacao em modo producao.
    """
    load_env("prod")
    c.run("flask run")


@task
def test(c):
    """
    Executa os testes automatizados.
    """
    load_env("test")
    c.run("pytest -v", env={"PYTHONPATH": "."})


@task
def lint(c):
    """
    Verifica qualidade de codigo.
    """
    c.run("flake8")


@task
def format(c):
    """
    Formata o codigo automaticamente.
    """
    c.run("black .", pty=True)

@task
def clean(c):
    """
    Exclui arquivos e pastas indesejadas a partir do diretório atual.
    """
    excludes = [
        "venv",
        "__pycache__",
        ".git",
        ".vscode",
        "delivery.egg-info"
    ]

    print("→ Iniciando a exclusão dos arquivos e pastas...")

    for root, dirs, files in os.walk(".", topdown=True):
        
        for d in list(dirs): 
            if d in excludes:
                dir_path = os.path.join(root, d)
                print(f"  Removendo pasta: {dir_path}")
                shutil.rmtree(dir_path, ignore_errors=True)
                dirs.remove(d) 

        for file in files:
            if file.endswith((".pyc", ".pyo", ".pyd", ".log", ".db", ".sqlite3")):
                filepath = os.path.join(root, file)
                print(f"  Removendo arquivo: {filepath}")
                try:
                    os.remove(filepath)
                except OSError:
                    pass

    print("→ Limpeza concluída com sucesso!")

@task
def zip_windows(c, name=None):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    zip_filename = name or f"delivery-projeto-{timestamp}.zip"
    zip_path = os.path.abspath(os.path.join("..", zip_filename))

    print(f"→ Criando ZIP: {zip_path}")

    excludes = [
        "venv",
        "__pycache__",
        ".git",
        ".vscode",
        "delivery.egg-info"
    ]

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("."):

            dirs[:] = [d for d in dirs if d not in excludes]

            for file in files:
                if file.endswith((".pyc", ".pyo", ".pyd", ".log", ".db", ".sqlite3")):
                    continue

                filepath = os.path.join(root, file)
                zipf.write(filepath)

    if os.path.exists(zip_path):
        size_mb = os.path.getsize(zip_path) / (1024 * 1024)
        print(f"→ ZIP criado com sucesso: {zip_path}")
        print(f"   Tamanho: {size_mb:.2f} MB")
