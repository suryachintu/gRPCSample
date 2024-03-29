# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from codegen import sample_pb2 as sample__pb2


class EchoServiceStub(object):
  """Service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMessage = channel.unary_unary(
        '/endpoints.examples.sample.EchoService/GetMessage',
        request_serializer=sample__pb2.GetMessageRequest.SerializeToString,
        response_deserializer=sample__pb2.SampleMessage.FromString,
        )


class EchoServiceServicer(object):
  """Service definition
  """

  def GetMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMessage': grpc.unary_unary_rpc_method_handler(
          servicer.GetMessage,
          request_deserializer=sample__pb2.GetMessageRequest.FromString,
          response_serializer=sample__pb2.SampleMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'endpoints.examples.sample.EchoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
