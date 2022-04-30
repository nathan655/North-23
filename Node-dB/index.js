const {Storage} = require('@google-cloud/storage');

const storage = new Storage();
const bucket = storage.bucket(CLOUD_BUCKET);