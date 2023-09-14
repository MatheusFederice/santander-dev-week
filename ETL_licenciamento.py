import pandas as pd
from datetime import datetime, timedelta

# Lê o arquivo CSV
df = pd.read_csv("list.csv", sep=";")

# Seleciona as colunas de interesse
colunas = [
    "Nome do empreendimento", "CPF/CNPJ do empreendimento",
    "Data de vencimento da licença", "Código da tipologia",
    "Descrição da tipologia", "Potencial poluidor",
    "Logradouro do empreendimento", "Número do endereço do empreendimento",
    "Município do empreendimento", "CEP do empreendimento",
    "UF do empreendimento", "Latitude", "Longitude"
]

# Define a lista de municípios desejados
municipios_desejados = [
    "ARUJÁ", "BIRITIBA-MIRIM", "FERRAZ DE VASCONCELOS", "GUARAREMA",
    "GUARULHOS", "ITAQUAQUECETUBA", "MOGI DAS CRUZES", "POÁ",
    "SALESÓPOLIS", "SANTA ISABEL", "SUZANO", "DIADEMA", "MAUÁ",
    "RIBEIRÃO PIRES", "RIO GRANDE DA SERRA", "SANTO ANDRÉ",
    "SÃO BERNARDO DO CAMPO", "SÃO CAETANO DO SUL", "COTIA", "EMBU",
    "EMBU-GUAÇU", "ITAPECERICA DA SERRA", "JUQUITIBA",
    "SÃO LOURENÇO DA SERRA", "TABOÃO DA SERRA", "VARGEM GRANDE PAULISTA",
    "BARUERI", "CARAPICUÍBA", "ITAPEVI", "JANDIRA", "OSASCO",
    "PIRAPORA DO BOM JESUS", "SANTANA DE PARNAÍBA",
    "CAIEIRAS", "CAJAMAR", "FRANCISCO MORATO", "FRANCO DA ROCHA", "MAIRIPORÃ"
]

# Calcula a data atual
data_atual = datetime.now()

# Calcula a data limite (180 dias a partir da data atual)
data_limite = data_atual + timedelta(days=180)

# Filtra o DataFrame com base nas condições
empreendimentos_filtrados = df[
    (df["Município do empreendimento"].str.upper().isin(municipios_desejados)) &
    (( (pd.to_datetime(df["Data de vencimento da licença"]) >= data_atual) & (pd.to_datetime(df["Data de vencimento da licença"]) <= data_limite) )
)
][colunas]

# Define o nome do arquivo Excel 
nome_arquivo_saida = "empreendimentos_filtrados.xlsx"

# Exporta o DataFrame em formato Excel
empreendimentos_filtrados.to_excel(nome_arquivo_saida, index=False)

# Imprime uma mensagem de confirmação
print(f'Dados exportados para {nome_arquivo_saida}')
