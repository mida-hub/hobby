'use strict';
const express = require('express');
const router = express.Router();

router.get('/', function(req, res, next) {
  console.log('schedules');
});

module.exports = router;
