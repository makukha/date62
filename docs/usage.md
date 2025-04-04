<!-- docsub: begin -->
<!-- docsub: x toc tests/test_usage.py 'Usage.*' -->
* [Encode](#encode)
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x cases tests/test_usage.py 'Usage.*' -->
## Encode

Works for `datetime`, `date`, `time`, `int`, `float`, `Decimal`.

```pycon
>>> from datetime import datetime
>>> from decimal import Decimal
>>> import date62

>>> d = '2024-12-29 12:34:56.789012'
>>> dtm = datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')

>>> date62.encode(dtm)
'WeCTCYu'

>>> date62.encode(dtm, scut=True, prec=2)
'24CTCYuCj0C'

>>> date62.encode(dtm.date(), scut=True)
'24CT'

>>> date62.encode(dtm.time())
'CYu'

>>> date62.encode(dtm.time(), prec=3)
'CYuCj0C00'

>>> t = '1735468496.789012345678'
>>> date62.encode(Decimal(t), scut=True, prec=4)
'24CTAYuCj0C5ZAw'
```

<!-- docsub: end -->
