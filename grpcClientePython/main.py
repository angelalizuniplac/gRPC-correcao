import grpc
import Proto.user_pb2_grpc as pb2_grpc
import Proto.user_pb2 as pb2


def client():
   with grpc.insecure_channel('localhost:50051') as channel:
      stub = pb2_grpc.UserServiceStub(channel)
      
      response1 = stub.AddUser(pb2.UserRequest(id = 0, name='John', email = "ze@123"))
      response2 = stub.AddUser(pb2.UserRequest(id = 0, name='ze', email = "ze@123"))

      response3 = stub.GetUser(pb2.UserIdRequest(id = 9))

      response4 = stub.UpdateUser(pb2.UserRequest(id = 2, name='angela', email = "angela@123"))

      response5 = stub.GetUser(pb2.UserIdRequest(id = 2))

      response6 = stub.DeleteUser(pb2.UserIdRequest(id = 1))

      print(f"{response1.msg}: {response1.id} -  {response1.name} -  {response1.email}")
      print(f"{response2.msg}: {response2.id} -  {response2.name} -  {response2.email}")
      print(f"{response3.msg}: {response3.id} -  {response3.name} -  {response3.email}")
      print(f"{response4.msg}: {response4.id} -  {response4.name} -  {response4.email}")
      print(f"{response5.msg}: {response5.id} -  {response5.name} -  {response5.email}")
      print(f"{response6.msg}: {response6.id} -  {response6.name} -  {response6.email}")   


if __name__ == '__main__':
    client()