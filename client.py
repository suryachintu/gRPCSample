import grpc

from codegen import sample_pb2, sample_pb2_grpc

SERVER_ADDRESS = '0.0.0.0'
PORT = 8080


class EchoServiceClient(object):
    def __init__(self):
        """Initializer. 
           Creates a gRPC channel for connecting to the server.
           Adds the channel to the generated client stub.
        Arguments:
            None.
        
        Returns:
            None.
        """
        self.channel = grpc.insecure_channel(f'{SERVER_ADDRESS}:{PORT}')
        self.stub = sample_pb2_grpc.EchoServiceStub(self.channel)

    def get_message(self, name):
        """Gets a sample message.
        Arguments:
            name: The resource name of a user.
        
        Returns:
            None; outputs to the terminal.
        """
        request = sample_pb2.GetMessageRequest(
            name=name
        )

        try:
            response = self.stub.GetMessage(request)
            print('Message fetched.')
            print(response)
        except grpc.RpcError as err:
            print(err.details())  # pylint: disable=no-member
            print('{}, {}'.format(err.code().name, err.code().value))  # pylint: disable=no-member


e = EchoServiceClient()
e.get_message('hello')