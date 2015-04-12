
## this is write by qingluan 
# just a inti handler 
# and a tempalte offer to coder

import tornado
import tornado.web
import os
import docker

class BaseHandler(tornado.web.RequestHandler):
	def prepare(self):
#		self.db = self.settings['db']
		pass
	def get_current_user(self):
		return (self.get_cookie('user'),self.get_cookie('passwd'))
	def get_current_secure_user(self):
		return (self.get_cookie('user'),self.get_secure_cookie('passwd'))
	def set_current_seccure_user_cookie(self,user,passwd):
		self.set_cookie('user',user)
		self.set_secure_cookie("passwd",passwd)





class IndexHandler(BaseHandler):
	
	def prepare(self):
		super(IndexHandler,self).prepare()
		self.template = "template/index.html"

	def get(self):
		return self.render(self.template,post_page="/",containers=docker.getAllHostContainers())

	@tornado.web.asynchronous
	def post(self):
		# you should get some argument from follow 
		post_args = self.get_argument("name")
		#cmd= = self.get_argument("cmd")
                #cid= self.get_argument("containerId")
		# .....
		self.write(os.popen("/home/lrj/vxlan.sh "+post_args).read())
                print post_args
		# self.redirect()  # redirect or reply some content
                self.finish()


class ExecHandler(BaseHandler):
	
	def prepare(self):
		super(ExecHandler,self).prepare()
		self.template = "template/exec.html"

	def get(self):
		return self.render(self.template,post_page="/exec")

	@tornado.web.asynchronous
	def post(self):
		# you should get some argument from follow 
		#post_args = self.get_argument("Id")
		cmd= self.get_argument("cmd")
                cid= self.get_argument("containerId")
		# .....

		# self.redirect()  # redirect or reply some content
		self.write(os.popen("docker exec "+ cid+ " "+ cmd).read())
		self.finish()
	
