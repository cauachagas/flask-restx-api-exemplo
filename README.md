# Iniciando com Flask-RESTX Framework

Flask-RESTX é uma extensão para Flask que adiciona suporte para construir APIs REST rapidamente. Flask-RESTX incentiva as melhores práticas com configuração mínima. Se você está familiarizado com o Flask, o Flask-RESTX deve ser fácil de aprender. Ele fornece uma coleção coerente de decoradores e ferramentas para descrever sua API e expor sua documentação corretamente (usando Swagger).[<sup>1</sup>](#1)

## Primeiros passos

O ideal é criar um ambiente de desenvolvimento virtual para rodar o projeto. Geralmente, recomendam o uso do `virtualenv`. Caso queira fazer deploy de uma aplicação Flask no Heroku é melhor usar uma versão `3.6 >= 3.6.x <= 3.6.13` do Python, que pode ser facilmente instalado pelo `miniconda/anaconda`.

Nesse [link](https://github.com/cauachagas/cling-torch#passo-1---instalando-miniconda) mostro como instalar o miniconda e criar um ambiente de desenvolvimento.

## Como rodar o projeto

1. Clone o repositório;
2. Crie um ambiente de desenvolvimento;
3. Ative o ambiente do passo anterior;
4. Instale as dependências;
5. Inicie o servidor.

Caso use o `miniconda/anaconda` e tenha os scripts `conda` e `activate` no `$PATH` então o passos serão esses

```bash
git clone https://github.com/cauachagas/flask-restx-api-exemplo
cd flask-restx-api-exemplo
conda env create -f environment.yml
source activate flask-restx
python main.py
```

Em seguida abra o link http://127.0.0.1:5000/ no seu navegador.

![](https://media.giphy.com/media/XCKRBs6sXIO0JprpJh/giphy.gif)

## Deploy na Vercel e Serverless Functions

Vercel é uma plataforma em nuvem para **sites estáticos** (Jamstack) e **Serverless Functions** que se adapta perfeitamente ao seu fluxo de trabalho. Ele permite que os desenvolvedores hospedem sites e serviços da web com **deploys instantâneos**,  **escalados automaticamente** e não requer supervisão, tudo sem configuração.

A Vercel é o responsável pelo incrível [Next.js](https://nextjs.org/).

### Deploy através de um repositório

No respositório deve exister

1. Um arquivo `requirements.txt` com as dependências do projeto;
2. Um arquivo python que rode a aplicação (aqui foi usado `main.py`);
3. Um arquivo `vercel.json` ([ver aqui](https://raw.githubusercontent.com/cauachagas/flask-restx-api-exemplo/master/vercel.json)) que aponte para o arquivo python que roda a aplicação

Caso você tenha feito um fork desse repositório basta fazer o seguinte para ter sua aplicação rodando na Vercel:

1. Criar uma conta na [Vercel](https://vercel.com)
2. Criar um novo projeto na sua conta Vercel
3. Importar projeto de seu repositório Git
4. Iniciar o deploy sem mexer em qualquer configuração

![](https://media.giphy.com/media/N6sXwYAHOYZQa75MFa/giphy.gif)

### Deploy feito localmente

Também é possível fazer o deploy a partir de sua máquina. Para isso será preciso

1. Instalar `Node.js` (Se estiver usando conda, basta digitar `conda install nodejs`). 
2. Instalar o Vercel CLI `npm i -g vercel`. 
   - **OBS**: Estou considerando que o arquivo python que roda a aplicação seja `main.py` e que ele está na raiz do projeto
3. Criar um arquivo `vercel.json` na raiz do projeto com as informações contidas [aqui](https://raw.githubusercontent.com/cauachagas/flask-restx-api-exemplo/master/vercel.json)


Após isso, basta usar o comando 

```bash
vercel --prod
```

para fazer o deploy.


Usando a estrutura deste repositório, ficou assim:

```bash
vercel --prod
Vercel CLI 21.3.3
? Set up and deploy “~/flask-restx-api”? [Y/n] y
? Which scope do you want to deploy to? cauachagas
? Link to existing project? [y/N] n
? What’s your project’s name? flask-restx-api
? In which directory is your code located? ./
```

Ao terminar, mostrará um link para acessar sua aplicação.

### Veja esta aplicação rodando

https://flask-restx-api-exemplo.vercel.app


## Referências
- <a class="anchor" id="1">https://flask-restx.readthedocs.io/en/latest/</a>
- https://www.youtube.com/watch?v=levz4eumJ98
- https://vercel.com/docs/serverless-functions/supported-languages#python
- https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k