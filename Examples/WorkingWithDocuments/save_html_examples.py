import os
import aspose.html as ah
import aspose.html.saving as sav
import aspose.html.dom.svg as ahsvg
from aspose.html.saving.resourcehandlers import *

class SaveHTMLExamples:

    def test_save_html_to_md(self):
        #ExStart:SaveHtmlToMd
        data_dir = "data"
        output_dir = "output/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        input_path = os.path.join(data_dir, "document.html")
        output_path = os.path.join(output_dir, "html-to-markdown.md")
        document = ah.HTMLDocument(input_path)
        document.save(output_path, sav.HTMLSaveFormat.MARKDOWN)
        #ExEnd:SaveHtmlToMd

    def test_save_html_to_mhtml(self):
        #ExStart:SaveHtmlToMhtml
        output_dir = 'output'
        document_path = os.path.join(output_dir, 'save-html-to-mhtml.mht')
        os.makedirs(output_dir, exist_ok=True)
        with open('document.html', 'w') as file:
            file.write("<p>Hello, World!</p>"
                "<a href='linked-file.html'>linked file</a>")
        with open('linked-file.html', 'w') as file:
            file.write("<p>Hello, linked file!</p>")
        with ah.HTMLDocument('document.html') as document:
            document.save(document_path, sav.HTMLSaveFormat.MHTML)
        #ExEnd:SaveHtmlToMhtml

    def test_save_html(self):
        #ExStart:SaveHtml
        output_dir = "output/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        document_path = os.path.join(output_dir, "create-new-document.html")
        with ah.HTMLDocument() as document:
            text = document.create_text_node("Hello, World!")
            document.body.append_child(text)
            document.save(document_path)
        #ExEnd:SaveHtml

    def test_save_svg(self):
        #ExStart:SaveSvg
        output_dir = 'output'
        document_path = os.path.join(output_dir, 'save-html-to-svg.svg')
        os.makedirs(output_dir, exist_ok=True)
        svg_code = """
        <svg xmlns='http://www.w3.org/2000/svg' height='400' width='300'>
            <path stroke="#a06e84" stroke-width="3" fill="#74aeaf" d="  
            M 150,50 L 150, 300
            M 120,100 L 150,50 L 180, 100
            M 110,150 L 150,90 L 190, 150
            M 90,220 L 150,130 L 210, 220
            M 70,300 L 150,190 L 230, 300
            M 110,310 L 150,240 L 190, 310
            " />
        </svg>
        """
        document = ahsvg.SVGDocument(svg_code, '.')
        document.save(document_path)
        #ExEnd:SaveSvg

    def test_save_to_file(self):
        #ExStart:SaveToFile
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        document_path = os.path.join(output_dir, "save-with-linked-file.html")
        with open(document_path, "w") as file:
            file.write("<p>Hello, World!</p>" +
                "<a href='linked.html'>linked file</a>")
        with open(os.path.join(output_dir, "linked.html"), "w") as file:
            file.write("<p>Hello, linked file!</p>")
        document = ah.HTMLDocument(document_path)
        options = sav.HTMLSaveOptions()
        options.resource_handling_options.max_handling_depth = 1
        output_path = os.path.join(output_dir, "save-with-linked-file_out.html")
        document.save(output_path, options)
        #ExEnd:SaveToFile

    def test_save_to_local_storage(self):
        #ExStart:SaveToLocalStorage
        data_dir = "data"
        input_path = os.path.join(data_dir, "with-resources.html")
        custom_out_dir = os.path.join(os.getcwd(), "../save-html-res/")
        doc = ah.HTMLDocument(input_path)
        save_options = sav.HTMLSaveOptions()
        save_options.resource_handling_options.max_handling_depth = 2
        output_path = os.path.join(custom_out_dir, "with-resources_out.html")
        doc.save(output_path, save_options)
        #ExEnd:SaveToLocalStorage

if __name__ == "__main__":
    tests = SaveHTMLExamples()
    tests.test_save_html_to_md()
    tests.test_save_html_to_mhtml()
    tests.test_save_html()
    tests.test_save_svg()
    tests.test_save_to_file()
    tests.test_save_to_local_storage()
    print("✅ Files created successfully.")