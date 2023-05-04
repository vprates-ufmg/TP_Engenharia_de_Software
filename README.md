# TP_Engenharia_de_Software
## Escopo do Sistema

Visamos criar um site que torna possível os alunos avaliarem os professores.
1. Criação de Perfil
2. Login do aluno
3. Ver avaliações prévias de cada professor, geral e por matéria ministrada
4. Escrever uma avaliação (anônima ou se identificando)
5. Sistema de upvote com ordenação das avaliações

## Membros da Equipe e Papel
### Frontend
- Lucas Emanuel Elias Alves
- Matheus Flavio Goncalves Silva

### Backend
- Michel Barros da Fonseca
- Victor Prates Figueiredo

## Tecnologias
- Quart
- React
- MongoDB

# Instalação
```bash
    git clone https://github.com/vprates-ufmg/TP_Engenharia_de_Software
    cd TP_Engenharia_de_Software

    ## configure o backend
    cd backend
    python3 -m pip install -r requirements.txt
    cp .env_example .env
    ## instale o mongodb, configure e coloque as credenciais
    nano .env
    cd ..

    ## configure o frontend
    cd frontend
    [...]
    cd ..

    ## abra os servidores
    ./start.sh # localmente
    ./start.sh --production #em produção
```

# Formatação do código
```bash
    ## backend
    cd backend
    find . -name '*.py' -print0 | xargs -0 python3 -m black --line-length=120
    cd ..

    ## frontend
    [...]
```

## Design do Front-End
Link do Figma com o desing das páginas
<br>
<a href="https://www.figma.com/file/6ZZET6D42xeVovtNnFhwm3/TP1_Eng_Soft?type=design&node-id=0%3A1&t=GMHt6m7Ct4FRkFFp-1">Figma Review De Profs</a>

# Histórias da sprint  
  
## Criação da página inicial  
### Tarefas
-  Configurar base de arquivos projeto.
- Criar rotas básicas do Flask para o uso dos templates.
- Implementar caixa de texto básica que envia dados para uma api interna.
  
## Criação de perfil de usuário  
### Tarefas
-  Criação da arte e página da página de login/registro.
- Criação da coleção do MongoDB que representa os usuários.
- Criação do usuário com os dados fornecidos e senha segura.
- Implementação de cookies para salvar a sessão do usuário.
  
## Escrever uma avaliação de professor que ministrou uma máteria em um período específico  
### Tarefas 
-  Criar a coleção representando a publicação no banco de dados.
- Verificar as matérias ministradas e os professores que ministrou nos últimos 3 semestres a partir de dados disponibilizados no SIGA.
-  Fazer a arte da página inicial com a caixa de texto.
- Testar uma chamada para a API com o conteúdo da avaliação.
- Anonimizar a publicação.
  
## Sistema de ordenação de avaliações  
### Tarefa 
-  Implementar rota da API que retorna as avaliações que condizem com o filtro, e ordenado da maneira desejada.
- Criar arte da interface de ordenação.
- Implementar a interface de ordenação.
  
## Sistema de relevância de avaliações (upvote/downvote)  
### Tarefas 
-  Criar arte dos botões de vote nas avaliações.
- Implementar o conceito nas publicações.
- Adicionar saldo de upvotes às publicações no banco de dados.
- Adicionar vote como uma das possibilidades de ordenação das avaliações.
  
  
  
# Histórias do Backlog  
- Criação de perfil e login por plataformas externas (Twitter, Facbeook, etc..)  
- Suporte a anexos nas avaliações (fotos, vídeos, documentos PDF)  
- Suporte à edição de avaliações.  
- Suporte a comentários nas avaliações.  
- Suporte a moderação de avaliações (evitar trolls)  
- Suporte à formatação de avaliações em Markdown.  
- Adicionar prêmios que podem ser dados a uma avaliação específica (como um superlike)  
- Suporte a compartilhamento de avaliações específicas para outras redes sociais  
- Adicionar suporte a plataformas mobile (web browser)  
- Adicionar suporte a doação para o projeto.  
- Acesso via um app mobile disponível na Play Store .
- Possibilidade de deletar a conta de usuário.
