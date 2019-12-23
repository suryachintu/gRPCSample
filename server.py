from concurrent import futures
import time

import grpc

from codegen import sample_pb2, sample_pb2_grpc


# Inherit from sample_pb2_grpc.ExampleServiceServicer
# ExampleServiceServicer is the server-side artifact.
class EchoServiceServicer(sample_pb2_grpc.EchoServiceServicer):
    def GetMessage(self, request, context):
        """Gets a sample message.
           gRPC calls this method when clients call the GetUser rpc (method).

        Arguments:
            request (GetMessageRequest): The incoming request.
            context: The gRPC connection context.
        
        Returns:
            user (User): A user.
        """
        name = request.name
        sample_message = sample_pb2.SampleMessage(
            name=name
        )

        return sample_message


if __name__ == '__main__':
    # Run a gRPC server with one thread.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    # Adds the servicer class to the server.
    sample_pb2_grpc.add_EchoServiceServicer_to_server(EchoServiceServicer(), server)
    server.add_insecure_port('0.0.0.0:8080')
    server.start()
    print('API server started. Listening at 0.0.0.0:8080.')
    while True:
        time.sleep(60)
