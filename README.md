**Objetivo do Projeto:** Este projeto, realizado como parte do bootcamp do Santander pela DIO, tem como finalidade a extração e análise de dados a partir de uma planilha disponível no **[Portal Nacional de Licenciamento Ambiental (PNLA)](https://pnla.mma.gov.br/pesquisa-de-licenciamento-ambiental)** referente às Licenças Ambientais de Operação vigentes no estado de São Paulo. O objetivo principal é identificar potenciais clientes para serviços de renovação de Licenças de Operação.

**Fases do Projeto:**

1. **EXTRAÇÃO (Extract):** Inicialmente, realizamos a extração da base de dados mencionada no PNLA. Esta base de dados contém informações sobre empreendimentos que possuem Licenças Ambientais de Operação ativas.
2. **TRANSFORMAÇÃO (Transform):** Na fase de transformação, refinamos os dados para identificar os empreendimentos que necessitarão renovar suas licenças até o final de 2023. Esta seleção é baseada em informações como a data de vencimento da licença, que deve ser menor ou igual a 180 dias a partir da data atual. Além disso, limitamos a nossa análise aos empreendimentos localizados na região metropolitana de São Paulo, composta por **[39 municípios](https://gestaourbana.prefeitura.sp.gov.br/marco-regulatorio/pdui/entidades-publicas-da-rmsp/#:~:text=Leste%3A%20Aruj%C3%A1%2C%20Biritiba%2DMirim,e%20S%C3%A3o%20Caetano%20do%20Sul.)**.
3. **CARGA (Load):** Finalmente, criamos uma nova base de dados que contém apenas os empreendimentos selecionados, ou seja, a lista de leads válidos. Essa lista é exportada para o Google Sheets e inclui informações relevantes para abordar esses potenciais clientes e oferecer serviços de renovação de Licenças de Operação.

**Dados Coletados:**

A lista de leads gerada contém as seguintes informações essenciais:

- Nome do empreendimento
- Código da tipologia (CNAE)
- Descrição da tipologia (CNAE)
- Potencial poluidor (W)
- CPF/CNPJ do empreendimento
- Endereço completo do empreendimento, incluindo logradouro, número, distrito, município, CEP e UF
- Data de vencimento da licença

Este projeto de ETL (Extração, Transformação e Carga) automatizado permite identificar oportunidades de negócios significativas na região metropolitana de São Paulo, agilizando o processo de prospecção de clientes que necessitam dos serviços de renovação de Licenças de Operação.
