# 📊 Automação de Vendas e Análise Regional com Python

Este projeto consiste numa solução automatizada desenvolvida em **Python** para processamento, tratamento e segmentação de dados de vendas descentralizados (*Superstore Sales*), gerando ficheiros regionais isolados e relatórios visuais executivos de alto impacto.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python 3.x**
* **Pandas**: Limpeza de dados, manipulação de datas, agregações e exportação.
* **Matplotlib**: Geração de gráficos estatísticos e relatórios visuais.
* **Glob & OS**: Mapeamento dinâmico do sistema de arquivos e manipulação de caminhos.
* **Git & GitHub**: Versionamento de código e controlo de repositório.

---

## 🚀 Funcionalidades da Aplicação

- [x] **Tratamento Global de Dados**: Conversão e padronização de datas (`dayfirst=True`), arredondamento financeiro e cálculo do tempo de envio das encomendas.
- [x] **Segregação Regional Automatizada**: Filtragem e exportação dinâmica de ficheiros `.csv` para cada região (*Central*, *East*, *South*, *West*).
- [x] **Leitura em Lote Dinâmica**: Mapeamento dinâmico de novos ficheiros com `glob` e armazenamento estruturado num dicionário de DataFrames.
- [x] **Geração de Relatórios Visuais**: Exportação automática de gráficos de alto desempenho em `.png` para suporte à tomada de decisão.

---

## 💻 Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/FelipeRFN/automacao-vendas-python.git](https://github.com/FelipeRFN/automacao-vendas-python.git)
   cd automacao-vendas-python