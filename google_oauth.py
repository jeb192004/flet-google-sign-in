import flet as ft
import urllib.parse
import uuid
import httpx

class MyGoogleOauth:
    def __init__(self, client_id, BASE_URL, stack=None, page=None):
        self.GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
        self.GOOGLE_SCOPES = ["profile", "email"]
        self.scopes = "%20".join(self.GOOGLE_SCOPES)
        self.client_id = client_id
        self.redirect_url = f"{BASE_URL}app/google/login/"
        self.confirm_login_url=f"{BASE_URL}app/google/login/confirm"
        self.wv = None
        self.stack=stack
        self.page=page
        self.session_token=None

    def on_lifecycle_change(self, event: ft.AppLifecycleStateChangeEvent):        
        if event.state==ft.AppLifecycleState.RESUME:
            headers = {"Authorization": f"Bearer {self.session_token}", "X-API-Key-Type": "temp_api_key"}
            response = httpx.post(self.confirm_login_url, headers=headers)
            if response.status_code == 200:
                self.page.client_storage.set("xxxxxxx.xxxxx.user.token", response.json()["api_key"])
                self.page.go("/bills")
                self.page.on_app_lifecycle_state_change=None
            else:
                print(f"HTTP Error: {response.status_code}")
                self.page.open(ft.SnackBar(ft.Text(f"{response.json()}")))
                self.session_token=None
        

    def login_with_google(self, e):
        session_token = str(uuid.uuid4())
        self.session_token=session_token
        auth_url =  f"{self.GOOGLE_AUTH_URL}?" \
                    f"client_id={self.client_id}&" \
                    f"redirect_uri={self.redirect_url}&" \
                    f"response_type=code&" \
                    f"scope={self.scopes}&" \
                    f"state={session_token}"
        self.page.launch_url(auth_url)
        self.page.on_app_lifecycle_state_change = self.on_lifecycle_change
        
