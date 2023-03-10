# Impuestito
> ## Descripcion
Impuestito es una API local para calcular impuestos al hacer compras al exterior, tambien tiene una herramienta para saber el precio oficial de diferentes cotizaciones en argentina como el dolar, el euro, dolar blue u otros. 
> ## Instalando
Puedes instalar o actualizar la API desde [pip](https://pip.pypa.io/en/stable/getting-started/):
```$ pip install impuestito```

 
# Ejemplos
> ## Calcular precio de compra al exterior con cualquier moneda
>> No importa si pones dolares, pesos, euros o cualquier otra moneda ya que la moneda no afecta el calculo
```
# Importamos la funcion de la API
from impuestito import calcularImpuestoPais

# Para mayor comodidad declaramos variable. Esta funcion le pedira a la API que le calcule el impuesto pais a la cantidad que pase de parametro, por ejemplo en este caso calcularemos 230 pesos.
x = calcularImpuestoPais(230).

# Imprimimos el resultado
print(x)

>> {'cantidadVieja': 230, 'agregado': 172.5, 'cantidadFinal': 402.5}

# Si queremos obtener la variable final que seria el total debemos imprimir esto:
print(x["cantidadFinal"])

>> 402.5

```

> ## Obtener precio del dolar oficial 
```
# Importamos la funcion de la API
from impuestito import dolarOficial

# Para mayor comodidad declaramos variable. Esta funcion le pedira a la API que le transforme $2 a Pesos
x = dolarOficial.aPesos(2)

# Imprimimos el resultado
print(x)

>> {'usd': 2, 'dolarPrice': 176.0, 'total': 352.0}

# Si queremos obtener la variable final que seria el total debemos imprimir esto:
print(x["total"])

>> 352.0

```

## Contacto & Donaciones
Si necesitas ayuda con algo o quieres ayudarme donando aqui te dejo algunos datos:

Discord: Pina#0001
Web: http://pinayt.tk
Paypal: https://paypal.me/pinaytt
