# FontFixer

FontFixer is a Python-based utility designed to correct and manage font issues in Windows, ensuring clear and consistent text display across applications. It provides functionalities to list installed fonts, verify font entries in the Windows registry, and reinstall fonts to fix common font issues.

## Features

- **List Fonts**: Displays all fonts currently installed in the Windows system font directory.
- **Verify Font Registry**: Checks the Windows registry to ensure font entries are correct.
- **Reinstall Fonts**: Reinstalls specified fonts to fix display issues.
- **Fix Common Issues**: Automates the process of fixing common font issues by reinstalling all fonts.

## Prerequisites

- Python 3.x
- Windows operating system

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fontfixer.git
   ```
2. Navigate to the directory:
   ```bash
   cd fontfixer
   ```

## Usage

Run the `font_fixer.py` script using Python:

```bash
python font_fixer.py
```

This will list all available fonts, verify the registry, and attempt to fix any font issues by reinstalling fonts.

## Notes

- Administrator privileges may be required to modify font settings and the Windows registry.
- The script currently supports TrueType (`.ttf`) and OpenType (`.otf`) fonts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.