import grpc
import Proto.user_pb2_grpc as pb2_grpc
import Proto.user_pb2 as pb2
import Proto.product_pb2 as pb2_product
import Proto.product_pb2_grpc as pb2_grpc_product


def client():
   with grpc.insecure_channel('localhost:50051') as channel:
      #operações de cliente
      stubUser = pb2_grpc.UserServiceStub(channel)

      #adicionado campo de idade no crud de usuario

      print('Dados de usuário')
      responseUser1 = stubUser.AddUser(pb2.UserRequest(id = 0, name='John', email = "ze@123", age = 30))
      responseUser2 = stubUser.AddUser(pb2.UserRequest(id = 0, name='ze', email = "ze@123", age = 31))

      responseUser3 = stubUser.GetUser(pb2.UserIdRequest(id = 9))

      responseUser4 = stubUser.UpdateUser(pb2.UserRequest(id = 2, name='angela', email = "angela@123", age = 27))

      responseUser5 = stubUser.GetUser(pb2.UserIdRequest(id = 2))

      responseUser6 = stubUser.DeleteUser(pb2.UserIdRequest(id = 1))

      print(f"{responseUser1.msg}: {responseUser1.id} -  {responseUser1.name} -  {responseUser1.email} - {responseUser1.age}")
      print(f"{responseUser2.msg}: {responseUser2.id} -  {responseUser2.name} -  {responseUser2.email} - {responseUser2.age}")
      print(f"{responseUser3.msg}: {responseUser3.id} -  {responseUser3.name} -  {responseUser3.email} - {responseUser3.age}")
      print(f"{responseUser4.msg}: {responseUser4.id} -  {responseUser4.name} -  {responseUser4.email} - {responseUser4.age}")
      print(f"{responseUser5.msg}: {responseUser5.id} -  {responseUser5.name} -  {responseUser5.email} - {responseUser5.age}")
      print(f"{responseUser6.msg}: {responseUser6.id} -  {responseUser6.name} -  {responseUser6.email} - {responseUser6.age}")  
      
      #adicionado operações de produto
      print('Dados de produto')
      stub_product = pb2_grpc_product.ProductServiceStub(channel)
      
      response1 = stub_product.AddProduct(pb2_product.ProductRequest(id=1, description="Abc Bolinhas", value=20.24))       
      response2 = stub_product.UpdateProduct(pb2_product.ProductRequest(id=1, description='Abc Bolinhas - seu nome', value=30.90))
      response3 = stub_product.GetProduct(pb2_product.ProductIdRequest(id=1))
      response4 = stub_product.DeleteProduct(pb2_product.ProductIdRequest(id=5))

      print(f"{response1.msg}: {response1.id} -  {response1.description} -  {response1.value}")
      print(f"{response2.msg}: {response2.id} -  {response2.description} -  {response2.value}")
      print(f"{response3.msg}: {response3.id} -  {response3.description} -  {response3.value}")
      print(f"{response4.msg}: {response4.id} -  {response4.description} -  {response4.value}")
    

if __name__ == '__main__':
    client()