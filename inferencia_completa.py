class Predicado:
    def __init__(self, nome, *args):
        self.nome = nome
        self.args = args

    def __repr__(self):
        return f"{self.nome}({', '.join(map(str, self.args))})"

    def __eq__(self, other):
        return isinstance(other, Predicado) and self.nome == other.nome and self.args == other.args

    def __hash__(self):
        return hash((self.nome, self.args))


class Regra:
    def __init__(self, antecedente, consequente, peso):
        self.antecedente = antecedente  # Lista de predicados
        self.consequente = consequente  # Predicado resultante
        self.peso = peso  # Peso da regra (certeza)

    def __repr__(self):
        return f"{self.antecedente} -> {self.consequente} (Peso: {self.peso})"


# Lista de predicados de sintomas
febre = Predicado("febre", "Paciente")
tosse = Predicado("tosse", "Paciente")
dor_de_garganta = Predicado("dor_de_garganta", "Paciente")
dor_no_corpo = Predicado("dor_no_corpo", "Paciente")
fadiga = Predicado("fadiga", "Paciente")
dificuldade_respiratoria = Predicado("dificuldade_respiratoria", "Paciente")
coriza = Predicado("coriza", "Paciente")
espirros = Predicado("espirros", "Paciente")
dor_de_cabeca = Predicado("dor_de_cabeca", "Paciente")
nausea = Predicado("nausea", "Paciente")
vomito = Predicado("vomito", "Paciente")
diarreia = Predicado("diarreia", "Paciente")
perda_de_olfato = Predicado("perda_de_olfato", "Paciente")
perda_de_paladar = Predicado("perda_de_paladar", "Paciente")
fadiga_extrema = Predicado("fadiga_extrema", "Paciente")
dores_abdominais = Predicado("dores_abdominais", "Paciente")
tosse_seca = Predicado("tosse_seca", "Paciente")
calafrios = Predicado("calafrios", "Paciente")
confusao_mental = Predicado("confusao_mental", "Paciente")
sudorese = Predicado("sudorese", "Paciente")
dor_nas_articulacoes = Predicado("dor_nas_articulacoes", "Paciente")
erupcao_cutanea = Predicado("erupcao_cutanea", "Paciente")
inapetencia = Predicado("inapetencia", "Paciente")
confusao_mental = Predicado("confusao_mental", "Paciente")
desidratacao = Predicado("desidratacao", "Paciente")
ictericia = Predicado("ictericia", "Paciente")
olhos_vermelhos = Predicado("olhos_vermelhos", "Paciente")
fraqueza = Predicado("fraqueza", "Paciente")
hipertemia = Predicado("hipertemia", "Paciente")
arritmia = Predicado("arritmia", "Paciente")
rigidez_no_pescoco = Predicado("rigidez_no_pescoco","Paciente")
hemorragia = Predicado("hemorragia","Paciente")
rouquidao = Predicado("rouquidao","Paciente")
chiado_no_peito = Predicado("chiado_no_peito","Paciente")


# Lista de predicados de diagnósticos
gripe = Predicado("doenca", "Paciente", "Gripe")
resfriado = Predicado("doenca", "Paciente", "Resfriado")
covid19 = Predicado("doenca", "Paciente", "COVID-19")
mononucleose = Predicado("doenca", "Paciente", "Mononucleose")
dengue = Predicado("doenca", "Paciente", "Dengue")
zika = Predicado("doenca", "Paciente", "Zika")
influenza = Predicado("doenca", "Paciente", "Influenza")
hepatite = Predicado("doenca", "Paciente", "Hepatite")
sarampo = Predicado("doenca", "Paciente", "Sarampo")
rubeola = Predicado("doenca", "Paciente", "Rubéola")
gastrite = Predicado("doenca", "Paciente", "Gastrite")
amigdalite = Predicado("doenca", "Paciente", "Amigdalite")
sinusite = Predicado("doenca", "Paciente", "Sinusite")
bronquite = Predicado("doenca", "Paciente", "Bronquite")
pneumonia = Predicado("doenca", "Paciente", "Pneumonia")
meningite = Predicado("doenca", "Paciente", "Meningite")
tuberculose = Predicado("doenca", "Paciente", "Tuberculose")
leptospirose = Predicado("doenca", "Paciente", "Leptospirose")
malaria = Predicado("doenca", "Paciente", "Malária")
hepatite_a = Predicado("doenca", "Paciente", "Hepatite A")
hepatite_b = Predicado("doenca", "Paciente", "Hepatite B")
hepatite_c = Predicado("doenca", "Paciente", "Hepatite C")
chikungunya = Predicado("doenca", "Paciente", "Chikungunya")
tifoide = Predicado("doenca", "Paciente", "Febre Tifoide")
ebola = Predicado("doenca", "Paciente", "Ebola")
sarampo_complicado = Predicado("doenca", "Paciente", "Sarampo Complicado")
encefalite = Predicado("doenca", "Paciente", "Encefalite")
laringite = Predicado("doenca", "Paciente", "Laringite")
fibrose_cistica = Predicado("doenca", "Paciente", "Fibrose Cística")
bronquiolite = Predicado("doenca", "Paciente", "Bronquiolite")


