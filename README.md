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
    <li>Listar todos os itens de uma modalidade em um período ordenados por data
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
</div>

> Obs: o retorno de cada requisição deve ser um JSON válido.

<h5>Parte 3. Desenvolver cache interno</h5>

<div align="justify">
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
<h3>Requisitos</h3>
<p>Requisitos necessários para a instalação e execução do projeto.</p>
<ul>
<li>Python 3.8.3</li>
<li>Virtualenv 20.0.25</li>
</ul>
<h4>Instalação</h4>

> **_NOTA:_** Repositório privado

```console
git clone https://github.com/gabrielhjs/Laura_teste.git
git cd Laura_teste
```

> **_NOTA:_** Crie uma máquina virtual

```console
pip install -r requirements/development.txt
```

<h4>Execução</h4>

```console
python server.py
```

<h4>Banco de dados</h4>
<p>A estrutura do banco de dados contém uma Collection chamada "students"
que contém todos os dados da aplicação. O ra de cada estudante é
único. Os cursos de cada estudante são armazenados na lista "courses".
</p>
<p>Formato dos dados:</p>

```json
{
    "_id": {
        "$oid": "5f2e278ffb12be63b5a3f3e8"
    },
    "name": "GABRIEL SÁ",
    "age": 24,
    "ra": 8740.0,
    "courses": [
        {
            "campus": "TL",
            "county": "Três Lagoas",
            "course": "TÉCNICO EM ELETROTÉCNICA",
            "modality": "PRESENCIAL",
            "level": "INTEGRADO",
            "start_date": {
                "$date": 1430524800000
            }
        },
        {
            "campus": "TL",
            "county": "Três Lagoas",
            "course": "ELETRÔNICA",
            "modality": "PRESENCIAL",
            "level": ".FICCAMPUS",
            "start_date": {
                "$date": 1480809600000
            }
        },
        {
            "campus": "AQ",
            "county": "Aquidauana",
            "course": "TÉCNICO EM INFORMÁTICA",
            "modality": "PRESENCIAL",
            "level": "SUBSEQUENTE",
            "start_date": {
                "$date": 1596844800000
            }
        }
    ]
}
```

<h4>Endpoints</h4>

##### 1. Busca por cursos de uma modalidade: `GET /api/school/modality/<modalidade>/<data inicial>/<data final>/`
<p>Exemplo de resultado:</p>

`GET /api/school/modality/PRESENCIAL/2015-07-27/2015-07-27/`

```json
[
    {
        "name": "ADALTO SEBASTIAO DA SILVA JUNIOR",
        "age": 18.0,
        "ra": 8570.0,
        "courses": {
            "campus": "AQ",
            "county": "Aquidauana",
            "course": "TÉCNICO EM INFORMÁTICA",
            "modality": "PRESENCIAL",
            "level": "SUBSEQUENTE",
            "start_date": {
                "$date": 1437955200000
            }
        }
    },
    {
        "name": "ADRIANO COSTA BISPO DOS SANTOS",
        "age": 29.0,
        "ra": 13463.0,
        "courses": {
            "campus": "AQ",
            "county": "Aquidauana",
            "course": "TÉCNICO EM INFORMÁTICA",
            "modality": "PRESENCIAL",
            "level": "SUBSEQUENTE",
            "start_date": {
                "$date": 1437955200000
            }
        }
    },
    {
        "name": "ALINE MARIE RONDON TOSCANO DE BRITO GOMES",
        "age": 17.0,
        "ra": 6891.0,
        "courses": {
            "campus": "AQ",
            "county": "Aquidauana",
            "course": "DESENHISTA DE MÓVEIS",
            "modality": "PRESENCIAL",
            "level": ".FIC",
            "start_date": {
                "$date": 1437955200000
            }
        }
    },
    {
        "name": "ANA AUGUSTA VICTORIO FLORES",
        "age": 41.0,
        "ra": 13468.0,
        "courses": {
            "campus": "AQ",
            "county": "Aquidauana",
            "course": "TÉCNICO EM INFORMÁTICA",
            "modality": "PRESENCIAL",
            "level": "SUBSEQUENTE",
            "start_date": {
                "$date": 1437955200000
            }
        }
    },
   "continua..."
]
```

