# flet-google-sign-in
Method to sign in via Google Oauth in flet mobile apps

Usage
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
