#projeto Ava redis + python
## Dockerfile

o dockerfile é um arquivo de texto com intruções 

para criar um dockerfile

Receita de volo para criar uma imagem.

dockerfile
´
FROM node:20
workdir /app
copy
RUN npm install
expose 3000
CMD ["npm", "start"]
´

From -> Definir uma imagem base.
WORKDIR -> DEfine um diretorio de trabalho.
COPY -> Copia arquivos para dentro do container.
RUN -> Executar comandos durante o build.
EXPOSE -> Documentar a porta utilizada.
CMS -> Comando inicial do container.

build -> dessa imagem
docker build <-> cria a imagem
-t <-> define nome
docker build -t meu-app .
meu-app <-> o nome da minha imagem
. <-> diretorio atual

docker images <-> Listar as imagens docker que vc criou

## Dockerfile da API

FROM python:3.11-slim
- Escolher a imagem do container.

WORKDIR /code
- Define o /code como pasta de trabalho dentro do container.
A partir daqui, os proximos comandos rodam considerando esse diretorio base.

COPY requirements.txt .
- Copia o aquivo de requirements.txt da sua máquina 
para dentro docontainer, no diretorio atual que é o /code.

RUN pip install --no-cache-dir -r requirements.txt
- Instala as dependências

COPY . .
- Copia todo o conteudo da pasta [api] para dentro do container,
também

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000", "--reload"]

- O comando será executado quando o containe iniciar.
uvicorn é o nosso servidor
main:appbuscar o arquivo main(entrypoint).
--host

## Dockerfile da Worker

- È basicamente o mesmo do Dockerfile da API 

A unica coisa que muda é o comando 
["python", "-u", "worker.py"]
Rode utilizando o python com a flag -u o arquivo worker.py
A flag 
apareceram em tempo real no docker logs do cotainer.

pip install -r 

#