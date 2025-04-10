# flet-google-sign-in
Method to sign in via Google Oauth in flet mobile apps

Usage<br>
Import MyGoogleOauth
```
from google_oauth import MyGoogleOauth
```

Init MyGoogleOauth setting your client id, redirect url and ect.

```
google_oauth=MyGoogleOauth(BASE_URL=BASE_URL, client_id="your-client-id", stack=stack, page=page)
```

In your button on click
```
lambda e:google_oauth.login_with_google(e)
```

<br><br>
Using this method to use google login requires having a server to process the code returned from google.<br>
sending your session token 
```
session_token = str(uuid.uuid4())
self.session_token=session_token
```
as the state parameter 
```
f"state={session_token}"
```
Google will return this with their code in the redirect url.
<br><br>
I saved the session token from the state parameter with the code from Google temporarily in my database.  Then as I returned to the flet app on_app_lifecycle_state_change gets triggered and if on_app_lifecycle_state_change state is RESUME I send a request to the server with the session token, matching the token to the one saved in the database with the code and exchange that for the user data.
