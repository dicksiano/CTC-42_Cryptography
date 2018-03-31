# CTC-42_Cryptography

##Projeto 1
Mensagem transmitida é formada por caracteres extended-ASCII com tamanho de 10k. Dentro da mensagem o texto-claro codificado possui no máximo 1k, o resto é composto por propriedades da codificação e lixo.

#### Propriedades enviadas na mensagem:
* P1: Posição inicial do texto-claro codificado (0 < n < 10k), são necessários 14 bits para enviar essa info.
* P2: Tamanho do texto-claro codificado (0 < n <= 1000), necessários 10 bits.
* P3: n-ésimo número primo utilizado como chave, em caso de n = 1, chave será Pi; estipulando máximo 500º primo, necessários 9 bits.
* P4: Posição inicial da contagem da chave (0 < n < 999000), necessários 20 bits.

#### Estrutura da mensagem:
Os bits das propriedades serão enviados dentro dos caracteres do lixo com a seguinte estrutura:
* caractere = L L L L P4 P3 P2 P1

Por isso, são necessários 20 caracteres para enviar todas as propriedades, esses caracteres são distribuídos metade no início da mensagem e metade ao final. A posição deles é de acordo com os 10 primeiros números da sequência de Fibonacci (0,1,2,3,5,8,13,21,34,55), dessa forma sempre os 56 primeiros e últimos caracteres serão lixo necessário para envio das propriedades.