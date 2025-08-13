
#Exemplo Simplificado de POO

# Classes: Pessoa, morador, visitante e portaria.


from datetime import datetime

class Pessoa:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return f"{self.nome} ({self.documento})"

class Morador(Pessoa):
    def __init__(self, nome, documento, apartamento):
        super().__init__(nome, documento)
        self.apartamento = apartamento

class Visitante(Pessoa):
    def __init__(self, nome, documento, motivo_visita):
        super().__init__(nome, documento)
        self.motivo_visita = motivo_visita

class Portaria:
    def __init__(self):
        self.__lista_autorizada = []  # lista de pessoas que pódem ser autorizadas
        self.__historico = []         # histórico de entradas/saídas

    def autorizar_entrada(self, pessoa):
        self.__lista_autorizada.append(pessoa)

    def verificar_autorizacao(self, documento):
        for p in self.__lista_autorizada:
            if p.documento == documento:
                return p
        return None

    def registrar_entrada(self, documento):
        pessoa = self.verificar_autorizacao(documento)
        if pessoa:
            self.__historico.append((pessoa, "Entrada", datetime.now()))
            print(f"[ACESSO PERMITIDO] Bem-vindo(a) {pessoa.nome}")
        else:
            print("[ACESSO NEGADO] Documento não autorizado.")

    def registrar_saida(self, documento):
        pessoa = self.verificar_autorizacao(documento)
        if pessoa:
            self.__historico.append((pessoa, "Saída", datetime.now()))
            print(f"[SAÍDA REGISTRADA] Até logo, {pessoa.nome}")
        else:
            print("[ERRO] Documento não encontrado.")

    def historico(self):
        return self.__historico





# Criando pessoas
m1 = Morador("Elias Dutra", "123456", "101")
v1 = Visitante("João Silva", "654321", "Visitar Elias Dutra")
v2 = Visitante("Joel Ribeiro","856984", "salão de festas")


# Criando portaria
portaria = Portaria()

# Autorizando entrada
portaria.autorizar_entrada(m1)
portaria.autorizar_entrada(v1)
portaria.autorizar_entrada(v2)

# Tentativas de entrada
portaria.registrar_entrada("123456")  # Morador autorizado
portaria.registrar_entrada("654321")  # Visitante autorizado
portaria.registrar_entrada("856984")  # Visitante autorizado
portaria.registrar_entrada("999999")  # Documento não autorizado

# Registrando saída
portaria.registrar_saida("654321")

# Exibindo histórico
print("\nHistórico de acessos:")
for pessoa, tipo, horario in portaria.historico():
    print(f"{tipo} - {pessoa} às {horario}")
