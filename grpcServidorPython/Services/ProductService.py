import Proto.product_pb2_grpc as pb2_grpc
import Proto.product_pb2 as pb2

produtos = []

class ProductService(pb2_grpc.ProductService):
    def AddProduct(self, request, context):
        id = len(produtos) + 1
        produtos.append({
            'id': id,
            'description': request.description,
            'value': request.value
        })
        return pb2.ProductResponse(**{'id': id, 'description': request.description, 'value': request.value, 'msg': 'add ok'})

    def GetProduct(self, request, context):
        product = next((p for p in produtos if p['id'] == request.id), None)
        if product:
            return pb2.ProductResponse(**{
                'id': product['id'],
                'description': product['description'],
                'value': product['value'],
                'msg': 'get ok'
            })
        else:
            return pb2.ProductResponse(**{'id': 0, 'description': '', 'value': 0, 'msg': 'get erro'})

    def UpdateProduct(self, request, context):
        product = next((p for p in produtos if p['id'] == request.id), None)
        if product:
            product['description'] = request.description
            product['value'] = request.value
            return pb2.ProductResponse(**{
                'id': product['id'],
                'description': product['description'],
                'value': product['value'],
                'msg': 'update ok'
            })
        else:
            return pb2.ProductResponse(**{'id': 0, 'description': '', 'value': 0, 'msg': 'update erro'})

    def DeleteProduct(self, request, context):
        product = next((p for p in produtos if p['id'] == request.id), None)
        if product:
            produtos.remove(product)
            return pb2.ProductResponse(**{
                'id': product['id'],
                'description': product['description'],
                'value': product['value'],
                'msg': 'del ok'
            })
        else:
            return pb2.ProductResponse(**{'id': 0, 'description': '', 'value': 0, 'msg': 'del erro'})