# Serviços gRPC - stubs e services para comunicação remota
import grpc  # Importa a biblioteca gRPC para criar serviços RPC
import Proto.user_pb2_grpc as pb2_grpc  # Stub 
import Proto.user_pb2 as pb2  # Classes de mensagens Protocol Buffers geradas automaticamente


def client():
    # Estabelece uma conexão insegura (sem TLS/SSL) com o servidor gRPC
    # O servidor está rodando no localhost na porta 50051
    with grpc.insecure_channel('localhost:50051') as channel:
        # Cria um stub (cliente) para o serviço UserService
        # O stub é usado para fazer chamadas RPC para o servidor
        stub = pb2_grpc.UserServiceStub(channel)
        
        # === OPERAÇÕES CRUD NO SERVIÇO DE USUÁRIOS ===
        
        # 1. Adiciona um novo usuário (John)
        # id é auto-incrementado pelo servidor)
        response1 = stub.AddUser(pb2.UserRequest(id=0, name='John', email="ze@123"))
        
        # 2. Adiciona outro usuário (ze)
        response2 = stub.AddUser(pb2.UserRequest(id=0, name='ze', email="ze@123"))

        # 3. Busca um usuário por id
        response3 = stub.GetUser(pb2.UserIdRequest(id=9))

        # 4. Atualiza o usuário com ID 2
        # Modifica nome para 'angela' e email para 'angela@123'
        response4 = stub.UpdateUser(pb2.UserRequest(id=2, name='angela', email="angela@123"))

        # 5. Busca o usuário recém-atualizado (ID 2) para verificar as mudanças
        response5 = stub.GetUser(pb2.UserIdRequest(id=2))

        # 6. Remove o usuário com ID 1 do sistema
        response6 = stub.DeleteUser(pb2.UserIdRequest(id=1))

        # === EXIBIÇÃO DOS RESULTADOS ===
        
        # Imprime as respostas de todas as operações
        # Cada resposta contém: mensagem de status, id, nome e email do usuário
        print(f"{response1.msg}: {response1.id} -  {response1.name} -  {response1.email}")
        print(f"{response2.msg}: {response2.id} -  {response2.name} -  {response2.email}")
        print(f"{response3.msg}: {response3.id} -  {response3.name} -  {response3.email}")
        print(f"{response4.msg}: {response4.id} -  {response4.name} -  {response4.email}")
        print(f"{response5.msg}: {response5.id} -  {response5.name} -  {response5.email}")
        print(f"{response6.msg}: {response6.id} -  {response6.name} -  {response6.email}")   


if __name__ == '__main__':
    client()