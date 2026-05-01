import json
from json_repair import repair_json
import jwt

def decode_cae_url(cae_jwt, attempt_to_repair_json=False):

    decoded_jwt = bytes.decode(jwt.utils.base64url_decode(cae_jwt))

    if attempt_to_repair_json:
        decoded_jwt = repair_json(decoded_jwt)

    return json.loads(decoded_jwt)
