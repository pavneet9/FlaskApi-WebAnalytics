
from .webevent_pubsub import WebEventsPubSub
from .auth import SignupApi, LoginApi
from .testresource import TestResource

def initialize_routes(api):
#	 api.add_resource(WebEvents, '/api/webevents')
	 api.add_resource(SignupApi, '/api/signupapi')
	 api.add_resource(LoginApi,'/api/loginApi')
	 api.add_resource(TestResource, '/api/test')
	 api.add_resource(WebEventsPubSub, '/api/webeventspub')
