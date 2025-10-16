# HTML Processing API for Python
Aspose.HTML for Python via .NET Examples

[Product Page](https://products.aspose.com/html/python-net/) | [Docs](https://docs.aspose.com/html/python-net/) | [Demos](https://products.aspose.app/html/applications) | [AI Apps](https://products.aspose.ai/html/) | [API Reference](https://reference.aspose.com/html/) |[Blog](https://blog.aspose.com/categories/aspose.html-product-family/) | [Free Support](https://forum.aspose.com/c/html/29) | [Temporary License](https://purchase.aspose.com/temporary-license/)

This repository contains comprehensive examples for using the **Aspose.HTML for Python via .NET** library. The examples demonstrate various capabilities, including document conversion, rendering, editing, and data extraction.

[Aspose.HTML for Python via .NET](https://products.aspose.com/html/python-net/) is an advanced HTML processing API to perform a wide range of management and manipulation tasks within cross-platform applications.  It allows you to create new HTML files or load existing ones from various sources. Once a document is loaded, you can easily manipulate its content — add, modify, or remove HTML elements, render pages, and convert HTML to popular formats such as PDF, XPS, or image files.

## Key HTML API Features

Aspose.HTML for Python via .NET provides essential capabilities for working with HTML and related formats.

- [Create and Edit Documents](https://docs.aspose.com/html/python-net/working-with-documents/) – Build or modify HTML, XHTML, SVG, Markdown, EPUB, and MHTML files using a powerful DOM-based API.
- [Extract Data Efficiently](https://docs.aspose.com/html/python-net/data-extraction/) – Retrieve text, attributes, metadata, styles, and other elements using XPath or CSS selectors.
- [Convert to Multiple Formats](https://docs.aspose.com/html/python-net/converting-between-formats/) – Convert  HTML, SVG, MHTML, Markdown, or EPUB documents into PDF, XPS, DOCX, or image formats (PNG, JPEG, TIFF, etc.).
- [Customize Conversion Output](https://docs.aspose.com/html/python-net/fine-tuning-converters/) – Control page size, resolution, stylesheets, and resource management during the rendering process.
- [Automate and Secure Processing](https://docs.aspose.com/html/python-net/sandboxing/) – Use sandboxed environments and control execution for safe and isolated operations.
- Integrate Dynamic Content – Populate HTML templates with JSON or XML data and execute JavaScript for interactive workflows.
- Ensure Accessibility – Validate HTML documents against WCAG standards to maintain compliance.

## Read & Write Web Formats

- Web: HTML, XHTML, MHTML
- Other: SVG, MD (Markdown)

## Save HTML As

- Fixed Layout: PDF, XPS, DOCX
- Images: TIFF, JPEG, PNG, BMP, GIF, WEBP

## Read Formats

- EPUB

## Platform Independence

Aspose.HTML for Python via .NET is a cross-platform API that works seamlessly on **Windows, macOS, and Linux**. It supports both 32-bit and 64-bit Python environments (Python 3.5 or newer) and requires the .NET Core / .NET 5+ runtime. Once installed from PyPI, it enables developers to build and run HTML processing applications consistently across all major operating systems.

## Getting Started

Installation is quick and easy—just open a terminal and run:

```bash
pip install aspose-html-net
```
Already installed? Update with:

```bash
pip install --upgrade aspose-html-net
```
After installation, try running a few simple code snippets to see how easy it is to create, edit, and convert HTML documents directly from Python. For a more detailed exploration, visit the [Aspose.HTML for Python via .NET Documentation](https://docs.aspose.com/html/python-net/); you'll learn more about all the available features.

## Create an HTML File from Scratch

Aspose.HTML for Python via .NET allows you to create a new blank document and add content to this document.

```py
import aspose.html as ah

# Initialize an empty HTML document
with ah.HTMLDocument() as document:
    # Create a text node and add it to the document
    text = document.create_text_node("Hello, World!")
    document.body.append_child(text)

    # Save the document to a file
    document.save("create-new-document.html")
```

## Convert HTML to PDF

Aspose.HTML for Python via .NET allows you to convert HTML to PDF, XPS, DOCX, Markdown, XHTML, MHTML, JPEG, PNG, TIFF, and other file formats. The following snippet demonstrates the conversion from HTML to PDF:

```py
import aspose.html as ah
import aspose.html.converters as conv
import aspose.html.saving as sav

# Load an HTML document from a file or URL
document = ah.HTMLDocument("document.html")

# Initialize saving options
options = sav.PdfSaveOptions()

# Convert HTML to PDF
conv.Converter.convert_html(document, options, "output.pdf")
```

[Product Page](https://products.aspose.com/html/python-net/) | [Docs](https://docs.aspose.com/html/python-net/) | [Demos](https://products.aspose.app/html/applications) | [AI Apps](https://products.aspose.ai/html/) | [API Reference](https://reference.aspose.com/html/) |[Blog](https://blog.aspose.com/categories/aspose.html-product-family/) | [Free Support](https://forum.aspose.com/c/html/29) | [Temporary License](https://purchase.aspose.com/temporary-license/)