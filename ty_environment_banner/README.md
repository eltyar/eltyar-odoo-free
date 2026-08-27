# Environment Banner

Server-rendered warning banner for staging and non-production Odoo databases.
A colored bar is painted above the navbar so users immediately see they are
not working on live data.

## Features

- Automatic detection: neutralized databases and database names containing
  `staging`, `test` or `demo`
- Manual override with a single system parameter (`on` / `off` / `auto`)
- Custom banner text and background color
- Pure server-side QWeb: no JavaScript, no assets, depends only on `web`
- Compatible with Odoo 14 through 19

## Configuration

Set under *Settings > Technical > System Parameters*:

| Parameter | Default | Description |
|---|---|---|
| `environment_banner.mode` | `auto` | `auto`, `on` (always show) or `off` (never show) |
| `environment_banner.label` | *built-in message* | Custom banner text |
| `environment_banner.color` | `#D0442C` | Banner background color (CSS color) |

## License

LGPL-3. Author: Mohamed Eltayar — <https://eltyar.com>
