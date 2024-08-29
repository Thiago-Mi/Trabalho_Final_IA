# Este documento descreve a representação do conhecimento e o funcionamento do motor de inferência em um sistema de diagnóstico baseado em regras. 

O sistema utiliza sintomas observados para inferir possíveis diagnósticos com graus de certeza e probabilidade.

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
