var mongoose = require("mongoose");
var Schema = mongoose.Schema;

var GameSchema = new Schema({
  console: {
    type: String
  },
  name: {
    type: String
  },
  image: {
    type: String
  },
  sales: {
    type: String
  }
});

module.exports = mongoose.model("Game", GameSchema);