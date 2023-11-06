code.language: javascript
code.language: typescript
code.language: javascriptreact
code.language: typescriptreact
-
tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_keywords
tag(): user.code_libraries
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_lambda
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_private_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_variable_formatter = "PRIVATE_CAMEL_CASE"

is strict equal:            " === "
is strict not equal:        " !== "
# op null else:               " ?? "

<user.operator> or quest:   " ?? "
<user.operator> (string | quote) var: user.insert_between("${", "}")
<user.operator> spread:     "..."

<user.operator> const:      "const "
<user.operator> let:        "let "
<user.operator> var:        "var "
<user.operator> export:     "export "
<user.operator> async:      'async '
<user.operator> await:      "await "
<user.operator> comment [<user.text>]: '// {text or ""}'


(add | chain) length:       ".length"
(add | chain) {user.code_common_member_function}:
    user.insert_between(".{code_common_member_function}(", ")")
(add | chain) {user.code_common_member_function_with_lambda}:
    user.cursorless_insert_snippet(".{code_common_member_function_with_lambda}(($args) => ($value))")
(add | chain) {user.code_common_member_function_with_lambda} block:
    user.cursorless_insert_snippet(".{code_common_member_function_with_lambda}(($args) => {{\n\t$body\n}})")
(add | chain) {user.code_common_member_function_with_lambda} short:
    user.insert_between(".{code_common_member_function_with_lambda}(", ")")
(add | chain) {user.code_common_member_function_with_lambda} <phrase>:
    name = user.formatted_text(phrase, "PRIVATE_CAMEL_CASE")
    user.cursorless_insert_snippet(".{code_common_member_function_with_lambda}(({name}) => ($value))")
(add | chain) {user.code_common_member_function_with_lambda} block <phrase>:
    name = user.formatted_text(phrase, "PRIVATE_CAMEL_CASE")
    user.cursorless_insert_snippet(".{code_common_member_function_with_lambda}(({name}) => {{\n\t$body\n}})")

(add | chain) sort:
    user.cursorless_insert_snippet(".sort((a, b) => $value)")
(add | chain) reduce:
    user.cursorless_insert_snippet(".reduce((prev, cur) => $cur, $initialValue)")
(add | chain) reduce block:
    user.cursorless_insert_snippet(".reduce((prev, cur) => {{\n\t\t$body\n\t}},\n\t$initialValue\n)")
(add | chain) reduce short:
    user.cursorless_insert_snippet(".reduce($function, $initialValue)")

dot {user.code_common_member_function}:
    user.insert_between(".{code_common_member_function}(", ")")

from import:                user.insert_between(' from  "', '"')
