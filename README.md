# O que é o Pix Notification?

É uma automação do Telegram que utiliza um bot para enviar, em um grupo de conversa específico, uma notificação sempre que um Pix é recebido.

A ideia surgiu como uma forma de facilitar o controle de pagamentos sem a necessidade de acessar o telefone onde o aplicativo bancário está instalado.

### Como funciona?
O fluxo da automação começa a partir de um aplicativo chamado [Automate](https://play.google.com/store/apps/details?id=com.llamalab.automate&hl=pt_BR), que monitora as notificações do celular. Quando uma notificação do banco é detectada, ele captura a informação e dispara uma requisição HTTP para um servidor.

Esse servidor, por sua vez, utiliza um bot para enviar uma mensagem em um grupo do Telegram.

``` mermaid
graph TD
  A[Flow beginning] --> B{When notification};
  B --> C[HTTP request];
  C --> D{Server};
  C --> |Loop|B;
  D --> E[Telegram bot];
```
