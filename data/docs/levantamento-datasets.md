# Levantamento de Datasets Públicos — Sprint 1

Projeto: Painel de Projeção de Capacidade Prisional e Reincidência (PCPR)

---

## 1. InfoPen — Levantamento Nacional de Informações Penitenciárias

- **Mantenedor:** DEPEN (Ministério da Justiça e Segurança Pública)
- **Descrição:** sistema estatístico do sistema penitenciário brasileiro, alimentado pelos gestores das unidades desde 2004 e reformulado em 2014. Contém dados de infraestrutura, capacidade, população prisional e perfil das pessoas presas.
- **Granularidade:** por unidade prisional
- **Periodicidade:** historicamente semestral (2014–2016); atualmente com ciclos anuais
- **Formato de acesso:** bases publicadas em dados.gov.br e dados.mj.gov.br; versão tratada e pronta para consulta via SQL/Python/R na Base dos Dados
- **Link:** https://dados.gov.br/dataset/infopen-levantamento-nacional-de-informacoes-penitenciarias1 · https://basedosdados.org/dataset/5ee80380-83fd-4e13-b145-437cb227a087
- **Justificativa de escolha:** é a única base nacional com granularidade por unidade prisional e série histórica longa (desde 2004), essencial para calibrar o modelo de ocupação e permitir comparação entre estados além do piloto escolhido.

## 2. BNMP 3.0 — Banco Nacional de Medidas Penais e Prisões

- **Mantenedor:** CNJ (Conselho Nacional de Justiça)
- **Descrição:** registra mandados de prisão, guias de recolhimento e movimentação processual de pessoas presas, atualizado em tempo real pelo Judiciário em todo o território nacional. Em março de 2025 o CNJ lançou o Painel Estatístico do BNMP 3.0, com exportação de dados para análise externa.
- **Granularidade:** individual (nível de mandado/pessoa), agregável por unidade e UF
- **Periodicidade:** tempo real / atualização contínua
- **Formato de acesso:** Painel Estatístico BNMP 3.0; base histórica tratada disponível na Base dos Dados
- **Link:** https://www.cnj.jus.br/sistema-carcerario/bnmp-3-0/ · https://basedosdados.org/dataset/640bcf13-88f7-4475-80ce-caeddbc4beed
- **Justificativa de escolha:** é a única fonte nacional com granularidade de entrada/saída necessária para construir a variável de reincidência (retorno ao sistema prisional); a atualização em tempo real permite validação contínua, complementando o caráter semestral/anual do InfoPen.

## 3. SAP-SP — Unidades Prisionais (Secretaria da Administração Penitenciária de São Paulo)

- **Mantenedor:** Governo do Estado de São Paulo
- **Descrição:** página institucional que lista as unidades do maior sistema prisional do país, com capacidade e população atualizadas por unidade em base diária.
- **Granularidade:** por unidade prisional, diária
- **Periodicidade:** diária
- **Formato de acesso:** publicação HTML pública; Plano de Dados Abertos da SAP em fase de consolidação, prevendo formatos processáveis por máquina
- **Link:** https://www1.sap.sp.gov.br/uni-prisionais/pen-.html
- **Justificativa de escolha:** é a fonte com maior frequência de atualização entre as levantadas, o que a torna a base primária ideal para o estado-piloto (SP), permitindo validar as projeções feitas a partir do InfoPen (anual) com dados quase em tempo real. Em consulta realizada em 2026, o sistema paulista registrava população total de 229.012 pessoas distribuídas em 180 unidades — o maior sistema prisional do Brasil, o que maximiza a robustez estatística dos modelos por unidade.

## 4. IBGE — Estimativas Populacionais Municipais

- **Mantenedor:** IBGE
- **Descrição:** estimativas de população residente por município.
- **Granularidade:** municipal, anual
- **Periodicidade:** anual
- **Formato de acesso:** SIDRA/API do IBGE, exportável em CSV
- **Link:** https://sidra.ibge.gov.br/
- **Justificativa de escolha:** fornece o contexto demográfico necessário para relativizar a pressão carcerária por região (ex.: taxa de encarceramento por 100 mil habitantes), permitindo comparações entre municípios/regiões do estado-piloto.

## 5. Anuário Brasileiro de Segurança Pública

- **Mantenedor:** Fórum Brasileiro de Segurança Pública (FBSP)
- **Descrição:** compilação anual de indicadores de segurança pública e sistema prisional a partir de dados oficiais de diferentes órgãos.
- **Granularidade:** estadual, anual
- **Periodicidade:** anual
- **Formato de acesso:** PDF e planilhas complementares
- **Link:** https://forumseguranca.org.br/anuario-brasileiro-seguranca-publica/
- **Justificativa de escolha:** amplamente citado na literatura de segurança pública brasileira; usado neste projeto como fonte de validação cruzada para identificar inconsistências entre o InfoPen e as bases estaduais.

## 6. Dados Estatísticos da População Carcerária (SAP-SP)

- **Mantenedor:** Secretaria da Administração Penitenciária de São Paulo (SAP-SP)
- **Descrição:** relatório estatístico oficial com o perfil completo da população carcerária do estado (situação processual, grau de instrução, tipo penal, faixa etária, cor/raça), por regime.
- **Granularidade:** estadual agregada, por regime (fechado, semiaberto, medida de segurança, prisão civil)
- **Periodicidade:** semestral
- **Formato de acesso:** PDF publicado em www1.sap.sp.gov.br/dados-abertos
- **Link:** https://www1.sap.sp.gov.br/dados-abertos/dados-estatisticos-populacao-prisional-geral_1-sem-2025.pdf
- **Justificativa de escolha:** é a fonte real mais detalhada encontrada para caracterizar o perfil da população carcerária do estado-piloto, fornecendo os atributos (regime, tipo penal, faixa etária) que serão usados como features no modelo de risco de reincidência.

## 7. Caracterização da população prisional geral — Cadernos de Saúde Pública

- **Mantenedor:** artigo peer-reviewed publicado em *Cadernos de Saúde Pública* (2023), com base em dados oficiais do INFOPEN/DEPEN
- **Descrição:** série histórica nacional (2007–2019) de população prisional e razão pessoas privadas de liberdade por vaga.
- **Granularidade:** nacional, anual
- **Periodicidade:** dado histórico consolidado (não atualizado)
- **Formato de acesso:** tabela do artigo, acessível publicamente
- **Link:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10552813/table/t1
- **Justificativa de escolha:** fonte acadêmica com revisão por pares que já consolida e calcula a razão pessoas/vaga ano a ano a partir do INFOPEN, servindo de série histórica nacional de referência para contextualizar a evolução da superlotação antes da ingestão da base bruta completa.

---

## Síntese da escolha do estado-piloto

São Paulo foi escolhido como piloto por reunir, simultaneamente: (i) o maior sistema prisional do país; (ii) publicação de dados por unidade com frequência diária (SAP-SP), rara entre os estados; e (iii) cobertura no InfoPen e no BNMP suficiente para cruzamento com as demais fontes nacionais. Essa combinação reduz o risco de o projeto ficar limitado pela baixa frequência de atualização das bases federais.
