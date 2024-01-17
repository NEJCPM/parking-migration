# Migração do Estacionamento V1 para V2

## Overview

Scripts criados utilizando Jupyter, Pandas e Python para realizar a migração dos dados do serviço de estacionamento V1 para a V2.

## Configurando o ambiente

- Crie um arquivo environment.py, na pasta work, utilizando o arquivo "environment-example.py" como exemplo.

- Ajuste as variáveis de ambiente no arquivo "environment.py" de acordo com o ambiente que deve ser migrado.

- Para cada shopping ajuste a variável "current_shopping"

- Adicione o mapeamento de tenent_id para shopping_id do shopping

- Inicie o container docker para executar o Jupyter executando o comando abaixo:

```sh
docker-compose up
```

- Configure um servidor ssh em sua máquina local e configure as credencias nas variáveis de ambiente para que os scripts executados dentro do container possam acessar os bancos de dados.

- Caso seja necessário, conecte-se à VPN onde os bancos de dados são acessíveis.

## Executando a migração

A migração dos dados é realizada em três etapas:

> extração dos dados -> transformação dos dados -> inserção dos dados

Na pasta "data" são salvos os dados, já tratados, que serão inseridos no banco de dados alvo (V2).
Na pasta "data_source" são salvos os registros do banco de dados de origem (V1).
Na pasta "data_target" são salvos os registros do banco de dados de destino (V2).

**Importante!** Execute os notebooks nesta ordem exata, pois alguns notebooks dependem dos outputs de outros notebooks.

Execute os notebooks na sequencia abaixo:

1. extract_data_source
2. extract_data_target
3. transform_faq
4. transform_pricing
5. transform_customer
6. transform_card
7. transform_ticket
8. transform_transaction
9. transform_receipt
10. transform_advert
11. insert_faq
12. insert_pricing
13. insert_customer
14. insert_card
15. insert_ticket
16. insert_transaction
17. insert_receipt
18. insert_advert
