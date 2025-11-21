import pytest
import os

def test_files_exist():
    """Testa se arquivos principais existem"""
    assert os.path.exists('gerar_csvs.py')
    assert os.path.exists('README.md')

def test_python_syntax():
    """Testa sintaxe do arquivo principal"""
    with open('gerar_csvs.py', 'r') as f:
        code = f.read()
        compile(code, 'gerar_csvs.py', 'exec')

if __name__ == "__main__":
    test_files_exist()
    test_python_syntax()
    print("✅ Todos os testes passaram")
