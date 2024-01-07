import streamlit as st
import streamlit.components.v1 as components
import os
import jwt
import time

METABASE_SITE_URL = st.secrets["METABASE_SITE"]
METABASE_SECRET_KEY = st.secrets["METABASE_SECRET"]

payload = {
  "resource": {"dashboard": 1},
  "params": {
    "client_(payment)": ["ERA TANI","BCA","AXIATA BOOST"]
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
# components.iframe(iframeUrl, width=300, height=800, scrolling=True)
components.html(f"""
                <iframe
                  src="{iframeUrl}"
                  frameborder="0"
                  width="100%"
                  height="600"
                  allowtransparency
              ></iframe>
                """,
                height=600,
                scrolling=True)