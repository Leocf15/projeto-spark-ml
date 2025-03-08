# Coleta e Preparação dos Dados
from pyspark.sql import SparkSession

# Inicializa a sessão do Spark
spark = SparkSession.builder.appName("MachineLearning").getOrCreate()

# Carrega os dados
df = spark.read.csv("caminho/do/arquivo.csv", header=True, inferSchema=True)

# Limpeza e Transformação
from pyspark.sql.functions import col

# Remove linhas com valores nulos
df = df.na.drop()

# Converte variáveis categóricas em numéricas
from pyspark.ml.feature import StringIndexer
indexer = StringIndexer(inputCol="categoria", outputCol="categoria_index")
df = indexer.fit(df).transform(df)

# Engenharia de Features
from pyspark.ml.feature import VectorAssembler

# Define as colunas de features e a coluna de label
feature_columns = ["feature1", "feature2", "categoria_index"]
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
df = assembler.transform(df)

# Divisão dos Dados
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# Treinamento do Modelo
from pyspark.ml.classification import LogisticRegression

# Define e treina o modelo
lr = LogisticRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_data)

# Previsões
predictions = model.transform(test_data)

# Avaliação de Acurácia
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Acurácia: {accuracy}")

# Implantação do Modelo
model.save("caminho/para/salvar/modelo")

# Carregamento do Modelo e Novas Previsões
from pyspark.ml.classification import LogisticRegressionModel

# Carrega o modelo
loaded_model = LogisticRegressionModel.load("caminho/para/salvar/modelo")

# Faz previsões em novos dados
new_predictions = loaded_model.transform(new_data)
