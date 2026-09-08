# Kanban do Projeto — Atualizado na Sprint 2 (MVP Analítico)

Estimativas em **story points** (escala Fibonacci: 1, 2, 3, 5, 8, 13), registradas no momento em que cada cartão entrou em "A Fazer".

## Quadro

| Backlog | A Fazer | Em Andamento | Em Revisão | Concluído |
|---|---|---|---|---|
| Ingestão automatizada completa InfoPen/BNMP — 8 pts | — | — | — | Confirmar estado-piloto (SP) — 2 pts |
| Modelo de reincidência com dados reais do BNMP — 13 pts | | | | Levantar datasets públicos com justificativa — 3 pts |
| Modelo de série temporal robusto (SARIMA/Prophet) — 8 pts | | | | Notebook de EDA (dados reais) — 5 pts |
| Painel interativo (Streamlit) — 8 pts | | | | Backlog priorizado + casos de uso — 3 pts |
| Validação com gestor/pesquisador da área — 3 pts | | | | Artigo científico: fundamentação, trabalhos relacionados, metodologia (Sprint 1) — 8 pts |
| Testar modelo de filas (M/M/c) — 5 pts | | | | Pré-processamento e engenharia de atributos — 5 pts |
| Filtros por unidade/regime/período no painel — 3 pts | | | | Notebook de treinamento e comparação de baselines — 8 pts |
| Exportação de relatório em PDF do painel — 2 pts | | | | Exportar modelos treinados (joblib) — 2 pts |
| | | | | Atualizar Kanban com estimativas ágeis — 1 pt |
| | | | | Artigo científico: metodologia detalhada, dados, pré-processamento, modelos e métricas (Sprint 2) — 5 pts |

## Registro de estimativas ágeis por sprint

| Sprint | Pontos planejados | Pontos concluídos | Observação |
|---|---|---|---|
| Sprint 1 — Conhecendo os Dados | 21 pts | 21 pts | 100% do planejado entregue; nenhum item retido no backlog desta sprint. |
| Sprint 2 — MVP Analítico | 21 pts | 21 pts | 100% do planejado entregue. Modelos treinados são um MVP sobre amostra pequena (ver artigo científico, Seção 8) — não representam a versão final. |
| Backlog futuro (Sprint 3+) | 50 pts | — | Ainda não estimado por sprint; prioridade principal é a ingestão automatizada completa (8 pts), pré-requisito para o modelo de reincidência (13 pts) e para um modelo de série temporal mais robusto (8 pts). |

## Notas sobre as estimativas

- As estimativas foram feitas por analogia com os cartões já concluídos na Sprint 1 (ex.: um notebook de EDA levou 5 pts; o notebook de treinamento e comparação de modelos, por envolver mais decisões de modelagem, foi estimado em 8 pts e essa estimativa se confirmou na prática).
- O cartão "Modelo de reincidência com dados reais do BNMP" recebeu a maior estimativa (13 pts) por depender de uma fonte de dados individual ainda não obtida (acesso ao BNMP), o que introduz incerteza adicional além do esforço técnico de modelagem em si.
- Cartões de UI do painel (filtros, exportação) foram estimados com pontuação baixa (2–3 pts) por serem tarefas de implementação bem delimitadas, sem incerteza de dados envolvida.
