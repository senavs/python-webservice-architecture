MAX_LINE_LENGTH=120

autopep8 api/ \
  --max-line-length $MAX_LINE_LENGTH \
  --in-place \
  --recursive \
  2> /dev/null

black api/ \
  --line-length $MAX_LINE_LENGTH

isort api/ \
  --line-length $MAX_LINE_LENGTH \
  --multi-line-output 3 \
  --include-trailing-comma \
  --force-grid-wrap 0 \
  --use-parentheses \
  --ensure-newline-before-comments \
  --py 310 \
  2> /dev/null

flake8 api/ \
  --max-line-length $MAX_LINE_LENGTH \
  --exclude ".git, --pycache--" \
  --extend-ignore "E203" \
  --count