# Gendiff - Configuration Files Comparison Tool

[![Actions Status](https://github.com/VVP04/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VVP04/python-project-50/actions)
[![Python CI](https://github.com/VVP04/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/VVP04/python-project-50/actions/workflows/main.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/963673bcabea6734e24a/test_coverage.svg)](https://codeclimate.com/github/VVP04/python-project-50/test_coverage)

A CLI utility for finding differences between configuration files in JSON and YAML formats. Supports multiple output formats for various use cases.

## Key Features

- 🔍 **Deep comparison** of nested structures
- 📁 **Multi-format support**: JSON and YAML inputs
- 🎨 **Customizable output**:
  - `stylish`
  - `plain`
  - `json`
- ✅ **Validation** of input files
- 📊 **Detailed change tracking**: added, removed, updated, and intact values

## Get started

1. Clone the repository:
```bash
git clone https://github.com/VVP04/python-project-50.git
cd python-project-50
```

2. Run the tool:
```bash
gendiff [options] <filepath1> <filepath2>
```

Options:
```
-f, --format [stylish|plain|json]  Output format (default: stylish)
-h, --help                         Show help
```

## Demo

#### Comparison of flat JSON files
[![asciicast](https://asciinema.org/a/708426.svg)](https://asciinema.org/a/708426)

#### Comparison of flat YAML files
[![asciicast](https://asciinema.org/a/709193.svg)](https://asciinema.org/a/709193)

#### Stylish-formatted comparison of nested files
[![asciicast](https://asciinema.org/a/710981.svg)](https://asciinema.org/a/710981)

#### Plain-formatted comparison of nested files
[![asciicast](https://asciinema.org/a/711171.svg)](https://asciinema.org/a/711171)

#### JSON-formatted comparison of nested files
[![asciicast](https://asciinema.org/a/711195.svg)](https://asciinema.org/a/711195)

## Development Setup

```bash
make install   # Install dependencies
make test      # Run tests
make lint      # Check code quality
```

## Project Goals

This project was created as part of Hexlet's Python Developer course to demonstrate:
- Advanced file parsing capabilities
- Complex data structure comparison
- Clean code architecture
- Comprehensive testing practices
- Professional CI/CD setup