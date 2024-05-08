# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import configparser
from pathlib import Path

from modules.example import show_app as show_app_example

LOGGER = get_logger(__name__)

# Path to the directory where images are stored
static_dir = Path(__file__).parent / 'static' 

# Path to favicon
favicon_path = static_dir / 'Merz_Lifecare_Signet_Screen.png'

st.set_page_config(
    page_title="MLC Data View",
    page_icon=str(favicon_path),
    layout="wide",
)

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.toml file
config.read('.streamlit/config.toml')

hide_footer_style = """
<style>
.css-1lcbmhc {
    visibility: hidden;
}
.css-1s9zz97 {
    visibility: hidden;
}
.css-hi6a2p {
    padding: 0rem;
}
</style>
"""

st.markdown(hide_footer_style, unsafe_allow_html=True)

def run():

    if "example" in st.query_params:
        if st.query_params["example"] == "5":
            show_app_example()
    else:
        st.write("Keine App ausgewählt")
if __name__ == "__main__":
    run()
