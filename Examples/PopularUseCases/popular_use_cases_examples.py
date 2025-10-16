import os
import unittest
import aspose.html as ah
import aspose.html as html
import aspose.html.drawing as dr

class HowToArticlesExamplesTests(unittest.TestCase):

    def test_change_background_color(self):
        #ExStart:ChangeBgColor
        output_dir = "output/"
        save_path = os.path.join(output_dir, "change-background-color-inline-css.html")
        data_dir = "data/"
        document_path = os.path.join(data_dir, "file.html")
        document = ah.HTMLDocument(document_path)
        body = document.get_elements_by_tag_name("body")[0]
        current_style = body.get_attribute("style") or ""
        new_style = current_style + "background-color: lavenderblush"
        body.set_attribute("style", new_style)
        document.save(save_path)
        #ExEnd:ChangeBgColor

    def test_change_background_color_using_internal_css(self):
        #ExStart:ChangeBackgroundColorUsingInternalCss
        output_dir = "output/"
        save_path = os.path.join(output_dir, "change-background-color-internal-css.html")
        data_dir = "data/"
        document_path = os.path.join(data_dir, "file.html")
        document = ah.HTMLDocument(document_path)
        body = document.get_elements_by_tag_name("body")[0]
        current_style = body.get_attribute("style") or ""
        updated_style = " ".join(prop for prop in current_style.split(";") if not prop.strip().startswith("background-color"))
        body.set_attribute("style", updated_style)
        style = document.create_element("style")
        style.text_content = "body { background-color: rgb(255 240 245) }"
        head = document.get_elements_by_tag_name("head")[0]
        head.append_child(style)
        document.save(save_path)
        #ExEnd:ChangeBackgroundColorUsingInternalCss

    def test_change_background_color_table_cells(self):
        #ExStart:ChangeBackgroundColorTableCells
        data_dir = "data"
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "table.html")
        save_path = os.path.join(output_dir, "change-table-cell-background.html")
        with ah.HTMLDocument(document_path) as doc:
            cells = doc.get_elements_by_tag_name("td")
            print("Found cells:", cells.length)
            for i in range(cells.length):
                cell = cells[i]
                color = "#f3d2dd" if i % 2 == 0 else "#bfd3f8"
                cell.set_attribute("style", f"background-color: {color};")
            doc.save(save_path)
        print("Saved to:", save_path)
        #ExEnd:ChangeBackgroundColorTableCells

    def test_change_border_color_four_sides(self):
        #ExStart:ChangeBorderColorForFourSides
        data_dir = "data"
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "file.html")
        save_path = os.path.join(output_dir, "change-four-border-color.html")
        with ah.HTMLDocument(document_path) as document:
            header = document.get_elements_by_tag_name("h1")[0]
            header.set_attribute("style", "border-style: solid; border-color: red blue green gray;")
            document.save(save_path)
        print("File saved to:", save_path)
        #ExEnd:ChangeBorderColorForFourSides

    def test_change_border_color_for_h1(self):
        #ExStart:ChangeBorderColorForH1
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "change-border-color.html")
        data_dir = "data"
        document_path = os.path.join(data_dir, "file.html")
        with ah.HTMLDocument(document_path) as document:
            header = document.get_elements_by_tag_name("h1")[0]
            header.set_attribute("style", "color: #8B0000; border-style: solid; border-color: rgb(220,30,100);")
            document.save(save_path)
        print("File saved to:", save_path)
        #ExEnd:ChangeBorderColorForH1

    def test_change_border_color_internal_css(self):
        #ExStart:ChangeBorderColorInternalCss
        data_dir = "data"
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "file.html")
        save_path = os.path.join(output_dir, "change-border-color-internal-css.html")
        with ah.HTMLDocument(document_path) as document:
            style = document.create_element("style")
            style.text_content = "p {border-style: solid; border-color: rgb(220,30,100); }"
            head = document.get_elements_by_tag_name("head")[0]
            head.append_child(style)
            document.save(save_path)
        print("File saved to:", save_path)
        #ExEnd:ChangeBorderColorInternalCss

    def test_change_p_background_color(self):
        #ExStart:ChangePBackgroundColor
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "change-background-color-p-inline-css.html")
        data_dir = "data/"
        document_path = os.path.join(data_dir, "file.html")
        with ah.HTMLDocument(document_path) as doc:
            paragraph = doc.get_elements_by_tag_name("p")[0]
            paragraph.set_attribute("style", "background-color: #fff0f5;")
            doc.save(save_path)
        #ExEnd:ChangePBackgroundColor

    def test_change_table_border_color_internal_css(self):
        #ExStart:ChangeTableBorderColorInternalCss
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        data_dir = "data"
        document_path = os.path.join(data_dir, "table.html")
        save_path = os.path.join(output_dir, "change-table-border-color-internal-css.html")
        with ah.HTMLDocument(document_path) as doc:
            style = doc.create_element("style")
            style.text_content = "table { border-style:none; border-color:none }"
            head = doc.get_elements_by_tag_name("head")[0]
            head.append_child(style)
            doc.save(save_path)
        #ExEnd:ChangeTableBorderColorInternalCss

    def test_change_table_border_color(self):
        #ExStart:ChangeTableBorderColor
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        data_dir = "data"
        document_path = os.path.join(data_dir, "table.html")
        save_path = os.path.join(output_dir, "change-table-border-color-inline-css.html")
        with ah.HTMLDocument(document_path) as doc:
            element = doc.query_selector("table")
            element.set_attribute("style", "border: 2px #0000ff solid;")
            doc.save(save_path)
        #ExEnd:ChangeTableBorderColor

    def test_change_text_color_internal_css(self):
        #ExStart:ChangeTextColorInternalCss
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        data_dir = "data"
        document_path = os.path.join(data_dir, "file.html")
        save_path = os.path.join(output_dir, "change-text-color-internal-css.html")
        with ah.HTMLDocument(document_path) as doc:
            style = doc.create_element("style")
            style.text_content = "p { color: #8B0000 }"
            head = doc.get_elements_by_tag_name("head")[0]
            head.append_child(style)
            doc.save(save_path)
        #ExEnd:ChangeTextColorInternalCss

    def test_change_text_color_with_condition(self):
        #ExStart:ChangeTextColorWithCondition
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "conditional-text-color.html")
        html_content = """
            <html>
            <body>
            <p>Score: 85</p>
            <p>Score: 42</p>
            <p>Score: 73</p>
            </body>
            </html>
            """
        with ah.HTMLDocument(html_content, ".") as doc:
            paragraphs = doc.get_elements_by_tag_name("p")
            for p in paragraphs:
                text = p.text_content
                score = int(text.split(":")[1].strip())
                color = "green" if score >= 70 else "red"
                p.set_attribute("style", f"color: {color};")
            doc.save(save_path)
        #ExEnd:ChangeTextColorWithCondition

    def test_change_text_color(self):
        #ExStart:ChangeTextColor
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "change-text-color-inline-css.html")
        data_dir = "data"
        document_path = os.path.join(data_dir, "file.html")
        with ah.HTMLDocument(document_path) as doc:
            paragraph = doc.get_elements_by_tag_name("p")[0]
            paragraph.set_attribute("style", "color: #8B0000;")
            doc.save(save_path)
        #ExEnd:ChangeTextColor

    def test_px_to_cm(self):
        #ExStart:PxToCm
        px = dr.Unit.from_pixels(1000.0)  # Specify the unit type explicitly
        cm = px.get_value(dr.UnitType.CM)  # Convert to centimeters
        print(cm)
        #ExEnd:PxToCm

    def test_check_text_content(self):
        #ExStart:CheckEmptyTextContent
        with html.HTMLDocument("document.html") as document:
            body = document.body
            if body.text_content and not body.text_content.isspace():
                print("Non-empty HTML elements found")
            else:
                print("No child nodes found in the body element.")
        #ExEnd:CheckEmptyTextContent

if __name__ == "__main__":
    tests = HowToArticlesExamplesTests()
    tests.test_change_background_color()
    tests.test_change_background_color_using_internal_css()
    tests.test_change_background_color_table_cells()
    tests.test_change_border_color_four_sides()
    tests.test_change_border_color_for_h1()
    tests.test_change_border_color_internal_css()
    tests.test_change_p_background_color()
    tests.test_change_table_border_color_internal_css()
    tests.test_change_table_border_color()
    tests.test_change_text_color_internal_css()
    tests.test_change_text_color_with_condition()
    tests.test_change_text_color()
    tests.test_px_to_cm()
    tests.test_check_text_content()
    print("✅ All how-to-articles example tests executed successfully.")