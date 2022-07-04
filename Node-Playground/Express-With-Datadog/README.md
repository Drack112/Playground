<h1 align="center">
    Express com DogData e Redis
</h1>

<p align="center">
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-rodando">Rodando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<a id="rocket-tecnologias"></a>

## 🚀 Tecnologias

<div align="center">
 	<img src="https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white" />
     <img src="https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB" />
     <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" />
     <img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white" />
     <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" />

</div>

<br>

<p align="center">
  <img alt="Ecoleta" src=".github/images/app.png" width="100%">
</p>
<a id="-projeto"></a>

## 💻 Projeto

Um teste simples para integrar uma aplicação Express com o logger **_[DataDog](https://www.datadoghq.com/)_**. Ele inclui mais algumas funções como por exemplo o sistema de cache com **_[Redis](https://redis.io/)_**.

<a id="-layout"></a>

<a id="-rodando"></a>

## Rodando o projeto 🌇

## Requerimentos:

- [NodeJS](https://nodejs.org/en/)
- [Docker](https://www.docker.com/)

## 📂 Instalando as dependências:

Yarn:

```bash
yarn install
```

NPM:

```bash
npm install
```

### 🐬 Iniciando o Banco de dados:

É recomendado subir ambos os bancos MongoDB e redis, você pode fazer isso usando o comando:

```bash
docker-compose up redis
```

Caso queira fazer um pequeno test de criação de usuário rode pelo comando:

```bash
yarn test
#ou
npm run test
```

## 🚀 Executando a API:

Apenas de o comando:

```bash
yarn dev
#ou
npm run dev
```

<a id="-como-contribuir"></a>

## 🤔 Como contribuir

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

Depois que o merge da sua pull request for feito, você pode deletar a sua branch.
