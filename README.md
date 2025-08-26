# Análise Comparativa: Regressão Linear vs Lasso no Dataset California Housing

## Descrição do Projeto
Este projeto compara o desempenho da **Regressão Linear** e do **Lasso Regression** na previsão do valor médio das casas no dataset **California Housing**, utilizando métricas como **Mean Squared Error (MSE)** e **R²**.  
Além disso, realiza uma análise visual comparando os coeficientes obtidos por cada modelo, permitindo observar a influência de cada variável na predição.

O dataset contém informações como idade média das casas, número médio de cômodos, população da região, latitude e longitude.


---

## Tecnologias Utilizadas
- Python 3.x  
- Bibliotecas:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `scikit-learn`

---

Análise de Regressão Linear e Lasso

Este projeto apresenta a aplicação de Regressão Linear e Regressão Lasso sobre o conjunto de dados de habitação da Califórnia, com o objetivo de prever o valor médio das casas a partir de variáveis como renda média, idade da casa, número médio de quartos, entre outras.

Resultados da Regressão Linear
Variável	Coeficiente
Intercept	-37.0233
MedInc       0.448675
HouseAge     0.009724
AveRooms    -0.123323
AveBedrms    0.783145
Population  -0.000002
AveOccup    -0.003526
Latitude    -0.419792
Longitude   -0.433708

MSE (Mean Squared Error): 0.5559

R² (Coeficiente de Determinação): 0.5758

Resultados da Regressão Lasso
Variável	Coeficiente
Intercept	-35.0475
MedInc	0.4089
HouseAge	0.0103
AveRooms	-0.0474
AveBedrms	0.3633
Population	-0.0000003
AveOccup	-0.0034
Latitude	-0.4071
Longitude	-0.4149

MSE (Mean Squared Error): 0.5444

R² (Coeficiente de Determinação): 0.5845

Através da análise dos dados, é possível notar que o modelo Lasso apresenta leve melhoria no ajuste, reduzindo coeficientes menos relevantes e controlando overfitting.
Variáveis como MedInc, AveBedrms, Latitude e Longitude são as mais influentes no valor médio das casas.
Ambos os modelos conseguem explicar boa parte da variabilidade dos preços, com Lasso tendo desempenho ligeiramente superior à regressão linear simples.
Também é possível visualizar a diferença nos coeficientes das variáveis independentes no gráfico gerado no repositório
