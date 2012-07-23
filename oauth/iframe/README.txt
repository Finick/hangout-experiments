== hangoutiframer - Sample OAuth2 app ==

This app uses the hangoutiframer service to put a Hangout App
in an iframe that is on your domain, not googleusercontent.

The point of app is to demonstrate how to access the OAuth2 
2.0 access token from within the iframe.  Also, you can pass
data to hangoutiframer using the &gd= parameter.

== What's Included ==

hangoutOAuth2iframe.html:  This file comprises the entire hangout app.

== Getting Started == 

To run this sample: 

1. host the .html file on an https service.  (It's currently hosted
on https://plushangoutstarter.appspot.com/static/hangoutOAuth2iframe.html
if you don't want to modify it.)

2. Create an App in the Google+ APIs console.

3. Turn on "Google+ APIs" and "Google+ Hangout APIs" in the Services tab.

4. REALLY IMPORTANT:  Create a Client ID under the "Access" tabs.  
(If you do not, you will get 403 errors.)

5. In the "Hangouts" tab, use the following URL:

https://hangoutiframer.appspot.com/forward/v0.2?u=https://mydomain.com/path/to/hangoutOAuth2iframe.html

For example, if you wish to use the demo-hosting, you would do this:

https://hangoutiframer.appspot.com/forward/v0.2?u=https://plushangoutstarter.appspot.com/static/hangoutOAuth2iframe.html

6. Click on "Enter a Hangout".  You should get a permissions screen.
Accept those permissions.

7. Click on the "Make authenticated REST API call" to make an authenticated call!

== Getting Help == 

For basic help getting a Hangout App running, see:

https://developers.google.com/+/hangouts/getting-started

If you've found a bug or have questions please visit our developer
forum:

https://developers.google.com/+/support