##### 2. Busca todos os cursos de um campus: `GET /api/school/campus/<campus>/`
<p>Exemplo de resultado:</p>

`GET /api/school/campus/tl/`

```json
[
    {
        "_id": "TL",
        "courses": "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"
    },
    {
        "_id": "TL",
        "courses": "AUTOMAÇÃO INDUSTRIAL"
    },
    {
        "_id": "TL",
        "courses": "ELETRÔNICA"
    },
    {
        "_id": "TL",
        "courses": "ESPANHOL BÁSICO"
    },
    {
        "_id": "TL",
        "courses": "ESPECIALIZAÇÃO EM DOCÊNCIA PARA A EDUCAÇÃO PROFISSIONAL, CIENTÍFICA E TECNOLÓGICA"
    },
    {
        "_id": "TL",
        "courses": "GRUPO DE ROBÓTICA"
    },
    {
        "_id": "TL",
        "courses": "INGLÊS BÁSICO"
    },
    {
        "_id": "TL",
        "courses": "OPERADOR DE COMPUTADOR"
    },
    {
        "_id": "TL",
        "courses": "SISTEMAS PARA INTERNET"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM ADMINISTRAÇÃO"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM AGENTE COMUNITÁRIO DE SAÚDE"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM AUTOMAÇÃO INDUSTRIAL"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM EDIFICAÇÕES"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM ELETROTÉCNICA"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM INFORMÁTICA"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM MANUTENÇÃO E SUPORTE EM INFORMÁTICA"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM REABILITAÇÃO DE DEPENDENTES QUÍMICOS"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM SERVIÇOS PÚBLICOS"
    },
    {
        "_id": "TL",
        "courses": "TÉCNICO EM TRANSAÇÕES IMOBILIÁRIAS"
    },
    {
        "_id": "TL",
        "courses": "VENDEDOR"
    }
]
```

##### 3. Busca pela quantidade de alunos em um campus em um período: `GET /api/school/campus/students/<campus>/<data inicial>/<data final>/`
<p>Exemplo de resultado:</p>

`GET /api/school/campus/students/tl/1015-07-27/3015-07-27/`

```json
[
    {
        "_id": "TL",
        "count": 836
    }
]
```

##### 4. Cadastro de aluno: `POST /api/school/student/new/`

> Obs: Caso o ra do aluno já exista no banco de dados, os dados serão
> atualizados e o curso será adicionado. Caso contrário, o aluno será
> cadastrado no banco com o curso inserido.

<p>Sucesso:</p>

```json
{
    "message": "Operation performed successfully",
    "status": "success"
}
```
<p>Erro:</p>

```json
[
    {
        "error": "This field is required.",
        "field": "ra"
    }
]
```

##### 5. Busca por dados de um aluno: `GET /api/school/student/<ra>/`
<p>Exemplo de resultado:</p>

`GET /api/school/student/19023/`

```json
{
    "_id": {
        "$oid": "5f2e278ffb12be63b5a3d7fe"
    },
    "name": "ADRIANA TEIXEIRA SERRA",
    "age": 20.0,
    "ra": 19023.0,
    "courses": [
        {
            "campus": "AQ",
            "county": "0",
            "course": "OPERADOR DE COMPUTADOR",
            "modality": "EAD",
            "level": ".FIC",
            "start_date": {
                "$date": 1465516800000
            }
        }
    ]
}
```

##### 6. Remover curso de aluno e/ou aluno: `POST /api/school/student/delete/`

> Obs: Caso o ra do estudante buscado tenha apenas o curso buscado o aluno será
> deletado do banco de dados. Caso contrário, apenas o curso será deletado
> da lista de cursos do aluno.

<p>Sucesso:</p>

```json
{
    "message": "Operation performed successfully",
    "status": "success"
}
```
<p>Erro:</p>

```json
{
    "message": "Data not found",
    "status": "error"
}
```

</div>