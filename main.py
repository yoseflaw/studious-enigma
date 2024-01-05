import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os
import jwt
import time

load_dotenv()

METABASE_SITE_URL = "https://telmark.metabaseapp.com"
METABASE_SECRET_KEY = os.environ["METABASE_SECRET"]

payload = {
  "resource": {"dashboard": 1},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"

# embed streamlit docs in a streamlit app
components.iframe(iframeUrl, width=1024, height=864)