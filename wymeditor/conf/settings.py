from django.conf import settings

DEFAULT_WYM_TOOLS = ",\n".join([
    "{'name': 'Bold', 'title': 'Strong', 'css': 'wym_tools_strong'}",
    "{'name': 'Italic', 'title': 'Emphasis', 'css': 'wym_tools_emphasis'}",
    "{'name': 'Superscript', 'title': 'Superscript', 'css': 'wym_tools_superscript'}",
    "{'name': 'Subscript', 'title': 'Subscript', 'css': 'wym_tools_subscript'}",
    "{'name': 'InsertOrderedList', 'title': 'Ordered_List', 'css': 'wym_tools_ordered_list'}",
    "{'name': 'InsertUnorderedList', 'title': 'Unordered_List', 'css': 'wym_tools_unordered_list'}",
    "{'name': 'Indent', 'title': 'Indent', 'css': 'wym_tools_indent'}",
    "{'name': 'Outdent', 'title': 'Outdent', 'css': 'wym_tools_outdent'}",
    "{'name': 'Undo', 'title': 'Undo', 'css': 'wym_tools_undo'}",
    "{'name': 'Redo', 'title': 'Redo', 'css': 'wym_tools_redo'}",
    "{'name': 'Paste', 'title': 'Paste_From_Word', 'css': 'wym_tools_paste'}",
    "{'name': 'ToggleHtml', 'title': 'HTML', 'css': 'wym_tools_html'}",
    "{'name': 'CreateLink', 'title': 'Link', 'css': 'wym_tools_link'}",
    "{'name': 'Unlink', 'title': 'Unlink', 'css': 'wym_tools_unlink'}",
    "{'name': 'InsertImage', 'title': 'Image', 'css': 'wym_tools_image'}",
    "{'name': 'InsertTable', 'title': 'Table', 'css': 'wym_tools_table'}",
    "{'name': 'Preview', 'title': 'Preview', 'css': 'wym_tools_preview'}",
])
WYM_TOOLS = getattr(settings, 'WYMEDITOR_TOOLS', DEFAULT_WYM_TOOLS)

DEFAULT_WYM_CONTAINERS = ",\n".join([
    "{'name': 'P', 'title': 'Paragraph', 'css': 'wym_containers_p'}",
    "{'name': 'H1', 'title': 'Heading_1', 'css': 'wym_containers_h1'}",
    "{'name': 'H2', 'title': 'Heading_2', 'css': 'wym_containers_h2'}",
    "{'name': 'H3', 'title': 'Heading_3', 'css': 'wym_containers_h3'}",
])
WYM_CONTAINERS = getattr(settings, 'WYMEDITOR_CONTAINERS', DEFAULT_WYM_CONTAINERS)

DEFAULT_WYM_CLASSES = ",\n".join([
    u"{'name': 'center-align', 'title': 'Align center', 'expr': 'p'}",
    u"{'name': 'right-align', 'title': 'Align right', 'expr': 'p'}",
    u"{'name': 'marginless', 'title': 'Margin less', 'expr': 'p'}",
    u"{'name': 'float-right', 'title': 'Float right', 'expr': 'p'}",
    u"{'name': 'float-left', 'title': 'Float left', 'expr': 'p'}",
])
WYM_CLASSES = getattr(settings, 'WYMEDITOR_CLASSES', DEFAULT_WYM_CLASSES)

DEFAULT_WYM_STYLES = ",\n".join([
    "{'name': '.center-align', 'css': 'text-align: center'}",
    "{'name': '.right-align', 'css': 'text-align: right'}",
    "{'name': '.marginless', 'css': 'margin-bottom: 0'}",
    "{'name': '.float-right', 'css': 'float: right'}",
    "{'name': '.float-left', 'css': 'float: left'}",
])
WYM_STYLES = getattr(settings, 'WYMEDITOR_STYLES', DEFAULT_WYM_STYLES)