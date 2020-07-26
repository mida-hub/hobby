'use strict';
const express = require('express');
const router = express.Router();

router.get('/', (req, res, next) => {
  res.send('Some photos');
});

router.get('/:title', (req, res, next) => {
  // XSS
  // res.send(req.params.title);
  const title = req.params.title;
  // ここで、変数 title の内容をもとに存在チェック
  res.send('タイトル');
});

module.exports = router;