# Definindo 50 regras com sintomas, diagnósticos e pesos
regras = [
    Regra([febre, tosse, dor_de_garganta, dor_no_corpo], gripe, 0.8),
    Regra([tosse, dor_de_garganta], resfriado, 0.5),
    Regra([febre, tosse, fadiga, dificuldade_respiratoria], covid19, 0.9),
    Regra([fadiga, dor_de_garganta, febre], mononucleose, 0.7),
    Regra([febre, dor_no_corpo, dor_de_cabeca], dengue, 0.85),
    Regra([febre, dor_de_cabeca, dores_abdominais], zika, 0.7),
    Regra([febre, tosse, coriza, espirros], influenza, 0.75),
    Regra([dor_de_cabeca, fadiga, dores_abdominais], hepatite, 0.6),
    Regra([febre, dor_de_cabeca, tosse], sarampo, 0.65),
    Regra([febre, dor_de_garganta, espirros], rubeola, 0.55),
    Regra([nausea, vomito, dores_abdominais], gastrite, 0.7),
    Regra([dor_de_garganta, febre, sudorese], amigdalite, 0.6),
    Regra([dor_de_garganta, coriza, dor_de_cabeca], sinusite, 0.5),
    Regra([tosse, dificuldade_respiratoria, febre], bronquite, 0.65),
    Regra([tosse_seca, dificuldade_respiratoria, febre], pneumonia, 0.9),
    Regra([fadiga, calafrios, sudorese], gripe, 0.8),
    Regra([dor_de_cabeca, coriza, tosse], resfriado, 0.5),
    Regra([febre, calafrios, dor_no_corpo], covid19, 0.85),
    Regra([fadiga_extrema, dor_de_garganta, febre], mononucleose, 0.75),
    Regra([calafrios, sudorese, febre], dengue, 0.8),
    Regra([febre, espirros, dor_no_corpo], zika, 0.6),
    Regra([febre, espirros, fadiga], influenza, 0.65),
    Regra([vomito, dor_no_corpo, dores_abdominais], hepatite, 0.7),
    Regra([dor_no_corpo, dor_de_cabeca, espirros], sarampo, 0.6),
    Regra([febre, fadiga, calafrios], rubeola, 0.5),
    Regra([nausea, dor_no_corpo, febre], gastrite, 0.7),
    Regra([dor_de_garganta, fadiga, coriza], amigdalite, 0.55),
    Regra([dor_de_garganta, fadiga, tosse], sinusite, 0.6),
    Regra([tosse, fadiga, calafrios], bronquite, 0.65),
    Regra([febre, fadiga, dificuldade_respiratoria], pneumonia, 0.85),
    Regra([febre, dor_de_cabeca, calafrios], gripe, 0.75),
    Regra([tosse, coriza, espirros], resfriado, 0.5),
    Regra([fadiga, dificuldade_respiratoria, tosse_seca], covid19, 0.9),
    Regra([febre, dor_de_cabeca, calafrios], mononucleose, 0.7),
    Regra([dor_no_corpo, febre, sudorese], dengue, 0.85),
    Regra([fadiga, dores_abdominais, febre], zika, 0.7),
    Regra([tosse, espirros, fadiga], influenza, 0.65),
    Regra([nausea, dor_de_cabeca, febre], hepatite, 0.75),
    Regra([dor_de_cabeca, tosse, febre], sarampo, 0.6),
    Regra([dor_de_garganta, febre, espirros], rubeola, 0.5),
    Regra([nausea, vomito, dor_de_garganta], gastrite, 0.7),
    Regra([dor_de_garganta, coriza, sudorese], amigdalite, 0.55),
    Regra([dor_de_garganta, tosse, calafrios], sinusite, 0.6),
    Regra([tosse_seca, dificuldade_respiratoria, febre], bronquite, 0.75),
    Regra([febre, fadiga_extrema, calafrios], pneumonia, 0.85),
    Regra([calafrios, sudorese, dor_no_corpo], gripe, 0.8),
    Regra([coriza, espirros, dor_de_garganta], resfriado, 0.5),
    Regra([febre, fadiga, perda_de_olfato, perda_de_paladar], covid19, 0.95),
    Regra([fadiga, dor_de_garganta, calafrios], mononucleose, 0.75),
    Regra([febre, dor_no_corpo, dor_de_cabeca], dengue, 0.8),
    Regra([febre, dor_de_cabeca, rigidez_no_pescoco], meningite, 0.9),
    Regra([tosse, dificuldade_respiratoria, febre], tuberculose, 0.85),
    Regra([febre, dor_no_corpo, olhos_vermelhos, erupcao_cutanea], leptospirose, 0.75),
    Regra([febre, sudorese, dor_nas_articulacoes, fadiga], malaria, 0.8),
    Regra([ictericia, dor_no_corpo, dores_abdominais], hepatite_a, 0.7),
    Regra([febre, dores_abdominais, ictericia], hepatite_b, 0.75),
    Regra([febre, dor_no_corpo, ictericia, desidratacao], hepatite_c, 0.7),
    Regra([febre, dor_nas_articulacoes, erupcao_cutanea], chikungunya, 0.8),
    Regra([febre, desidratacao, dores_abdominais], tifoide, 0.85),
    Regra([febre, dor_no_corpo, hemorragia], ebola, 0.95),
    Regra([febre, erupcao_cutanea, tosse, dificuldade_respiratoria], sarampo_complicado, 0.9),
    Regra([confusao_mental, febre, dor_de_cabeca], encefalite, 0.85),
    Regra([febre, tosse_seca, rouquidao], laringite, 0.65),
    Regra([tosse_seca, dificuldade_respiratoria, fadiga], fibrose_cistica, 0.8),
    Regra([tosse, dificuldade_respiratoria, febre, chiado_no_peito], bronquiolite, 0.75),
    Regra([febre, dor_de_garganta, erupcao_cutanea], rubeola, 0.7),
    Regra([fadiga, dor_de_cabeca, febre, inapetencia], mononucleose, 0.65),
    Regra([febre, espirros, dor_nas_articulacoes], zika, 0.7),
    Regra([calafrios, dor_no_corpo, sudorese, febre], malaria, 0.85),
    Regra([tosse, coriza, espirros, febre], influenza, 0.7),
    Regra([dor_de_cabeca, tosse, dificuldade_respiratoria], pneumonia, 0.85),
    Regra([febre, fadiga, inapetencia], hepatite, 0.6),
    Regra([fadiga, dor_nas_articulacoes, erupcao_cutanea], chikungunya, 0.75),
    Regra([febre, tosse, calafrios, sudorese], gripe, 0.8),
    Regra([febre, coriza, dor_de_garganta], resfriado, 0.5),
    Regra([fadiga, dificuldade_respiratoria, perda_de_olfato], covid19, 0.9),
    Regra([dor_nas_articulacoes, febre, erupcao_cutanea], dengue, 0.8),
    Regra([febre, dores_abdominais, inapetencia], hepatite_a, 0.7),
    Regra([febre, dor_de_cabeca, ictericia], hepatite_b, 0.75),
    Regra([dor_no_corpo, febre, erupcao_cutanea], zika, 0.65),
    Regra([febre, dor_no_corpo, olhos_vermelhos], leptospirose, 0.8),
    Regra([sudorese, dificuldade_respiratoria, arritmia], pneumonia, 0.85),
    Regra([confusao_mental, febre, sudorese], encefalite, 0.8),
    Regra([febre, dor_nas_articulacoes, inapetencia], tifoide, 0.7),
    Regra([febre, fadiga_extrema, dor_nas_articulacoes], fibrose_cistica, 0.65),
    Regra([febre, dificuldade_respiratoria, erupcao_cutanea], bronquiolite, 0.7),
    Regra([dor_no_corpo, calafrios, febre], ebola, 0.9),
    Regra([febre, dor_no_corpo, sudorese], malaria, 0.75),
    Regra([tosse, fadiga, dor_no_corpo], influenza, 0.65),
    Regra([febre, tosse, confusao_mental], meningite, 0.85),
    Regra([febre, dificuldade_respiratoria, tosse_seca], tuberculose, 0.9),
    Regra([febre, dor_no_corpo, fadiga_extrema], sarampo_complicado, 0.85),
    Regra([febre, espirros, coriza, erupcao_cutanea], rubeola, 0.6),
    Regra([febre, fadiga, dificuldade_respiratoria], covid19, 0.9),
    Regra([dor_no_corpo, erupcao_cutanea, febre], chikungunya, 0.7),
    Regra([calafrios, febre, dores_abdominais], tifoide, 0.8)
]


