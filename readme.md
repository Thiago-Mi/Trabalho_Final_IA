# Este documento descreve a representação do conhecimento e o funcionamento do motor de inferência em um sistema de diagnóstico baseado em regras. 

O sistema utiliza sintomas observados para inferir possíveis diagnósticos com graus de certeza e probabilidade.

# Recapitulação da Teoria da Lógica de Primeira Ordem, Representação do Conhecimento e Motor de Inferência

## 1. Lógica de Primeira Ordem (LPO)

A Lógica de Primeira Ordem (LPO) é um sistema formal que estende a lógica proposicional, permitindo expressar relações entre objetos e suas propriedades de forma mais rica.

### Elementos Básicos
- **Termos**: Representam objetos e podem ser variáveis (ex.: `x, y`), constantes (ex.: `João, 42`), ou funções (ex.: `pai(joao)`).
- **Predicados**: Representam propriedades ou relações entre termos (ex.: `amigo(Joao, Maria)`).
- **Quantificadores**:
  - **Universal (∀)**: Afirmam que uma propriedade é verdadeira para todos os elementos (ex.: ∀x, `Pessoa(x) → Mortal(x)`).
  - **Existencial (∃)**: Afirmam que existe pelo menos um elemento que satisfaz a propriedade (ex.: ∃x, `Cachorro(x) ∧ Late(x)`).
- **Conectivos Lógicos**: Usados para combinar fórmulas (e.g., ∧ para "e", ∨ para "ou", ¬ para "não", → para "implica").

### Exemplo
A expressão ∀x (Gato(x) → Mamífero(x)) significa que todos os gatos são mamíferos.

## 2. Representação do Conhecimento

Representação do conhecimento é o processo de modelar informações e raciocínio de forma compreensível para sistemas computacionais.

### Estruturas de Representação
- **Redes Semânticas**: Grafos que representam conceitos (nós) e as relações entre eles (arestas).
- **Frames**: Estruturas que organizam o conhecimento em blocos associados a atributos e valores.
- **Sistemas de Regras**: Conjuntos de regras `Se-Então` que descrevem relações causais e inferências.
- **Lógica de Primeira Ordem**: Utiliza predicados, quantificadores e conectivos lógicos para modelar conhecimento.

### Exemplo em Sistemas de Regras
- **Regra**: Se "o paciente tem febre e tosse", então "o paciente pode ter gripe".
- **Predicado**: `febre(Paciente) ∧ tosse(Paciente) → gripe(Paciente)`.

## 3. Motor de Inferência

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

## 1. Representação do Conhecimento

A representação do conhecimento é feita através das classes `Predicado` e `Regra`, que modelam sintomas e diagnósticos.

### Classe `Predicado`
- **Descrição**: Representa um predicado, que pode ser um sintoma ou um diagnóstico.
- **Atributos**:
  - `nome`: Nome do predicado (ex.: "febre").
  - `args`: Argumentos associados ao predicado (ex.: "Paciente").
- **Métodos**:
  - `__repr__()`: Retorna a representação em string no formato "nome(arg1, arg2, ...)".
  - `__eq__()`: Compara dois predicados para verificar igualdade com base no nome e nos argumentos.
  - `__hash__()`: Implementa um hash para uso em conjuntos (sets).

### Classe `Regra`
- **Descrição**: Representa uma regra de inferência que relaciona sintomas a um diagnóstico.
- **Atributos**:
  - `antecedente`: Lista de predicados representando os sintomas.
  - `consequente`: Predicado resultante (diagnóstico).
  - `peso`: Peso da regra, indicando o grau de certeza (entre 0 e 1).
- **Métodos**:
  - `__repr__()`: Retorna uma representação textual da regra.

## 2. Motor de Inferência

O motor de inferência utiliza as regras definidas para inferir novos fatos a partir dos sintomas fornecidos.

### Classe `MotorDeInferencia`
- **Atributos**:
  - `regras`: Lista de regras utilizadas pelo motor de inferência.
  - `fatos`: Conjunto de fatos conhecidos (sintomas observados).
  - `certeza`: Dicionário que armazena a certeza acumulada dos diagnósticos inferidos.
  - `probabilidade`: Dicionário que armazena a probabilidade acumulada dos diagnósticos inferidos.
- **Métodos**:
  - `adicionar_fato(fato)`: Adiciona um novo fato (sintoma) e inicia o processo de inferência.
  - `inferir()`: Avalia cada regra e atualiza a certeza e probabilidade dos diagnósticos.
  - `atualizar_certeza(diagnostico, fracao_certeza)`: Atualiza a certeza de um diagnóstico.
  - `atualizar_probabilidade(diagnostico, fracao_probabilidade)`: Atualiza a probabilidade de um diagnóstico usando uma abordagem simplificada da regra de Bayes.
  - `mostrar_fatos()`: Exibe os fatos conhecidos e as certezas e probabilidades dos diagnósticos.

## 3. Exemplo de Uso

Exemplo de uso do motor de inferência:
1. Instancia o motor de inferência com uma lista de regras.
2. Adiciona fatos como "febre", "tosse", "dificuldade respiratória" e "fadiga".
3. O motor faz inferências com base nos fatos e regras, exibindo os resultados.

## 4. Funcionamento do Processo de Inferência

- O motor avalia as regras para verificar quais podem ser aplicadas com base nos fatos conhecidos.
- Para cada regra, calcula-se a certeza e probabilidade do diagnóstico com base nos sintomas presentes.
- A certeza acumulada aumenta conforme o número de sintomas correspondentes aos antecedentes da regra.
- A probabilidade é ajustada para considerar a combinação de eventos múltiplos, refinando a confiança no diagnóstico.

## 5. Conclusão

Este sistema permite inferir diagnósticos baseados em sintomas observados usando regras de conhecimento pré-definidas. A combinação de múltiplas regras possibilita um diagnóstico com graus de certeza e probabilidade, tornando o sistema flexível e capaz de lidar com novos fatos.
