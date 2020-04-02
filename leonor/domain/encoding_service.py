import json
import gzip
import base64
import time


class EncodingService:
    def encode(self, input_data):
        input_data['timestamp'] = time.time()
        json_dump = json.dumps(input_data)
        compressed = gzip.compress(json_dump.encode())
        return base64.b64encode(compressed).decode()
