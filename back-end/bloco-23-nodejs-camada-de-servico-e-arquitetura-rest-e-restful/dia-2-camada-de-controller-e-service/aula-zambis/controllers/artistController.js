const artistModel = require('../models/artistModel');

const create = async (req, res) => {
  const { name, genre } = req.body;
  const result = await artistModel.create({ name, genre });

  return res.status(201).json({ id: result.insertId, name, genre });
};

module.exports = {
  create,
}