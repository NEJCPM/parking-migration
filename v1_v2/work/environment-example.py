# Dados de conexão com o ssh da máquina local
ssh_host = "172.17.0.1" # ip do host dentro do container docker
ssh_username = "user"
ssh_password = "***"

# Banco de onde os dados serão migrados, versão 1 da aplicação
source_database_host = "host"
source_database_port = 3306
source_database_username = "user"
source_database_password = "***"
source_database_name = "database"

# Banco de destido para onde os dados serão migrados, Versão 2 da aplicação
target_database_host = "172.17.0.1"
target_database_port = 5449
target_database_username = "develop"
target_database_password = "develop"
target_database_name = "parking"

# Mapeamento entre tenant_id e shopping_id
tenants_to_shopping = {
    "d7640ec1-d199-4fa9-a8a0-4f42501aa519": "ead5811c-3105-11ec-8d3d-0242ac130003", # RioMar Recife
}

# Shopping_id do shopping que será migrado
current_shopping = "ead5811c-3105-11ec-8d3d-0242ac130003"