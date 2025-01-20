# pathto

A fast command-line utility to search for files and directories across your entire system. Performs case-insensitive searches, handles filenames with spaces, and automatically skips system directories for better performance.

## Installation

1. Clone this repository
```bash
git clone https://github.com/Jaisinh/pathto
```
2. Shift the pathto.py
```bash
mv pathto.py /usr/local/bin/pathto
```

3. Make it executable:
```bash
sudo chmod +x /usr/local/bin/pathto
```

## Usage

Basic usage:
```bash
pathto <name>
```

Search for items with spaces in name:
```bash
pathto "My Documents"
```
or
```bash
pathto My Documents
```

## Examples

```bash
$ pathto document
Searching for files or folders named 'document'...
(This may take a while as it searches all directories...)

Found the following matches:
Directory: /Users/username/Documents
File: /Users/username/Documents/document.pdf
```

## Features

- Searches entire system recursively
- Case-insensitive matching
- Handles filenames with spaces
- Shows whether matches are files or directories
- Automatically skips system directories and hidden files
- Fast performance through optimized directory traversal
- Error handling for permission issues

## Requirements

- Python 3.x
- Unix-like operating system (Linux, macOS)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License 
