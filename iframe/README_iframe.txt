
HANGOUTS IN AN IFRAME

This is an experimental service!

This allows developers build hangout apps in an iframe hosted on their 
own servers, rather than directly in a gadget.  It uses the
Google JS API client to do OAuth2.

WHY DO I WANT THIS?

Are you hung up on XSS problems?  Are you trying to do Ajax?  Do you
not want to use "Security.allowDomain('*')" in your .swf?

All of these are great reasons to use this iframe service.  Your app
is in an iframe that is hosted on *your* site, not
googleusercontent.com.  However, by including a few .js files, you get
access to information from the hangout. 

HOW IT WORKS

Create an HTML page somewhere on the internet.  (It doesn't even need
to be publicly available!)

Add these lines to it:

<script src="//hangoutsapi.talkgadget.google.com/talkgadget/apps/gadgets/js/rpc.js">
</script>
<script
src="//hangoutsapi.talkgadget.google.com/hangouts/api/hangout.js?v=0.2">
</script>

When you create your project in code.google.com, you need to enable
Hangouts API (of course) and then use our (currently alpha) service to
automatically generate your XML gadget spec.

When the hangout starts, you will get a chance to authorize.  You 
can automatically check for authorization after the client starts 
with this call (assumes your app starts with "onClientReady"):

<script src="https://apis.google.com/js/client.js?onload=onClientReady">
</script> 


GETTING THIS SAMPLE TO WORK:

1. Download the two source files (authCheck.html and authCheck_iframe.js).

2. Host them wherever you want, as long as this serves https, such as
Google App Engine.  We have these files already hosted at:

https://hangoutoauth2example/static/authCheck.html
https://hangoutoauth2example/static/authCheck_iframe.js

These will not work, as they do not contain a correct client_id (see
below), so you will have to host them yourself at, say,
yourdomain.com. 

3. Create a project at https://code.google.com/apis/console/.

4. In the "Services" tab, turn on "Google+ Hangouts API".

5. In the API Access tab, create a client ID (it's the big button
there).  List https://yourdomain.com as the domain name.

After you hit "Done", your site should be listed under JavaScript
origins for that Client ID.

6. Find the Client ID and put it in authCheck_iframe.js under
'client_id' in checkAuth() function under gapi.auth.authorize.  (It's
a string currently filled with 'your_client_id'.)

7.  Find the API Key (under "Simple API Access") and put it in
authCheck_iframe.js under YOUR_API_KEY.

8.  In the API console, now switch to the "Hangouts" tab.  In the
"Gadget URL", type:

https://hangoutiframer.appspot.com/forward/gadgetspec?u=https://yourdomain.com/authCheck.html

and hit "Save".

You can follow that link to make sure it's correct.  You should get an
XML file, a gadget spec, that contains your link in the right place.

9. Click "Start hangout" and you should get to the app, which will
provide an "Authorize" button that will look up who you are and
provide an OAuth2 token.








