<h1 align="center">
  Processo seletivo backend 2019 - Teste prático
</h1>
<h6 align="center">
  <a href="#Teste">Teste</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Documentação">Documentação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Candidato">Candidato</a>
</h6>
<br>

## Teste

<div align="justify">
<p>
O objetivo deste teste é avaliar o seu conhecimento técnico em relação às ferramentas
utilizadas no backend da Laura. Os serviços do sistema tem sua comunicação majoritariamente
baseada em APIs, desenvolvidas utilizando frameworks e micro frameworks. A comunicação e a
arquitetura do banco de dados também são pontos importantes para questões de performance e
escalabilidade.
</p>
<p>
Neste teste, solicitamos que você defina uma arquitetura para as collections de um banco
MongoDB e crie uma aplicação em python com API para gerenciamento dos dados nele presente.
Lembre-se de seguir as melhores práticas de desenvolvimento.
</p>
<p>
Ainda que, por qualquer motivo, você não consiga completar este teste, recomendamos que
ainda assim nos encaminhe o que foi desenvolvido. A falta de cumprimento de alguns dos requisitos
aqui descritos não implica necessariamente na desconsideração do candidato. Em caso de dúvidas
não hesite em entrar em contato.
</p>
<h5>Parte 1. Importar dados de “dataset_estudantes.csv” para o banco de dados</h5>
<p>
Utilizando a biblioteca pymongo, crie uma base de dados e uma collection, bem como os
indíces que achar pertinente, contendo os dados do arquivo “dataset_estudantes.csv”. As credenciais
da conexão do banco (host, porta, etc) e o nome da base de dados e da collection deverão ser lidas
de variáveis de ambiente. O formato dos dados no banco de dados fica a seu critério, bem como o
nome das variáveis de ambiente. O código gerado deverá estar em um arquivo import_data.py.
Também solicitamos que nos seja enviado um exemplo do arquivo contendo as variáveis de
ambiente como o nome env_file.env (solicitamos esse arquivo apenas para referência, podendo
inclusive ser o que você usou localmente para testar).
</p>
<h5>Parte 2. Criar uma aplicação python com pymongo e Flask</h5>
<p>
A seguir são listados algumas definições a respeito dos endpoints que devem estar presentes
na aplicação. Além do código, você também será responsável por definir o tipo de requisição HTTP
de cada um dos endpoints (com exceção do primeiro), bem como seus status de retorno. O código
da aplicação deverá estar em arquivo de nome server.py. Na aplicação, a API deve ser feita da
seguinte maneira:
</p>
<ol>
    <li>Listar todos os itens de uma modalidade em um período ordenados por data - [x]
    <ol type="a">
        <li>Tipo da requisição: GET</li>
        <li>Parâmetros: modalidade, data de início e data de fim</li>
        <li>Retorno: lista de todos os itens com modalidade, filtrando pelo período
        passado e ordenando de forma decrescente pela data dos
        documentos.</li>
    </ol>
    </li>
    <li>Listar todos os cursos de um campus
    <ol type="a">
        <li>Tipo da requisição: [a definir]</li>
        <li>Parâmetros: campus</li>
        <li>Retorno: lista de cursos do campus</li>
    </ol>
    </li>
    <li>Descobrir número total de alunos num campus em um dado período
    <ol type="a">
        <li>Tipo de requisição: [a definir]</li>
        <li>Parâmetros: campus, data de início e data de fim</li>
        <li>Retorno: número de alunos do campus no período</li>
    </ol>
    </li>
    <li>Cadastrar alunos
    <ol type="a">
        <li>Tipo da requisição: [a definir]</li>
        <li>Parâmetros: nome, idade_ate_31_12_2016, ra, campus, município, curso, modalidade, nivel_do_curso, data_inicio</li>
        <li>Retorno: sucesso/erro</li>
    </ol>
    </li>
    <li>Buscar aluno
    <ol type="a">
        <li>Tipo da requisição: [a definir]</li>
        <li>Parâmetro: ra</li>
        <li>Retorno: todos os dados do aluno</li>
    </ol>
    </li>
    <li>Remover aluno do banco
    <ol type="a">
        <li>Tipo da requisição: [a definir]</li>
        <li>Parâmetros: ra, campus</li>
        <li>Retorno: sucesso/erro</li>
    </ol>
    </li>
</ol>

> Obs: o retorno de cada requisição deve ser um JSON válido.

<h5>Parte 3. Desenvolver cache interno</h5>
<p>
Desenvolver um cache simples, em memória, para que não seja necessária uma nova
consulta no banco de dados para os alunos recém-acessados. O cache deverá conter no MÁXIMO
10 itens (ou seja, dados de no máximo 10 alunos). O cache também deverá levar em conta dados
recém-cadastrados. Exemplos de comportamento do cache:
</p>
<ol>
<li>O endpoint 5 (Buscar aluno) busca por aluno de ra 123. Em seguida, o mesmo endpoint é
acessado também para o aluno de ra 123. Como esse dado já havia sido buscado no banco
recentemente, a aplicação não deve fazer uma nova leitura no banco mas sim ler do cache;</li>
<li>O endpoint 4 (Cadastrar aluno) registra aluno de ra 321. Em seguida o endoint 5 (Buscar aluno) é
acessado para o aluno de 321. Como esse aluno acabou de ser registrado, a aplicação não deve fazer
nova leitura no banco mas sim ler do cache.</li>
</ol>
<p>
O critério de evasão (momento em que um dado deve ser removido da cache para dar lugar a
outro mais recente) fica por sua conta.
</p>
<h5>Parte 4: Documentação da APIs</h5>
<p>Desenvolva alguma forma de documentação das APIs.</p>
<p>Links para referência:</p>

- [Virtual Env](https://virtualenv.pypa.io/en/stable/userguide/#usage)
- [Flask Docs](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application)
- [Mongo API](https://api.mongodb.com/python/current/tutorial.html)
- [Mongo Docs](https://docs.mongodb.com/manual/tutorial/manage-indexes/)
</div>

## Documentação

<div align="justify">
<h5>Requisitos</h5>
<p>Requisitos necessários para a instalação e execução do projeto.</p>
<ul>
<li>Python 3.8.3</li>
<li>Virtualenv 20.0.25</li>
</ul>
<h5>Instalação</h5>

> **_NOTA:_** Repositório privado

```console
git clone https://github.com/gabrielhjs/Laura_teste.git
git cd Laura_teste
```

> **_NOTA:_** Crie uma máquina virtual

```console
pip install -r requirements/development.txt
```

<h5>Execução</h5>

```console
python server.py
```

<h5>Banco de dados</h5>
<h5>Endpoints</h5>

</div>