class MinhaClasse:
    def __enter__(self):
        print("Entrei!")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Sair!")

with MinhaClasse() as mc:
    print("Estou aqui dentro!")