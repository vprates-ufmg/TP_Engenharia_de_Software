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
    python3 db/load_classes_from_csv.py db/classes.csv
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

## Como usuário, gostaria de acessar a página inicial do site
### Tarefas
- Criar o template base da página inicial. [Lucas]
- Criar rotas básicas do Flask para o uso do template. [Victor]
- Implementar um formulário com caixa de texto básica que envia dados para uma api interna. [Matheus]
- Implementar a api interna e guardar os dados no MongoDB como teste. [Michel]
  
## Como usuário, gostaria de criar um perfil anônimo
### Tarefas
- Criação da arte da página de login/registro. [Lucas]
- Implementação do template usado para a página de login/registro. [Matheus]
- Criação da coleção do MongoDB que representa os usuários. [Michel]
- Criação do usuário com os dados fornecidos e senha segura. [Michel]
- Implementação de cookies para salvar a sessão do usuário. [Victor]
  
## Como usuário, gostaria de avaliar anonimamente um professor que ministrou uma matéria
### Tarefas 
- Criar a coleção representando a publicação no banco de dados. [Michel]
- Verificar as matérias ministradas e os professores que ministrou nos últimos 3 semestres a partir de dados disponibilizados no SIGA. [Michel]
- Fazer a arte da página com o formulário com a caixa de texto da avaliação. [Lucas]
- Fazer o template da página com o formulário com a caixa de texto da avaliação. [Matheus]
- Testar uma chamada para a API com o conteúdo da avaliação. [Victor]
- Anonimizar a publicação. [Victor]
  
## Como usuário, gostaria de encontrar facilmente avaliações existentes de acordo com um critério meu
### Tarefa 
- Implementar rota da API que retorna as avaliações que condizem com o filtro, e ordenado da maneira desejada. [Michel]
- Criar arte da interface de ordenação. [Lucas]
- Implementar a interface de ordenação. [Matheus]
  
## Como usuário, gostaria de marcar uma avaliação anônima como relevante ou não relevante
### Tarefas 
- Criar arte dos botões de vote nas avaliações. [Lucas]
- Implementar os botões de upvote nas publicações. [Matheus]
- Adicionar saldo de upvotes às publicações no banco de dados. [Michel]
- Adicionar vote como uma das possibilidades de ordenação das avaliações. [Victor]
  
  
  
# Histórias do Backlog  
- Como usuário, eu gostaria de criar perfil e fazer login por plataformas externas (Twitter, Facbeook, etc..)  
- Como usuário, eu gostaria de adicionar anexos às avaliações (fotos, vídeos, documentos PDF)  
- Como usuário, eu gostaria de editar minhas avaliações.  
- Como usuário, eu gostaria de adicionar comentários nas avaliações.  
- Como usuário, eu gostaria de reportar avaliações que abusam do sistema.  
- Como usuário, eu gostaria de formatar as minhas avaliações usando Markdown.
- Como usuário, eu gostaria de adicionar prêmios a uma avaliação específica (como um superlike)  
- Como usuário, eu gostaria de compartilhar avaliações específicas com outras redes sociais  
- Como usuário, eu gostaria de acessar o site em uma plataforma mobile (celulares, tablets)
- Como usuário, eu gostaria de ajudar o projeto por meio de doações.
- Como usuário, eu gostaria de acessar o site por um app mobile disponível na Play Store.
- Como usuário, eu gostaria de deletar minha conta, dados e publicações do site.
- Como administrador, eu gostaria de apagar posts de qualquer usuário
- Como administrador, eu gostaria de banir um usuário