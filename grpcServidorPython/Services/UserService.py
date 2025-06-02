# Serviços gRPC - stubs e services para comunicação remota)
import Proto.user_pb2_grpc as pb2_grpc
# Mensagens Protobuf (estruturas de dados).
import Proto.user_pb2 as pb2

#os dados são salvos apenas em memoria nesse array
usuarios = []

class UserService(pb2_grpc.UserService):
# instancia atual da classe self
# O gRPC automaticamente espera que o método tenha dois parâmetros: request e context, mesmo que não use o context, ele precisa estar ali.
    def AddUser(self, request, context):
        # print(context.is_active()) #context.abort() Exemplo de uso para o context

        #adiciona os itens no array de usuarios
        id = len(usuarios) + 1
        usuarios.append({
            'id': id,
            'name': request.name,
            'email': request.email
        })
        return pb2.UserResponse(**{'id': id, 'name' : request.name, 'email': request.email, 'msg': 'add ok'})

    def GetUser(self, request, context):
        # busca na lista
        #next busca o primeiro usuário na lista usuarios que tenha id igual ao request.id
        #Se nenhum item for encontrado, ele retorna o valor padrão: None=nenhum
        user = next((usuario for usuario in usuarios if usuario['id'] == int(request.id)), None)
        if user:
            return pb2.UserResponse(**{'id': user['id'], 'name' : user['name'], 'email': user['email'], 'msg': 'get ok'})
        else:
            return pb2.UserResponse(**{'id': 0, 'name' : '', 'email': '', 'msg': 'get erro'})

    def UpdateUser(self, request, context):
        # busca na lista
        user = next((user for user in usuarios if user['id'] == int(request.id)), None)
        if user:
            # atualiza os dados
            user['name'] = request.name
            user['email'] = request.email
            return pb2.UserResponse(**{'id': user['id'], 'name' : user['name'], 'email': user['email'], 'msg': 'update ok'})
        else:
            return pb2.UserResponse(**{'id': 0, 'name' : '', 'email': '', 'msg': 'update erro'})

    def DeleteUser(self, request, context):
        # busca na lista
        user = next((c for c in usuarios if c['id'] == int(request.id)), None)
        if user:
            # exclui o usuário
            usuarios.remove(user)
            return pb2.UserResponse(**{'id': user['id'], 'name' : user['name'], 'email': user['email'], 'msg': 'del ok'})
        else:
            return pb2.UserResponse(**{'id': 0, 'name' : '', 'email': '', 'msg': 'del erro'})
