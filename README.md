# gRPC-cliente-servidor-py

Primeiro crie um Ambiente Virtual de Desenvolvimento para isolar as bibliotecas e dependências do projeto.

1. Utilizando 'venv' que é módulo do Python usado para criar ambientes virtuais: 

    ```python -m venv venv ```

2. Ative o ambiente virtual criado para poder utilizar:

    ```Venv\Scripts\activate ```

Se tudo der certo, quando estiver ativo, vai aparecer uma flag com o nome do ambiente virtual no início da linha de comando. 

---

Instale as dependencias dos pacotes necessários no ambiente virtual através do pip: 

1. Atualizar o pip do ambiente virtual

    ```python.exe -m pip install --upgrade pip ``` 

2. Instalação do framework gRPC 

    ```pip install grpcio ```

3. Instalar as ferramentas gRPC: 
As ferramentas gRPC incluem o compilador protoc e o plugin especial para gerar código de definição de serviço a partir de arquivos .proto. 

    ```pip install grpcio-tools ```

4. Atualize o arquivo de requeriments

    ```pip freeze > requirements.txt ```

Ambiente criado e configurado! 

---

Gerar os stubs com base no arquivo .proto:
    
 ```python -m grpc_tools.protoc --proto_path=. ./Proto/user.proto --python_out=. --grpc_python_out=. ```

---

Agora está pronto para executar: 
    ```py main.py ```

---

A execução deve acontecer dentro de cada diretorio, cliente e servidor, ou seja, executar 2x sendo 1 para cada.
Frisando: Cliente e servidor devem terem seus proprios ambientes virtuais!!!!

Lembrando também que esse passo a passo é a configuração completa para a primeira execução, após isso para as proximas basta apenas ativar o ambiente virtual e executar o arquivo main. 



