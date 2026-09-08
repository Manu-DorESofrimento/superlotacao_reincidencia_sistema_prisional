# Backlog Priorizado — Histórias de Usuário e Casos de Uso

Projeto: Painel de Projeção de Capacidade Prisional e Reincidência (PCPR)

---

## 1. Backlog priorizado (histórias de usuário)

Prioridade MoSCoW: **Must** (essencial) · **Should** (importante) · **Could** (desejável).

| ID | Épico | Prioridade | História de usuário |
|---|---|---|---|
| HU01 | Dados | Must | Como analista de dados, quero baixar e consolidar as séries do InfoPen por unidade prisional, para ter capacidade e população histórica confiáveis. |
| HU02 | Dados | Must | Como analista de dados, quero extrair os dados do BNMP sobre entradas, saídas e regime, para construir o fluxo carcerário. |
| HU03 | Dados | Must | Como analista de dados, quero coletar diariamente os dados de capacidade e população por unidade da SAP-SP, para validar as projeções com dados quase em tempo real. |
| HU04 | Dados | Should | Como analista de dados, quero cruzar cada unidade prisional com o município/UF via IBGE, para dar contexto geográfico ao painel. |
| HU05 | Dados | Must | Como analista de dados, quero documentar a qualidade e completude de cada fonte, para justificar decisões de modelagem. |
| HU06 | Dados | Could | Como analista de dados, quero automatizar a atualização periódica das bases, para reduzir trabalho manual em sprints futuras. |
| HU07 | Ocupação | Must | Como gestor penitenciário, quero visualizar a série histórica de ocupação vs. capacidade por unidade, para entender a magnitude do problema atual. |
| HU08 | Ocupação | Must | Como analista de dados, quero construir um modelo de série temporal por unidade, para projetar a ocupação nos próximos 6–12 meses. |
| HU09 | Ocupação | Should | Como gestor penitenciário, quero receber um alerta quando a projeção ultrapassar um limiar crítico de ocupação, para agir antes da crise. |
| HU10 | Reincidência | Must | Como analista de dados, quero definir com clareza a janela de observação e o critério de reincidência, para que a métrica seja auditável. |
| HU11 | Reincidência | Must | Como analista de dados, quero treinar um modelo de risco de reincidência agregado por perfil, para apoiar a priorização de programas de ressocialização. |
| HU12 | Reincidência | Must | Como responsável ético do projeto, quero documentar limitações e possíveis vieses do modelo, para evitar uso indevido em decisões individuais. |
| HU13 | Painel | Must | Como gestor penitenciário, quero um painel único com ocupação projetada e risco agregado de reincidência, para embasar minhas decisões. |
| HU14 | Painel | Should | Como gestor penitenciário, quero filtrar o painel por unidade, regime e período, para investigar cenários específicos. |
| HU15 | Validação | Must | Como responsável pelo projeto, quero validar os resultados com pelo menos um gestor ou pesquisador da área, para checar a utilidade prática do modelo. |

---

## 2. Casos de uso

### UC01 — Consultar ocupação projetada de uma unidade prisional
- **Atores:** Gestor da Secretaria de Administração Penitenciária (ator principal); Analista de dados (ator de apoio).
- **Pré-condições:** modelo de projeção de ocupação treinado e disponível no painel; unidade prisional cadastrada na base.
- **Fluxo principal:**
  1. O gestor acessa o painel PCPR.
  2. O gestor seleciona a unidade prisional de interesse.
  3. O sistema exibe a série histórica de ocupação e a projeção para os próximos 6–12 meses, com intervalo de confiança.
  4. O sistema destaca, com alerta visual, se a projeção ultrapassa o limiar crítico definido (ex.: 150% da capacidade).
- **Fluxos alternativos:** se a unidade não tiver histórico suficiente para projeção confiável, o sistema exibe apenas os dados históricos disponíveis e um aviso de dados insuficientes.
- **Pós-condições:** o gestor obtém subsídio para decidir sobre transferência de custodiados ou priorização de mutirão carcerário.

### UC02 — Consultar risco agregado de reincidência por perfil
- **Atores:** Gestor de programas de ressocialização (ator principal).
- **Pré-condições:** modelo de risco de reincidência treinado; features agregadas por perfil (regime, tipo penal, faixa etária, unidade) disponíveis.
- **Fluxo principal:**
  1. O gestor acessa a aba de reincidência do painel.
  2. O gestor filtra por regime e/ou unidade prisional.
  3. O sistema exibe a taxa de reincidência estimada por perfil agregado, nunca em nível individual.
  4. O gestor identifica os perfis/unidades prioritários para alocação de programas de ressocialização.
- **Fluxos alternativos:** se o filtro selecionado resultar em um grupo pequeno demais para preservar o caráter agregado (ex.: menos de N pessoas), o sistema bloqueia a exibição e exige um filtro mais amplo.
- **Pós-condições:** direcionamento de recursos de ressocialização baseado em evidência, sem uso do modelo para decisão sobre pessoa específica.

### UC03 — Atualizar as bases de dados do projeto
- **Atores:** Analista de dados (ator principal).
- **Pré-condições:** acesso às fontes (InfoPen, BNMP, SAP-SP, IBGE) configurado.
- **Fluxo principal:**
  1. O analista executa os scripts de ingestão para cada fonte.
  2. O sistema valida a completude e o formato dos dados recebidos.
  3. O analista registra a extração no dicionário de dados (fonte, data, observações de qualidade).
  4. As bases processadas ficam disponíveis para os modelos de ocupação e reincidência.
- **Fluxos alternativos:** se uma fonte estiver indisponível ou o layout tiver mudado, o sistema registra erro e mantém a última versão válida das bases.
- **Pós-condições:** bases atualizadas e documentadas, prontas para re-treino dos modelos.

### UC04 — Validar o modelo com um gestor ou pesquisador da área
- **Atores:** Responsável pelo projeto (ator principal); Gestor público ou pesquisador convidado (ator de apoio).
- **Pré-condições:** painel funcional com projeções de ocupação e risco de reincidência geradas para o estado-piloto.
- **Fluxo principal:**
  1. O responsável apresenta o painel e a metodologia ao convidado.
  2. O convidado avalia se as projeções e alertas fazem sentido frente à realidade operacional conhecida.
  3. O convidado aponta divergências ou lacunas percebidas.
  4. O responsável registra os ajustes necessários no backlog.
- **Pós-condições:** validação qualitativa documentada, usada como critério de sucesso do projeto.

### UC05 — Auditar uma decisão de modelagem sensível
- **Atores:** Membro da equipe (ator principal); Revisor externo ao time técnico (ator de apoio).
- **Pré-condições:** decisão de modelagem envolvendo atributo potencialmente sensível ou mudança na definição de reincidência.
- **Fluxo principal:**
  1. O membro da equipe registra a decisão em um ADR (Architecture/Analysis Decision Record).
  2. O ADR descreve contexto, decisão, justificativa e consequências.
  3. Um revisor externo ao time técnico avalia o ADR antes da decisão entrar em produção.
- **Pós-condições:** toda decisão sensível fica documentada e rastreável, alinhada aos limites éticos definidos para o projeto.
