# lcd-fit-gym-management

Projeto da cadeira de **Programação** (1º ano, 1º semestre, Ciência de Dados, ISCTE). Aplicação de consola em Python para gerir um ginásio, o **LCD Fit**: membros, aulas, entradas e subscrições.

## Funcionalidades
- **Membros**: criar e identificar membros, comprar entradas e ativar ou desativar a subscrição.
- **Aulas**: criar aulas com instrutor e lotação, inscrever e remover membros.
- **Menu de gestão**: adicionar membros e aulas, pesquisar com filtros.
- **Menu do membro**: ver e gerir as próprias entradas e inscrições.
- **Persistência**: exportar e importar o estado do ginásio para ficheiro de texto.

O código usa programação orientada a objetos, com as classes `Membro`, `Aula` e `Gym`.

## Como executar
Requer Python 3.

```bash
python 1º_Projeto.py
```

Para carregar dados de exemplo, importa o ficheiro `gym.txt` a partir do menu principal.

## Ficheiros
- `1º_Projeto.py` – código da aplicação
- `gym.txt` – dados de exemplo (membros e aulas)
- `projeto_programacao.zip` – cópia do projeto entregue
