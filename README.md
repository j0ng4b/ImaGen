# ImaGen

## Como executar?
Para executar é necessário conhecimento básico de python (**não haverá arquivo executável!!**).  
Abaixo os passos para executar o projeto:

**Instalar dependências**  
Para instalar as dependências é bem simples, basta executar o seguinte comoando no terminal:

    pip install -r requirements.txt

Após o comando finalizar todas as dependências terão sido instaladas.

**Atribuir o token a variável de ambiente**  
Para que as imagens sejam geradas é necessário um token de acesso. Por razões financeiras não  
foi possível utilizar a api da OpenAI (Dall-e) e por razões de tempo de processamento não foi  
possível utilizar a Stable Diffusion.

Como alternativa utilizamos [MonsterAPI](https://monsterapi.ai/) para fazer a geração das imagens. Para obter um token de  
acesso visite: https://developer.monsterapi.ai/reference/getting-started-1.

Após obter o token, copie o arquivo `.env.sample` como `.env` e edite-o seguindo as instruções  
no próprio arquivo.


**Executar o projeto**
Feito todo o processo anterior chegou a parte mais simples, execute no terminal o seguinte comando:

    python app.py

Dependento do sistema operacional os comandos podem ter variações, por exemplo, no Windows pode ser  
necessário trocar `python` por `py.exe`.

Tudo correndo bem é possível acessar o projeto no navegador atráves do link que é exibido na tela do  
terminal.
