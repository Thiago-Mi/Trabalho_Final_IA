# Sistema que utiliza sintomas observados para inferir possíveis diagnósticos com graus de certeza e probabilidade.

Este sistema foi construído com base em um motor de inferência de lógica de primeira ordem, onde regras são aplicadas para relacionar sintomas observados a possíveis diagnósticos. Ele utiliza graus de certeza e probabilidade, calculados a partir de múltiplos sintomas e regras, permitindo diagnósticos mais precisos. A interface é acessível através do link [Dignóstico por inferência](https://inferencia-diagnostic.streamlit.app/).


# Recapitulação da Teoria da Lógica de Primeira Ordem, Representação do Conhecimento e Motor de Inferência

# Lógica de Primeira Ordem (LPO)

A Lógica de Primeira Ordem (LPO) é um sistema formal que estende a lógica proposicional, permitindo expressar relações entre objetos e suas propriedades de forma mais rica.

## Elementos Básicos
- **Termos**: Representam objetos e podem ser variáveis (ex.: `x, y`), constantes (ex.: `João, 42`), ou funções (ex.: `pai(joao)`).
- **Predicados**: Representam propriedades ou relações entre termos (ex.: `amigo(Joao, Maria)`).
- **Quantificadores**:
  - **Universal (∀)**: Afirmam que uma propriedade é verdadeira para todos os elementos (ex.: ∀x, `Pessoa(x) → Mortal(x)`).
  - **Existencial (∃)**: Afirmam que existe pelo menos um elemento que satisfaz a propriedade (ex.: ∃x, `Cachorro(x) ∧ Late(x)`).
- **Conectivos Lógicos**: Usados para combinar fórmulas (e.g., ∧ para "e", ∨ para "ou", ¬ para "não", → para "implica").

### Exemplo
Por exemplo, podemos definir a regra: ∀x (Febre(x) ∧ Tosse(x) → Gripe(x)), que indica que se um paciente apresenta febre e tosse, ele pode ser diagnosticado com gripe.


## 1. Representação do Conhecimento

Representação do conhecimento é o processo de modelar informações e raciocínio de forma compreensível para sistemas computacionais.

### Estruturas de Representação
- **Redes Semânticas**: Grafos que representam conceitos (nós) e as relações entre eles (arestas).
- **Frames**: Estruturas que organizam o conhecimento em blocos associados a atributos e valores.
- **Sistemas de Regras**: Conjuntos de regras `Se-Então` que descrevem relações causais e inferências.
- **Lógica de Primeira Ordem**: Utiliza predicados, quantificadores e conectivos lógicos para modelar conhecimento.

### Exemplo em Sistemas de Regras
- **Regra**: Se "o paciente tem febre e tosse", então "o paciente pode ter gripe".
- **Predicado**: `febre(Paciente) ∧ tosse(Paciente) → gripe(Paciente)`.

## 2. Motor de Inferência

Um motor de inferência utiliza regras de conhecimento para deduzir novos fatos ou conclusões a partir dos dados conhecidos.

### Funcionamento Básico
- **Entrada**: Conjunto de fatos (informações conhecidas) e regras.
- **Processo de Inferência**:
  - **Encadeamento Progressivo (Forward Chaining)**: Começa com os fatos conhecidos e aplica regras para inferir novos fatos.
  - **Encadeamento Regressivo (Backward Chaining)**: Começa com uma meta e trabalha "para trás" para verificar quais fatos e regras sustentam essa meta.
- **Saída**: Novos fatos ou diagnósticos baseados nas inferências feitas.

### Exemplo de Inferência
- **Regras**:
  - Regra 1: `febre(Paciente) ∧ tosse(Paciente) → gripe(Paciente)` (com peso 0.8).
  - Regra 2: `tosse(Paciente) ∧ coriza(Paciente) → resfriado(Paciente)` (com peso 0.5).
- **Fatos Conhecidos**: `febre(Paciente)`, `tosse(Paciente)`.
- **Inferência**: O sistema infere que o paciente pode ter gripe com uma certeza de 0.8.

### Componentes do Motor de Inferência
- **Base de Conhecimento**: Conjunto de fatos e regras.
- **Mecanismo de Inferência**: Avalia regras em relação aos fatos e executa inferências.
- **Gestão de Incerteza**: Atribui graus de certeza ou probabilidade às conclusões inferidas, utilizando técnicas como pesos das regras.

A lógica de primeira ordem oferece uma estrutura poderosa para expressar raciocínios formais, enquanto as técnicas de representação do conhecimento tornam as informações utilizáveis para processamento por sistemas computacionais. Os motores de inferência utilizam essas estruturas para simular o raciocínio humano, aplicando regras para alcançar conclusões úteis em sistemas de diagnóstico, recomendação, entre outros. 
Abaixo está o passo a passo da implementação do sistema de inferência utilizado nesse trabalho.

# Representação do Conhecimento

A representação do conhecimento é feita através das classes `Predicado` e `Regra`, que modelam sintomas e diagnósticos.

#### Classe `Predicado`
- **Descrição**: Representa um predicado, que pode ser um sintoma ou um diagnóstico.
- **Atributos**:
  - `nome`: Nome do predicado (ex.: "febre").
- **Métodos**:
  - `__repr__()`: Retorna a representação em string no formato "nome".
  - `__eq__()`: Compara dois predicados para verificar igualdade com base no nome.
  - `__hash__()`: Implementa um hash para uso em conjuntos (sets).

#### Classe `Regra`
- **Descrição**: Representa uma regra de inferência que relaciona sintomas a um diagnóstico.
- **Atributos**:
  - `antecedente`: Lista de predicados representando os sintomas.
  - `consequente`: Predicado resultante (diagnóstico).
  - `peso`: Peso da regra, indicando o grau de certeza (entre 0 e 1).
- **Métodos**:
  - `__repr__()`: Retorna uma representação textual da regra.

## 1. Motor de Inferência

O motor de inferência implementado utiliza as regras definidas para inferir novos fatos a partir dos sintomas fornecidos.

### Classe `MotorDeInferencia`
- **Atributos**:
  - `regras`: Lista de regras utilizadas pelo motor de inferência.
  - `fatos_por_paciente`: Dicionário que armazena fatos conhecidos (sintomas observados) por paciente.
  - `certeza_por_paciente`: Dicionário que armazena a certeza acumulada dos diagnósticos inferidos por paciente.
  - `probabilidade_por_paciente`: Dicionário que armazena a probabilidade acumulada dos diagnósticos inferidos por paciente.
- **Métodos**:
  - `adicionar_fato(paciente, fato)`: Adiciona um novo fato (sintoma) e inicia o processo de inferência.
  - `inferir(paciente)`: Avalia cada regra e atualiza a certeza e probabilidade dos diagnósticos.
  - `atualizar_certeza(paciente, diagnostico, fracao_certeza)`: Atualiza a certeza de um diagnóstico.
  - `atualizar_probabilidade(paciente, diagnostico, fracao_probabilidade)`: Atualiza a probabilidade de um diagnóstico usando uma abordagem simplificada da regra de Bayes.
  - `mostrar_fatos()`: Exibe os fatos conhecidos e as certezas e probabilidades dos diagnósticos.

## 2. Leitura de Dados de Arquivos

O sistema agora lê os predicados de sintomas, diagnósticos e regras de arquivos `.txt`.

### Funções de Leitura
- **ler_predicados_de_arquivo(uploaded_file)**: Lê predicados de sintomas de um arquivo.
- **ler_predicados_de_diagnosticos_de_arquivo(uploaded_file)**: Lê predicados de diagnósticos de um arquivo.
- **ler_definicao_de_regras(uploaded_file, predicados_sintomas, predicados_diagnosticos)**: Lê a definição de regras de um arquivo.

### Exemplo de Conteúdo dos Arquivos `.txt`:
- **sintomas.txt**:

- ``febre``
- ``tosse``
- ``dor_de_garganta``
- ``dor_no_corpo``

- **diagnosticos.txt**:

- ``Gripe``
- ``Resfriado``
- ``COVID19``
- ``Mononucleose``

- **regras.txt**:

- ``febre,tosse,dor_de_garganta,dor_no_corpo;Gripe;0.8`` 
- ``tosse,dor_de_garganta;Resfriado;0.5 ``
- ``febre,tosse,fadiga,dificuldade_respiratoria;COVID-19;0.9 ``
- ``fadiga,dor_de_garganta,febre;Mononucleose;0.7 ``

## 3. Exemplo de Uso

Exemplo de uso do motor de inferência:
1. Instancia o motor de inferência com uma lista de regras.
2. Adiciona fatos como "febre", "tosse", "dificuldade respiratória" e "fadiga".
3. O motor faz inferências com base nos fatos e regras, exibindo os resultados.

## 4. Funcionamento do Processo de Inferência

- O motor avalia as regras para verificar quais podem ser aplicadas com base nos fatos conhecidos.
- Para cada regra, calcula-se a certeza e probabilidade do diagnóstico com base nos sintomas presentes.
- A certeza é calculada como uma fração do grau de correspondência entre os sintomas observados e os antecedentes da regra, ponderada pelo peso da regra.
- A probabilidade é ajustada de acordo com a combinação de múltiplos sintomas, utilizando a regra de Bayes para calcular a probabilidade combinada de um diagnóstico.

### Cálculo de Certeza e Probabilidade

**Cálculo de Certeza:**
- A certeza acumulada de um diagnóstico para um paciente é atualizada com base na fração de certeza fornecida.
- A fração de certeza é calculada como: 
  `fração de certeza = peso × (num_correlações / total_antecedentes)`
- Se o diagnóstico ainda não possui uma certeza acumulada para o paciente, a fração de certeza fornecida é usada como a certeza inicial.
- Se o diagnóstico já possui uma certeza acumulada, a nova fração de certeza é combinada com a certeza existente usando uma média aritmética.

**Cálculo de Probabilidade:**
- A probabilidade acumulada de um diagnóstico para um paciente é atualizada usando uma versão simplificada da regra de Bayes.
- A fração de probabilidade é calculada como:
  `fração de probabilidade = 1 - (1 - peso) ^ (num_correlações / total_antecedentes)`
- Se o diagnóstico ainda não possui uma probabilidade acumulada para o paciente, a fração de probabilidade fornecida é usada como a probabilidade inicial.
- Se o diagnóstico já possui uma probabilidade acumulada, a nova fração de probabilidade é combinada com a probabilidade existente usando a fórmula:
  `P(A|B) = 1 - (1 - P(A|B_anterior)) × (1 - P(B|A))` onde `P(A|B_anterior)` é a probabilidade acumulada anterior e `P(B|A)` é a nova fração de probabilidade.


## 5. Estrutura do Código

O sistema é dividido em três componentes principais:
- **Classe Predicado**: Representa um sintoma ou diagnóstico. Cada predicado tem um nome e pode ser comparado a outros predicados.
- **Classe Regra**: Define a relação entre sintomas (antecedentes) e diagnósticos (consequente), além de um peso que indica o grau de certeza da regra.
- **Motor de Inferência**: Gerencia o processo de inferência. Quando sintomas são adicionados, o motor avalia todas as regras e calcula a certeza e probabilidade de diagnósticos para cada paciente.


## 6. Conclusão

Este sistema permite inferir diagnósticos baseados em sintomas observados usando regras de conhecimento pré-definidas. A combinação de múltiplas regras possibilita um diagnóstico com graus de certeza e probabilidade, tornando o sistema flexível e capaz de lidar com novos fatos.

# Exemplo de uso
```python
caminho_predicados_sintomas = 'sintomas.txt'
caminho_predicados_diagnosticos = 'diagnosticos.txt'
caminho_definicao_regras = 'regras.txt'

predicados_sintomas = ler_predicados_de_arquivo(caminho_predicados_sintomas)
predicados_diagnosticos = ler_predicados_de_diagnosticos_de_arquivo(caminho_predicados_diagnosticos)
regras = ler_definicao_de_regras(caminho_definicao_regras, predicados_sintomas, predicados_diagnosticos)

motor = MotorDeInferencia(regras)
motor.adicionar_fato('Nome do Paciente',Predicado("febre"))
motor.adicionar_fato('Nome do Paciente',Predicado("tosse"))
motor.adicionar_fato('Nome do Paciente',Predicado("dificuldade_respiratoria"))
motor.adicionar_fato('Nome do Paciente',Predicado("fadiga"))
motor.mostrar_fatos()
```