# Desafio Backend Jeitto

O desafio foi implementar uma API em Python para simular a contratação de crédito telefônico


## Pré-requisistos

MongoDB exposto na porta 27017  
Python3

## Rodar o Projeto
#### Sem Docker
Sugiro fortemente que seja utilizado o ambiente virtual do python (VirtualEnv) para que não haja conflitos de dependências entre outros projetos python  
Assumindo que os pré-requisitos, citados anteriormente, estão em plena conformidade, para rodar o projeto basta instalarmos as dependências da seguinte maneira:

> pip install --trusted-host pypi.python.org -r requirements.txt

Assim que as dependências forem instaladas, basta executarmos o script principal, da seguinte maneira:
> python3 main.py

#### Com docker
Na raiz do projeto execute:
> docker build --tag=teste-jeitto .

após a conclusão do comando supracitado, execute:
> docker run -p 8080:8080 teste-jeitto

## EndPoints
Os exemplos de chamada de todos os endpoints estão numa coleção postman nomeada de `Jeitto Recarga.postman_collection.json` na raiz deste projeto
Caso a mesma seja importada no Postman, será possível realizar os testes dos endpoints.

#### Criar Companhia
> POST localhost:8080/CompanyProducts

Request
```json
{
	"name": "New Company",
	"products": [{"name": "Produto 1", "value": 5}]
}
```
Response
```json
{
    "id": "5cd86ac275c5083811275942",
    "name": "New Company",
    "products": [
        {
            "id": "5cd86ac275c5083811275941",
            "name": "Produto 1",
            "value": 5
        }
    ]
}
```

#### Consultar Companhias
> GET localhost:8080/CompanyProducts

```json
[
    {
        "id": "5cd8525575c50829dd6ad390",
        "name": "teste Shodi 1",
        "products": [
            {
                "id": "5cd8525575c50829dd6ad38f",
                "name": "Produto 2",
                "value": 0.01
            }
        ]
    },
    {
        "id": "5cd86ac275c5083811275942",
        "name": "New Company",
        "products": [
            {
                "id": "5cd86ac275c5083811275941",
                "name": "Produto 1",
                "value": 5
            }
        ]
    }
]
```


___


> GET localhost:8080/CompanyProducts?companyId=5cd8525575c50829dd6ad390

```json
{
    "id": "5cd8525575c50829dd6ad390",
    "name": "teste Shodi 1",
    "products": [
        {
            "id": "5cd8525575c50829dd6ad38f",
            "name": "Produto 2",
            "value": 0.01
        }
    ]
}
```


___


> GET http://localhost:8080/CompanyProducts?companyName=teste%20Shodi%201

```json
[
    {
        "id": "5cd8525575c50829dd6ad390",
        "name": "teste Shodi 1",
        "products": [
            {
                "id": "5cd8525575c50829dd6ad38f",
                "name": "Produto 2",
                "value": 0.01
            }
        ]
    }
]
```

___


> GET localhost:8080/CompanyProducts?productId=5cd86ac275c5083811275941

```json
{
    "id": "5cd86ac275c5083811275942",
    "name": "New Company",
    "products": [
        {
            "id": "5cd86ac275c5083811275941",
            "name": "Produto 1",
            "value": 5
        }
    ]
}
```

#### Recarga Telefônica
> POST localhost:8080/PhoneRecharges

Request
```json
{
	"phoneNumber": "952554155",
	"productId": "5cd86ac275c5083811275941",
	"companyId": "5cd86ac275c5083811275942",
	"value": 50
}
```

Response
```json
{
    "id": "5cd87a6975c50842ece8d134",
    "createdAt": "2019-05-12 16:56:25.848803",
    "companyId": "5cd86ac275c5083811275942",
    "productId": "5cd86ac275c5083811275941",
    "phoneNumber": "952554155",
    "value": 50
}
```

#### Consulta Recarga Telefônica
> GET localhost:8080/PhoneRecharges

```json
[
    {
        "id": "5cd8713775c5083d7229a1b9",
        "createdAt": "2019-05-12 16:17:11.242767",
        "companyId": "5cd8525575c50829dd6ad390",
        "productId": "5cd8525575c50829dd6ad38f",
        "phoneNumber": "952554155",
        "value": 50
    },
    {
        "id": "5cd872ed75c5083e78f67a63",
        "createdAt": "2019-05-12 16:24:29.124370",
        "companyId": "5cd8525575c50829dd6ad390",
        "productId": "5cd8525575c50829dd6ad38f",
        "phoneNumber": "952554155",
        "value": 50
    }
]
```

___


> GET localhost:8080/PhoneRecharges?id=5cd8713775c5083d7229a1b9

```json
{
    "id": "5cd8713775c5083d7229a1b9",
    "createdAt": "2019-05-12 16:17:11.242767",
    "companyId": "5cd8525575c50829dd6ad390",
    "productId": "5cd8525575c50829dd6ad38f",
    "phoneNumber": "952554155",
    "value": 50
}
```


___


> GET localhost:8080/PhoneRecharges?phoneNumber=952554155

```json
[
    {
        "id": "5cd8713775c5083d7229a1b9",
        "createdAt": "2019-05-12 16:17:11.242767",
        "companyId": "5cd8525575c50829dd6ad390",
        "productId": "5cd8525575c50829dd6ad38f",
        "phoneNumber": "952554155",
        "value": 50
    },
    {
        "id": "5cd872ed75c5083e78f67a63",
        "createdAt": "2019-05-12 16:24:29.124370",
        "companyId": "5cd8525575c50829dd6ad390",
        "productId": "5cd8525575c50829dd6ad38f",
        "phoneNumber": "952554155",
        "value": 50
    },
    {
        "id": "5cd874f575c5083f907fbc3b",
        "createdAt": "2019-05-12 16:33:09.324727",
        "companyId": "5cd86ac275c5083811275942",
        "productId": "5cd8525575c50829dd6ad38f",
        "phoneNumber": "952554155",
        "value": 50
    },
    {
        "id": "5cd8789675c508418ef1deb4",
        "createdAt": "2019-05-12 16:48:38.403168",
        "companyId": "5cd86ac275c5083811275942",
        "productId": "5cd86ac275c5083811275941",
        "phoneNumber": "952554155",
        "value": 50
    }
]
```