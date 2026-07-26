from google.adk.cli.fast_api import get_fast_api_app

app = get_fast_api_app(agents_dir=".", web=False, auto_create_session=True)
