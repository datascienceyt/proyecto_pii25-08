FEATURE_FLAGS = {
  "ALERT_REPORTS": True,
  "EMBEDDED_SUPERSET": True,
  "ENABLE_JAVASCRIPT_CONTROLS": True,
}
ENABLE_UI_THEME_ADMINISTRATION = True
THEME_DEFAULT = {
    "token": {
        "colorPrimary": "#2893B3",
        "colorSuccess": "#5ac189",
        # ... your theme JSON configuration
    }
}

# Optional: Dark theme configuration
THEME_DARK = {
    "algorithm": "dark",
    "token": {
        "colorPrimary": "#2893B3",
        # ... your dark theme overrides
    }
}

TALISMAN_ENABLED = False
OVERRIDE_HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
ENABLE_CORS = True
WTF_CSRF_ENABLED = False
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['Content-Type', 'Authorization'],
    'resources': ['*'],
    'origins': ['*']
}
GUEST_ROLE_NAME = "Gamma"
LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    "es": {"flag": "es", "name": "Spanish"},
}
CSV_EXPORT = {
    "encoding": "utf_8_sig",
    "sep": ";",
}
