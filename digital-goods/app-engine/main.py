#!/usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import webapp2
import jwt
from google.appengine.ext.webapp import template
import os

from sellerinfo import SELLER_ID
from sellerinfo import SELLER_SECRET

class MainPage(webapp2.RequestHandler):
  def get(self):  
     self.redirect('/iframer')    

class AjaxJWT(webapp2.RequestHandler):
  def get(self):  
    now = int(time.time())
    now_plus_one = now + 3600
    self.request.get('subscribe', default_value='no')

    name = self.request.get('name', default_value='Awesome Item')
    desc = self.request.get('desc', default_value='Awesome Item is the coolest thing you can buy')
    price = self.request.get('price', default_value='1.00')

    jwt_token = jwt.encode(
      {
        'iss' : SELLER_ID,
        'aud' : 'Google',
        'typ' : 'google/payments/inapp/item/v1',
        'iat' : now,
        'exp' : now_plus_one,
        'request' : {
          'name' : name,
          'description' : desc,
          'price' : price,
          'currencyCode' : 'USD',
          'sellerData' : 'fromDigitalGoodsHangoutApp'
        }
      },
      SELLER_SECRET)

    self.response.headers['Content-Type'] = 'application/json'
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.out.write(jwt_token)

class WebappJWT(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    path = os.path.join(os.path.dirname(__file__), 'hangoutapp.html')

    self.response.out.write(
      template.render(path, []));

app = webapp2.WSGIApplication([('/', MainPage),
               ('/ajax', AjaxJWT),
               ('/iframer', WebappJWT)], debug=True)
