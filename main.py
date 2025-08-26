import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

data = fetch_california_housing(as_frame=True)
df = data.frame

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

#APLICAÇÃO DA REGRESSÃO LINEAR

linear = LinearRegression().fit(X_train, y_train)
linear_intercept = linear.intercept_
linear_coefs = pd.DataFrame(linear.coef_, index=X.columns, columns=['Coeficientes'])
y_linear_pred = linear.predict(X_test)
mse_linear = mean_squared_error(y_test, y_linear_pred)
r2_linear = r2_score(y_test, y_linear_pred)


print(" *** ANÁLISE DA REGRESSÃO LINEAR ***")

print(f'Intercept(Linear): {linear_intercept}')
print(linear_coefs)
print(f'MSE(Linear):  {mse_linear}')
print(f'R2(Linear): {r2_linear}')



#APLICAÇÃO DO LASSO UTILIZANDO ALPHA = 0.01

lasso = Lasso(alpha=0.01)
lasso.fit(X_train, y_train)
lasso_coefs = pd.DataFrame(lasso.coef_, index=X.columns, columns=['Coeficientes'])
lasso_intercept = lasso.intercept_
y_lasso_pred = lasso.predict(X_test)
mse_lasso = mean_squared_error(y_test, y_lasso_pred)
r2_lasso = r2_score(y_test, y_lasso_pred)

print(" *** ANÁLISE DO LASSO *** ")

print(f'Intercept(LASSO): {lasso_intercept}')
print(lasso_coefs)
print(f'MSE(Lasso):  {mse_lasso}')
print(f'R2(Lasso): {r2_lasso}')

#PLOTANDO O COMPARATIVO ENTRE OS COEFS DA REGRESSÃO LINEAR E DO LASSO

def plot_coefs(linear_coefs, lasso_coefs):
    df = pd.concat([linear_coefs, lasso_coefs], axis=1)
    df.columns = ['Linear', 'Lasso']
    df.plot(kind='bar', figsize=(10,6))
    plt.title('Comparação dos Coeficientes')
    plt.ylabel('Valor do Coeficiente')
    plt.savefig("graph analysis.png")
    plt.show()


plot_coefs(linear_coefs, lasso_coefs)









