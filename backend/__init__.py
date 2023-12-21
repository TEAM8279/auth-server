from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session, dashboard

init(
    app_info=InputAppInfo(
        app_name="8279",
        api_domain="http://localhost:8079",
        website_domain="http://localhost:8079",
        api_base_path="/auths",
        website_base_path="/s"
    ),
    supertokens_config=SupertokensConfig(
        # https://try.supertokens.com is for demo purposes. Replace this with the address of your core instance (sign up on supertokens.com), or self host a core.
        connection_uri="http://localhost:3567",
        # api_key=<API_KEY(if configured)>
    ),
    framework='flask',
    recipe_list=[
        session.init(), # initializes session features
        emailpassword.init(),
        dashboard.init(),
    ]
)