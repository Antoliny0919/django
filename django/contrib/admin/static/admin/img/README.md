# Information about icons in this directory

## License

All icons in this directory are provided by
[Font Awesome Free](https://fontawesome.com), version 7.2.0.

- The icons are licensed under the [Creative Commons Attribution 4.0
  International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/)
  license.
- This license allows you to use, modify, and distribute the icons, provided
  proper attribution is given.

## Usage

- You may use, modify, and distribute the icons in this repository in
  compliance with the [Creative Commons Attribution 4.0 International
  (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/) license.

## Modifications

- These icons have been resized, recolored, or otherwise modified to fit the
  requirements of this project.

- These modifications alter the appearance of the original icons but remain
  covered under the terms of the
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Contributing SVG Icons

To ensure visual consistency, traceability, and proper license attribution,
follow these guidelines. This applies when adding or modifying icons.

## ⚠️ Important: Changing Font Awesome Version

If you update to a different Font Awesome version, you must **update all SVG
files** and **comments inside the files** to reflect the new version number and
licensing URL accordingly. For example:

* Original:
```xml
<!--!Font Awesome Free 7.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2026 Fonticons, Inc.-->
```
* Updated:
```xml
<!--!Font Awesome Free X.Y.Z by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright YYYY Fonticons, Inc.-->
```

## Adding a new icon

1. Use only [Font Awesome Free Icons](https://fontawesome.com/icons).
2. Save the icon as an .svg file in this directory.
3. Include the following attribution comment at the top of the file (do not
   change it):
```xml
<!--!Font Awesome Free 7.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.-->
```
4. Right before the `<path>` element, add the following metadata comment with
   the appropriate values:
```xml
<!--
  Icon Name: [icon-name]
  Icon Family: [classic | sharp | brands | etc.]
  Icon Style: [solid | regular | light | thin | duotone | etc.]
-->
```

### Example SVG Structure

```xml
<svg width="13" height="13" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640">
  <!--!Font Awesome Free v7.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2026 Fonticons, Inc.-->
  <!--
    Icon Name: plus
    Icon Family: classic
    Icon Style: solid
  -->
  <path fill="#5fa225" stroke="#5fa225" stroke-width="30" d="M352 128C352 110.3 337.7 96 320 96C302.3 96 288 110.3 288 128L288 288L128 288C110.3 288 96 302.3 96 320C96 337.7 110.3 352 128 352L288 352L288 512C288 529.7 302.3 544 320 544C337.7 544 352 529.7 352 512L352 352L512 352C529.7 352 544 337.7 544 320C544 302.3 529.7 288 512 288L352 288L352 128z"/>
</svg>
```
