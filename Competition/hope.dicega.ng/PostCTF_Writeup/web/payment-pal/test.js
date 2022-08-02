const crypto = require("crypto");

const KEY = crypto.randomBytes(32);

const encrypt = (data) => {
  const iv = Buffer.from(crypto.randomBytes(16));
  const cipher = crypto.createCipheriv('aes-256-gcm', KEY, iv);
  let enc = cipher.update(data, 'utf8', 'base64');
  enc += cipher.final('base64');
  return [enc, iv.toString('base64'), cipher.getAuthTag().toString('base64')].join(".");
};

const decrypt = (data) => {
  try {
    const [enc, iv, authTag] = data.split(".").map(d => Buffer.from(d, 'base64'));
    const decipher = crypto.createDecipheriv('aes-256-gcm', KEY, iv);
    decipher.setAuthTag(authTag);
    let dec = decipher.update(enc, 'base64', 'utf8');
    return dec;
  }
  catch(err) {
    return null;
  }
};

console.log(encrypt("12312312312"));