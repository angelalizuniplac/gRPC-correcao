import grpc  # Importa a biblioteca gRPC para criar serviços RPC
from concurrent import futures  # Importa futures para gerenciar execução concorrente
import Proto.user_pb2_grpc as pb2_grpc  # Importa as classes geradas pelo compilador do protobuf para gRPC
import Services.UserService as service  # Importa o serviço de usuário que implementa a lógica de negócio


def server():
    # Cria uma instância do servidor gRPC com um pool de 10 threads para processar requisições
    # O servidor pode lidar com até 10 requisições simultaneamente
    # Se chegarem mais de 10 requisições ao mesmo tempo, as extras aguardarão em fila até que uma thread fique disponível
    # Não há necessidade de criar novas threads para cada cliente que se conecta
    # O sistema tem uma capacidade previsível e controlada de processamento
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Registra nosso serviço de usuário no servidor gRPC
    pb2_grpc.add_UserServiceServicer_to_server(service.UserService(), server)
    
    # Define a porta onde o servidor vai escutar (50051 é a porta padrão para serviços gRPC)
    # [::] significa que vai escutar em todos os endereços IPv6 (equivalente a 0.0.0.0 para IPv4)
    server.add_insecure_port('[::]:50051')
    
    # Exibe uma mensagem informando que o servidor foi iniciado
    print("Server started at 50051")
    
    # Inicia o servidor (começa a aceitar requisições)
    server.start()
    
    # Bloqueia a execução até o servidor ser encerrado
    # quando chama server.start(), o servidor gRPC começa a aceitar conexões, mas essa função não bloqueia a execução do programa - ela retorna imediatamente.
    # Sem wait_for_termination(), o programa Python continuaria executando até o final do script e terminaria, encerrando o servidor prematuramente.
    server.wait_for_termination()


# Verifica se este script está sendo executado diretamente (não importado)
if __name__ == '__main__':
    server()  # Chama a função server() para iniciar o servidor gRPC





    