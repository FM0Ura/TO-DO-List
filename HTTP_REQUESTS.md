# HTTP Requests (Requisições HTTP)

## O que é HTTP?

HTTP, é o acrônimo para HyperText Transfer Protocol, sendo esse o principal protocolo de comunição de computadores

Essa comunicação entre os dispositivos é feita de acordo com o modelo de **REQUEST** e **RESPONSE**. Especificamente as respostas de transferência acontecem usando TCP (Transmission Control Protocol).

O TCP gerencia as conexões de internet e implementa a comunicação entre o lado do cliente e o lado do servidor.

A diferença entre o HTTP e o TCP está no fato de o HTTP é a linguagem utilizada tanto pelo cliente quanto pelo servidor para se comunicarem, já o TCP é o que permite essa comunicação entre os servidores

## Qual a sua função?

Essa comunicação segue o modelo de **REQUEST** e **RESPONSE**, ou seja, ao **acessar um site** você estará **requisitando informações do servidor** onde o site está hospedado, e **enviará uma resposta** ao computador que **solicitou a requisição**.

As respostas, geralmente são arquivos HTML que serão interpretados pelo navegador. Porém, HTTP não é utilizado apenas pelo navegador, diversos aplicativos de celular, para acessar suas informações utilizam esse modelo de comunicação.

### Tipos de Requisições

| Requisições | Ação                              | Analogia do Restaurante        |
| ----------- | --------------------------------- | ------------------------------ |
| GET         | Requisita informações do servidor | Pedir o cardápio               |
| POST        | Requisita uma gravação de dados   | Registrar um pedido            |
| PUT         | Requisita alteração de dados      | Registrar um mudança no pedido |
| DELETE      | Requisita uma remoção de dados    | Cancelar o pedido              |

## Status Code

(Á FAZER) São quais tipos de respostas podem ser obtidas, como as seguintes:

## Estrutura de Requisição e Resposta

### Estrutura de Requisição

A comunicação feita utilizando HTTP é feita utilizando mensagem, essa mensagem possui obrigatoriamente, dois espaços reservados. O header e o body, caso uma dessas divisões do arquivo possuem suas próprias particularidades.

Antes do header, a primeira linha da mensagem, também conhecida como **_request line_**, nella há o verbo HTTP (GET, PUT, DELETE etc...), a URIs e também o número da versão do HTTP. Com isso, exemplos de header seriam os seguintes:

```http
GET/home.html HTTP/1.1
POST/index.html HTTP/1.1
DELETE/query.html HTTP/1.1
```

Ao separarmos os elementos dessas linhas temos:

| HTTP   | URIs       | Versão do HTTP |
| ------ | ---------- | -------------- |
| GET    | home.html  | HTTP/1.1       |
| POST   | index.html | HTTP/1.1       |
| DELETE | query.html | HTTP/1.1       |

#### Header:

Os cabeçalhos (headers) contêm metadados sobre a solicitação, como informações sobre o navegador, cookies, tipos de conteúdo aceitos, entre outros. Alguns desses metadados seriam:

- **User-Agent:** Identifica o agente do usuário (geralmente o navegador) que está fazendo a solicitação.

- **Host:** Especifica o nome de domínio do servidor.

- **Accept:** Indica os tipos de mídia que o cliente pode processar.

- **Cookies:** Pode incluir informações de autenticação ou dados específicos da sessão.

- **Authorization:** Pode conter credenciais para autenticação no servidor.

- **Referer (Referência):** Indica de onde o cliente veio (a página anterior que continha o link).

- **Content-Type:** Especifica o tipo de conteúdo no corpo da solicitação (por exemplo, "application/json" para dados JSON).

Um exemplo de uma mensagem HTTP de requisição completa seria a seguinte:

```html
GET /exemplo.html HTTP/1.1
<!-- Linha de Solicitação -->
Host: www.exemplo.com
<!-- Host (Inicio do Header) -->
User-Agent: Mozilla/5.0 Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,_/_;q=0.8
```

#### Body:

Embaixo do header, separado por uma linha em branco há o body, que contém os dados que o cliente está enviando para o servidor, caso o cliente não esteja enviando nada o body ficará em branco, o que torna-o opcional.

O corpo da requisição é comumente utilizado em solicitações HTTP do tipo POST, PUT e PATCH. O body pode ser escrito de diversas formas, os formatos mais comuns são XML, JSON, x-www-form-urlencoded, plain, form-data.

Um exemplo de uma mensagem HTTP REQUEST completa seria a seguinte:

```http
POST /enviar-dados HTTP/1.1
Host: www.exemplo.com
Content-Type: application/json

{
  "nome": "Maria",
  "email": "maria@example.com",
  "idade": 25
}
```

### Estrutura de Resposta

Já na estrutura de resposta do servidor a organização é diferente. Assim como a requisição, a resposta possui um header (obrigatório) e um body (opcional). Também assim como na requisição a primeira linha da mensagem é especial e diferenciada, chamada de **_status line_**, nessa linha há a versão do HTTP, o status code, e uma frase que explica o status code.

Exemplos de **_status line_** seriam:

```http
HTTP 1.1/200 OK
HTTP 1.1/404 Not Found
HTTP 1.1/403 Forbidden
HTTP 1.1/500 Internal Server Error
```

Com isso temos:

| Versão do HTTP | Status Code | Frase                 |
| -------------- | ----------- | --------------------- |
| HTTP 1.1       | 200         | OK                    |
| HTTP 1.1       | 404         | Not Found             |
| HTTP 1.1       | 403         | Forbidden             |
| HTTP 1.1       | 500         | Internal Server Error |

#### Header:

Um exemplo de HTTP RESPONSE completa seria a seguinte:

#### Body:

O body contém os dados solicitados ao servidor. Ou seja, ao clicar em um site no google, será enviada uma requisição ao servidor, e o servidor irá retornar um resposta, se for positiva o cliente receberá o arquivo HTML da página solicitada.

```http response
HTTP/1.1 200 OK
Date: Sat, 05 Nov 2023 12:00:00 GMT
Server: Apache/2.4.38 (Ubuntu)
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
<head>
    <title>Página de Exemplo</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
</body>
</html>
```
