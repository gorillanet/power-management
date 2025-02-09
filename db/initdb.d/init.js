db = db.getSiblingDB('data');
db.createCollection("battery")
db.battery.createIndex(
    { "insertDate": 1 },
    { expireAfterSeconds: 2592000 }
 )
db.createCollection("solar")
db.solar.createIndex(
    { "insertDate": 1 },
    { expireAfterSeconds: 604800 }
 )