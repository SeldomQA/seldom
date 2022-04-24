from genson import SchemaBuilder
from seldom.request import ResponseResult


def genson(data=None):
    """
    genson:
    https://github.com/wolverdude/GenSON
    """
    if (data is None) and ResponseResult.response is not None:
        data = ResponseResult.response

    builder = SchemaBuilder()
    builder.add_object(data)
    to_schema = builder.to_schema()
    return to_schema
