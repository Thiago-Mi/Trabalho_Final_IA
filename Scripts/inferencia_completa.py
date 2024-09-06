import streamlit as st
import io
import pandas as pd

class Predicado:
    """
    Classe que representa um predicado, que pode ser um sintoma ou um diagnóstico.
    """
    def __init__(self, nome):
        """
        Inicializa um predicado com um nome.
        
        :param nome: Nome do predicado.
        """
        self.nome = nome

    def __repr__(self):
        """
        Retorna a representação em string do predicado.
        
        :return: Nome do predicado.
        """
        return f"{self.nome}"

    def __eq__(self, other):
        """
        Compara dois predicados para verificar igualdade com base no nome.
        
        :param other: Outro predicado a ser comparado.
        :return: True se os nomes forem iguais, False caso contrário.
        """
        return isinstance(other, Predicado) and self.nome == other.nome

    def __hash__(self):
        """
        Implementa um hash para uso em conjuntos (sets).
        
        :return: Hash do nome do predicado.
        """
        return hash((self.nome))


class Regra:
    """
    Classe que representa uma regra de inferência que relaciona sintomas a um diagnóstico.
    """
    def __init__(self, antecedente, consequente, peso):
        """
        Inicializa uma regra com antecedente, consequente e peso.
        
        :param antecedente: Lista de predicados representando os sintomas.
        :param consequente: Predicado resultante (diagnóstico).
        :param peso: Peso da regra, indicando o grau de certeza (entre 0 e 1).
        """
        self.antecedente = antecedente
        self.consequente = consequente
        self.peso = peso

    def __repr__(self):
        """
        Retorna uma representação textual da regra.
        
        :return: Representação textual da regra.
        """
        return f"{self.antecedente} -> {self.consequente} (Peso: {self.peso})"


def ler_predicados_de_arquivo(uploaded_file):
    """
    Lê predicados de sintomas de um arquivo.
    
    :param uploaded_file: Arquivo carregado contendo os predicados.
    :return: Lista de predicados.
    """
    predicados = []
    with io.StringIO(uploaded_file.getvalue().decode("utf-8")) as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            predicados.append(Predicado(nome))
    return predicados


def ler_predicados_de_diagnosticos_de_arquivo(uploaded_file):
    """
    Lê predicados de diagnósticos de um arquivo.
    
    :param uploaded_file: Arquivo carregado contendo os predicados.
    :return: Lista de predicados.
    """
    predicados = []
    with io.StringIO(uploaded_file.getvalue().decode("utf-8")) as arquivo:
        for linha in arquivo:
            valor = linha.strip()
            predicados.append(Predicado(valor.lower()))
    return predicados


def ler_definicao_de_regras(uploaded_file, predicados_sintomas, predicados_diagnosticos):
    """
    Lê a definição de regras de um arquivo.
    
    :param uploaded_file: Arquivo carregado contendo as regras.
    :param predicados_sintomas: Lista de predicados de sintomas.
    :param predicados_diagnosticos: Lista de predicados de diagnósticos.
    :return: Lista de regras.
    """
    regras = []
    predicados_dict = {p.nome: p for p in predicados_sintomas}
    predicados_dict.update({p.nome: p for p in predicados_diagnosticos})
    with io.StringIO(uploaded_file.getvalue().decode("utf-8")) as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(';')
            try:
                sintomas = [predicados_dict[sintoma.strip()] for sintoma in partes[0].split(',')]
                diagnostico = predicados_dict[partes[1].strip()]
                peso = float(partes[2])
                regras.append(Regra(sintomas, diagnostico, peso))
            except KeyError as e:
                print(f"Erro: Chave {e} não encontrada nos predicados.")
    return regras


