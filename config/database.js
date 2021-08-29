// const { createPool } = require('mysql');

// const pool = createPool({
//     port: '3306',
//     host: 'localhost',
//     user: 'root',
//     password: '',
//     database: 'vello_food',
//     connectionLimit: 10
// });
const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;


const pool = MongoClient.connect("mongodb+srv://Testshop:Alwan123@testshop.83kst.mongodb.net/TestShop", function(err, client) {
      if(err) throw err;
        // Connect to the database, if not, create it automatically
        let db = client.db('laoxie');
    });

module.exports = pool;