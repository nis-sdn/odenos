# -*- coding:utf-8 -*-

# Copyright 2015 NEC Corporation.                                          #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License");          #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#   http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #

from org.o3project.odenos.core.component.network.packet.ofp_in_packet\
    import OFPInPacket

import unittest


class InPacketTest(unittest.TestCase):
    value = None
    result = None

    def setUp(self):
        self.target = OFPInPacket("ofp_in_packet_id",
                                  "OFPInPacket",
                                  "ofp_in_packet_attributes",
                                  "ofp_in_packet_node",
                                  "ofp_in_packet_port",
                                  {"type": "OFPFlowMatch",
                                   "in_port": "123456",
                                   "in_node": "123456789"},
                                  "ofp_in_packet_data")

    def tearDown(self):
        self.target = None

    def test_constructor(self):
        self.assertEqual(self.target._body[self.target.PACKET_ID],
                         "ofp_in_packet_id")
        self.assertEqual(self.target._body[self.target.TYPE],
                         "OFPInPacket")
        self.assertEqual(self.target._body[self.target.ATTRIBUTES],
                         "ofp_in_packet_attributes")
        self.assertEqual(self.target._body[self.target.NODE],
                         "ofp_in_packet_node")
        self.assertEqual(self.target._body[self.target.PORT],
                         "ofp_in_packet_port")
        self.assertEqual(self.target._body[self.target.HEADER],
                         {"type": "OFPFlowMatch",
                          "in_port": "123456",
                          "in_node": "123456789"})
        self.assertEqual(self.target._body[self.target.DATA],
                         "ofp_in_packet_data")

    def test_create_from_packed(self):

        self.value = {"packet_id": "0123",
                      "type": "OFPInPacket",
                      "attributes": "0789",
                      "node": "9870",
                      "port": "6540",
                      "header": {"type": "OFPFlowMatch",
                                 "in_port": "123456",
                                 "in_node": "123456789"},
                      "data": "0147"}

        self.result = OFPInPacket.create_from_packed(self.value)
        self.assertEqual(self.result._body[self.target.PACKET_ID],
                         "0123")
        self.assertEqual(self.result._body[self.target.TYPE],
                         "OFPInPacket")
        self.assertEqual(self.result._body[self.target.ATTRIBUTES],
                         "0789")
        self.assertEqual(self.result._body[self.target.NODE],
                         "9870")
        self.assertEqual(self.result._body[self.target.PORT],
                         "6540")
        self.assertEqual(self.result._body[self.target.HEADER]._body,
                         {"type": "OFPFlowMatch",
                          "in_port": "123456",
                          "in_node": "123456789"})
        self.assertEqual(self.result._body[self.target.DATA],
                         "0147")

    def test_packed_object(self):
        self.value = {"packet_id": "0123",
                      "type": "OFPInPacket",
                      "attributes": "0789",
                      "node": "9870",
                      "port": "6540",
                      "header": {"type": "OFPFlowMatch",
                                 "in_port": "123456",
                                 "in_node": "123456789"},
                      "data": "0147"}

        self.create = OFPInPacket.create_from_packed(self.value)

        self.result = self.create.packed_object()

        self.assertEqual(self.result[self.target.PACKET_ID],
                         "0123")
        self.assertEqual(self.result[self.target.TYPE],
                         "OFPInPacket")
        self.assertEqual(self.result[self.target.ATTRIBUTES],
                         "0789")
        self.assertEqual(self.result[self.target.NODE],
                         "9870")
        self.assertEqual(self.result[self.target.PORT],
                         "6540")
        self.assertEqual(self.result[self.target.HEADER],
                         {"type": "OFPFlowMatch",
                          "in_port": "123456",
                          "in_node": "123456789"})
        self.assertEqual(self.result[self.target.DATA],
                         "0147")

if __name__ == '__main__':
    unittest.main()
