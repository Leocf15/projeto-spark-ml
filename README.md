# Análise de Dados com Apache Spark

Este projeto utiliza o Apache Spark para realizar análises de dados e treinamento de modelos de machine learning. O código é escrito em Python com a API `pyspark` e inclui etapas como limpeza de dados, transformação, treinamento de modelos e avaliação de desempenho.

## 🚀 Sobre o Projeto

O objetivo deste projeto é demonstrar como o Apache Spark pode ser usado para processar grandes volumes de dados e construir modelos de machine learning escaláveis. O código realiza as seguintes etapas:

1. **Carregamento de dados**: Leitura de um arquivo CSV.
2. **Limpeza e transformação**: Remoção de valores nulos e conversão de variáveis categóricas em numéricas.
3. **Engenharia de features**: Criação de um vetor de features para treinamento do modelo.
4. **Treinamento do modelo**: Uso de regressão logística para classificação.
5. **Avaliação do modelo**: Cálculo da acurácia do modelo.
6. **Implantação do modelo**: Salvamento e carregamento do modelo treinado.

## 📋 Requisitos

Para executar este projeto, você precisará de:

- **Apache Spark**: Instalado e configurado.
- **Python 3.x**: Com as seguintes bibliotecas instaladas:
  ```bash
  pip install pyspark pandas numpy
