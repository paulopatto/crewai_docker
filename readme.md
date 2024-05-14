# crewAI no Docker

## Sobre CrewAI no Docker 

Esse projeto visa fazer a utilização do crewAI usando Docker, sem ter que instalar e promovendo uma utilização segura sem impactar as bibiliotecas e facilitando o usos.

Esse projeto usa:

- [crewAI](https://www.crewai.com/) 
- [Docker](https://www.docker.com/) & [Compose](https://docs.docker.com/compose/) 
- [gradIO](https://www.gradio.app/)

## Como usar

Segue passo a passo de como usar:

1. Instale o Docker Desktop (Windows) ou alguma versão Linux.
2. Crie uma pasta para seu projeto e dentro dela crie uma pasta chamada **app**
3. Faça download dos arquivos e salve na pasta de seu projeto, atente para os arquivos dentro da pasta **app**.

## Ajuste sua chave da OpenAI ou outro modelo que deseja usar

Dentro da pasta **app**, ajuste sua **API KEY** da openAI no arquivo `settings.py`

## Execute o comando para executar o container

Para baixar e ativar o container execute o comando:

```sh
docker compose up
```

## Entre pelo navegador na página do gradio

Acesse o endereço do gradio:

[http://localhost:7860/](http://localhost:7860/)

ou para tema dark:

[http://localhost:7860/?__theme=dark](http://localhost:7860/?__theme=dark)


Projeto original do usuário @mumunha no [Github](https://github.com/mumunha/crewai_docker)
