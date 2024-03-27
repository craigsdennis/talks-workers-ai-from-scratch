import os

from cloudflare import Cloudflare

from dotenv import load_dotenv
import streamlit as st


load_dotenv()

client = Cloudflare(
    api_token=os.environ.get("CLOUDFLARE_API_TOKEN"),
)
account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID")

"# Python SDK Example"

with st.form("text-to-image"):
    model = st.selectbox("Choose your model", options=("@cf/lykon/dreamshaper-8-lcm", "@cf/bytedance/stable-diffusion-xl-lightning"))
    prompt = st.text_input("What image would you like to generate?")
    submitted = st.form_submit_button("Generate")
    if submitted:
        response = client.workers.ai.with_raw_response.run(model, account_id=account_id, prompt=prompt)
        st.image(response.read(), caption=prompt)