class MotorDeInferencia:
    def __init__(self, regras):
        self.regras = regras
        self.fatos = set()
        self.certeza = {}  # Dicionário para armazenar certeza dos diagnósticos
        self.probabilidade = {}  # Dicionário para armazenar probabilidade acumulada

    def adicionar_fato(self, fato):
        self.fatos.add(fato)
        self.inferir()

    def inferir(self):
        for regra in self.regras:
            match_count = sum(1 for antecedente in regra.antecedente if antecedente in self.fatos)
            total_antecedentes = len(regra.antecedente)
            if match_count > 0:  # Se pelo menos um antecedente corresponde
                fracao_certeza = regra.peso * (match_count / total_antecedentes)
                fracao_probabilidade = 1 - (1 - regra.peso) ** (match_count / total_antecedentes)
                self.atualizar_certeza(regra.consequente, fracao_certeza)
                self.atualizar_probabilidade(regra.consequente, fracao_probabilidade)
                print(f"Fato parcial inferido: {regra.consequente} com certeza {self.certeza[regra.consequente]:.2f} e probabilidade {self.probabilidade[regra.consequente]:.2f}")

    def atualizar_certeza(self, diagnostico, fracao_certeza):
        if diagnostico not in self.certeza:
            self.certeza[diagnostico] = fracao_certeza
        else:
            self.certeza[diagnostico] += fracao_certeza

    def atualizar_probabilidade(self, diagnostico, fracao_probabilidade):
        if diagnostico not in self.probabilidade:
            self.probabilidade[diagnostico] = fracao_probabilidade
        else:
            # Combina a nova fração com a probabilidade existente usando a regra de Bayes simplificada
            self.probabilidade[diagnostico] = 1 - (1 - self.probabilidade[diagnostico]) * (1 - fracao_probabilidade)

    def mostrar_fatos(self):
        for fato in self.fatos:
            print(f"Fato: {fato}")
        print("\nCerteza e Probabilidade dos diagnósticos:")
        for diag, certeza in self.certeza.items():
            prob = self.probabilidade.get(diag, 0)
            print(f"{diag}: Certeza = {certeza:.2f}, Probabilidade = {prob:.2f}")


