try:
    __import__('pkg_resources').declare_namespace(__name__)
except:
    pass

from pyga.requests import Q

def shutdown():
    '''
    Fire all stored GIF requests One by One.
    You should call this if you set Config.queue_requests = True
    '''
    map(lambda func: func(), Q.REQ_ARRAY)
