INSTALLATION

You need to create an application in the Google API Console.

https://code.google.com/apis/console/

You need to turn on both Google+ API and Google+ Hangouts API in the
"Services" tab.

In the "API Access" tab, create an OAuth 2.0 client ID.  You do not
need to set the site or hostname, nor any redirect URIs if you are
only using this application in a Hangout.

Enter the URL to authCheck.xml spec in the Hangouts tab.

Start a hangout, and click "Authorize".

## To use the minimalist version

Same as above, except point to minimalistAuth.xml.

What's the difference?  mimimalistAuth.xml loads only the auth part of
the Google JS Client library.  If your app is only using the access
token and not making any further use of the client library, you can
use this startup instead.

---
Reference:

Google API JS Client:
http://code.google.com/p/google-api-javascript-client/

Standalone Auth Client:
http://code.google.com/p/google-api-javascript-client/wiki/CORS