# def ler_dados_arquivo(caminho_arquivo):
#     sintomas = {}
#     diagnosticos = {}
#     regras = []

#     with open(caminho_arquivo, 'r') as file:
#         secao_atual = None
        
#         for linha in file:
#             linha = linha.strip()

#             # Detecta a seção atual
#             if linha.startswith("# Sintomas"):
#                 secao_atual = "sintomas"
#             elif linha.startswith("# Diagnósticos"):
#                 secao_atual = "diagnosticos"
#             elif linha.startswith("# Regras"):
#                 secao_atual = "regras"
#             elif linha and not linha.startswith("#"):
#                 if secao_atual == "sintomas":
#                     nome, definicao = linha.split(' = ')
#                     exec(f"{nome} = {definicao}", globals(), sintomas)
#                 elif secao_atual == "diagnosticos":
#                     nome, definicao = linha.split(' = ')
#                     exec(f"{nome} = {definicao}", globals(), diagnosticos)
#                 elif secao_atual == "regras":
#                     exec(f"regras.append({linha})", globals(), {"regras": regras, **sintomas, **diagnosticos})

#     return sintomas, diagnosticos, regras

# Exemplo de uso
# sintomas, diagnosticos, regras = ler_dados_arquivo("dados.txt")

# Testando o sistema
motor = MotorDeInferencia(regras)
motor.adicionar_fato(Predicado("febre", "Paciente"))
motor.adicionar_fato(Predicado("tosse", "Paciente"))
motor.adicionar_fato(Predicado("dificuldade_respiratoria", "Paciente"))
motor.adicionar_fato(Predicado("fadiga", "Paciente"))
motor.mostrar_fatos()