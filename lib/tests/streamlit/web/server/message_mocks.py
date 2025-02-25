# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Shared protobuf message mocking utilities."""

from streamlit import RootContainer
from streamlit.cursor import make_delta_path
from streamlit.elements import legacy_data_frame
from streamlit.elements.arrow import Data
from streamlit.logger import get_logger
from streamlit.proto.ForwardMsg_pb2 import ForwardMsg

LOGGER = get_logger(__name__)


def create_dataframe_msg(df: Data, id: int = 1) -> ForwardMsg:
    """Create a mock legacy_data_frame ForwardMsg."""
    msg = ForwardMsg()
    msg.metadata.delta_path[:] = make_delta_path(RootContainer.SIDEBAR, (), id)
    legacy_data_frame.marshall_data_frame(df, msg.delta.new_element.data_frame)
    return msg
