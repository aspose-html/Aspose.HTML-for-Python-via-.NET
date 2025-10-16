import os
import io
import aspose.html as ah
import aspose.html.dom.svg as ahsvg

class CreateHTMLDocumentsExamples:

    def test_create_empty_html_document(self):
        #ExStart:CreateEmptyHTMLDocument
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "CreateEmptyHTMLDocument_out.html")
        document = ah.HTMLDocument()
        document.save(save_path)
        #ExEnd:CreateEmptyHTMLDocument

    def test_create_html_from_string(self):
        #ExStart:CreateHTMLFromString
        html_code = "<p>Hello, World!</p>"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document = ah.HTMLDocument(html_code, ".")
        save_path = os.path.join(output_dir, "CreateHTMLFromString_out.html")
        document.save(save_path)
        #ExEnd:CreateHTMLFromString

    def test_create_new_html_document(self):
        #ExStart:CreateNewHTMLDocument
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(output_dir, "CreateNewHTMLDocument_out.html")
        with ah.HTMLDocument() as document:
            text = document.create_text_node("Hello, World!")
            document.body.append_child(text)
            document.save(document_path)
        #ExEnd:CreateNewHTMLDocument

    def test_create_svg_document(self):
        #ExStart:CreateSVGDocument
        svg_content = "<svg xmlns='http://www.w3.org/2000/svg'><circle cx='50' cy='50' r='40'/></svg>"
        base_uri = "."
        content_stream = io.BytesIO(svg_content.encode('utf-8'))
        document = ahsvg.SVGDocument(content_stream, base_uri)
        document.save(os.path.join("output", "CreateSVGDocument_out.svg"))
        #ExEnd:CreateSVGDocument

    def test_load_html_from_file(self):
        #ExStart:FromFile
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        input_dir = "data/"
        document_path = os.path.join(input_dir, "document.html")
        save_path = os.path.join(output_dir, "FromFile_out.html")
        document = ah.HTMLDocument(document_path)
        document.save(save_path)
        #ExEnd:FromFile

    def test_load_html_from_stream(self):
        #ExStart:FromStream
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        content_stream = io.BytesIO(b"<p>Hello, World!</p>")
        base_uri = "."
        document = ah.HTMLDocument(content_stream, base_uri)
        document.save(os.path.join(output_dir, "FromStream_out.html"))
        #ExEnd:FromStream

    def test_load_from_url(self):
        #ExStart:LoadFromUrl
        document = ah.HTMLDocument("https://docs.aspose.com/html/files/aspose.html")
        print(document.document_element.outer_html)
        #ExEnd:LoadFromUrl

if __name__ == "__main__":
    tests = CreateHTMLDocumentsExamples()
    tests.test_create_empty_html_document()
    tests.test_create_html_from_string()
    tests.test_create_new_html_document()
    tests.test_create_svg_document()
    tests.test_load_html_from_file()
    tests.test_load_html_from_stream()
    tests.test_load_from_url()
    print("✅ Files created successfully.")