class MotorDeInferencia:
    """
    Classe que representa o motor de inferência, responsável por gerenciar o processo de inferência baseado em regras.
    """
    def __init__(self, regras):
        """
        Inicializa o motor de inferência com um conjunto de regras.
        
        :param regras: Lista de objetos Regra que definem as relações entre sintomas e diagnósticos.
        """
        self.regras = regras
        self.fatos_por_paciente = {}  # Dicionário para armazenar fatos por paciente
        self.certeza_por_paciente = {}  # Dicionário para armazenar certeza dos diagnósticos por paciente
        self.probabilidade_por_paciente = {}  # Dicionário para armazenar probabilidade acumulada por paciente

    def adicionar_fato(self, paciente, fato):
        """
        Adiciona um novo fato (sintoma) para um paciente e inicia o processo de inferência.
        
        :param paciente: Nome do paciente.
        :param fato: Objeto Predicado representando o sintoma observado.
        """
        if paciente not in self.fatos_por_paciente:
            self.fatos_por_paciente[paciente] = set()
        self.fatos_por_paciente[paciente].add(fato)
        self.inferir(paciente)

    def inferir(self, paciente):
        """
        Avalia cada regra em relação aos fatos conhecidos do paciente e atualiza a certeza e probabilidade dos diagnósticos.
        
        :param paciente: Nome do paciente.
        """
        self.certeza_por_paciente[paciente] = {}
        self.probabilidade_por_paciente[paciente] = {}
        for regra in self.regras:
            match_count = sum(1 for antecedente in regra.antecedente if antecedente in self.fatos_por_paciente[paciente])
            total_antecedentes = len(regra.antecedente)
            if match_count > 0:  # Se pelo menos um antecedente corresponde
                fracao_certeza = regra.peso * (match_count / total_antecedentes)
                fracao_probabilidade = 1 - (1 - regra.peso) ** (match_count / total_antecedentes)
                self.atualizar_certeza(paciente, regra.consequente, fracao_certeza)
                self.atualizar_probabilidade(paciente, regra.consequente, fracao_probabilidade)

    def atualizar_certeza(self, paciente, diagnostico, fracao_certeza):
        """
        Atualiza a certeza acumulada de um diagnóstico para um paciente.
        
        :param paciente: Nome do paciente.
        :param diagnostico: Objeto Predicado representando o diagnóstico.
        :param fracao_certeza: Fração de certeza a ser adicionada.
        """
        if diagnostico not in self.certeza_por_paciente[paciente]:
            self.certeza_por_paciente[paciente][diagnostico] = fracao_certeza
        else:
            self.certeza_por_paciente[paciente][diagnostico] = (self.certeza_por_paciente[paciente][diagnostico] + fracao_certeza) / 2

    def atualizar_probabilidade(self, paciente, diagnostico, fracao_probabilidade):
        """
        Atualiza a probabilidade acumulada de um diagnóstico para um paciente usando a regra de Bayes simplificada.
        
        :param paciente: Nome do paciente.
        :param diagnostico: Objeto Predicado representando o diagnóstico.
        :param fracao_probabilidade: Fração de probabilidade a ser adicionada.
        """
        if diagnostico not in self.probabilidade_por_paciente[paciente]:
            self.probabilidade_por_paciente[paciente][diagnostico] = fracao_probabilidade
        else:
            # Aplicar a regra de Bayes simplificada
            self.probabilidade_por_paciente[paciente][diagnostico] = 1 - (1 - self.probabilidade_por_paciente[paciente][diagnostico]) * (1 - fracao_probabilidade)


    def mostrar_fatos(self):
        """
        Exibe os fatos conhecidos e as certezas e probabilidades dos diagnósticos.
        """
        for paciente, fatos in self.fatos_por_paciente.items():
            st.write(f"Paciente: {paciente}")
            st.write(f"    Fatos: {fatos}")
            st.write("\n  Certeza e Probabilidade dos diagnósticos:")

            # Criar uma lista de dicionários para armazenar os dados da tabela
            dados_tabela = []
            diagnosticos_ordenados = sorted(
                self.certeza_por_paciente[paciente].items(),
                key=lambda item: (self.probabilidade_por_paciente[paciente].get(item[0], 0), item[1]),
                reverse=True
            )
            for diag, certeza in diagnosticos_ordenados:
                prob = self.probabilidade_por_paciente[paciente].get(diag, 0)
                dados_tabela.append({
                    "Diagnóstico": diag.nome,
                    "Certeza": f"{certeza:.3f}",
                    "Probabilidade": f"{prob:.3f}"
                })

            # Criar um DataFrame a partir dos dados da tabela
            df = pd.DataFrame(dados_tabela)
            st.table(df)


def main():
    """
    Função principal que inicializa a interface do Streamlit e gerencia a entrada de dados.
    """
    st.title("Sistema de Inferência de Diagnósticos")

    # Carregar arquivos de sintomas, diagnósticos e regras
    sintomas_path = st.file_uploader("Carregar arquivo de sintomas")
    diagnosticos_path = st.file_uploader("Carregar arquivo de diagnósticos")
    regras_path = st.file_uploader("Carregar arquivo de regras")

    if sintomas_path and diagnosticos_path and regras_path:
        # Ler predicados e regras dos arquivos
        predicados_sintomas = ler_predicados_de_arquivo(sintomas_path)
        predicados_diagnosticos = ler_predicados_de_diagnosticos_de_arquivo(diagnosticos_path)
        regras = ler_definicao_de_regras(regras_path, predicados_sintomas, predicados_diagnosticos)

        # Inicializar o motor de inferência
        motor = MotorDeInferencia(regras)
        paciente = st.text_input("Digite o nome do paciente")
        sintomas = st.text_input("Digite os sintomas do paciente separados por vírgula")
        if st.button("Adicionar Sintoma"):
            # Adicionar sintomas ao motor de inferência
            for sintoma in sintomas.split(','):
                motor.adicionar_fato(paciente, Predicado(sintoma.strip()))
            motor.mostrar_fatos()

if __name__ == "__main__":
    main()