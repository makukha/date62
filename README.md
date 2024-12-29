# Date62
> Compact string-based date(time) format for logging, data engineering, and visualizations.

# Features

* Compact: 4 ASCII characters for date, 7 characters for datetime
* URL safe: uses Base62 encoding
* Natural sorting
* Semi-human-readable
* Dates cover range from 567-Jan-01 to 3843-Dec-31
* Arbitrary sub-second precision
* More readable shortcut form for values between 1970-Jan-01 and 2069-Dec-31
* Timezone info not supported at the moment


# Use cases

* Logging timestamps
* Visualize dates on charts
* Datetime-based file identifiers
* Sub-second-precision string labels


# Examples

| Date or Datetime     | Plain            | Date62                |
|----------------------|------------------|-----------------------|
| 2024-Dec-29          | `20241229`       | `WeCT` or `24CT`      |
| 2025-Jan-01          | `20250101`       | `Wf11` or `2511`      |
| 2025-Jan-01 00:01:02 | `20250101000102` | `Wf11012` or `2511012` |

## Sub-second precision
| Datetime                       | Plain                     | Date62          |
|--------------------------------|---------------------------|-----------------|
| 2025-Jan-01 00:01:02.345       | `20250101000102345`       | `Wf110125Z`     |
| 2025-Jan-01 00:01:02.345678    | `20250101000102345678`    | `25110125ZAw`   |
| 2025-Jan-01 00:01:02.345678012 | `20250101000102345678012` | `25110125ZAw0C` |


# Shortcut form


# CLI Reference
