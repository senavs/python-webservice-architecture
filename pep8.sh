MAX_LINE_LENGTH=120

autopep8 app/ \
  --max-line-length $MAX_LINE_LENGTH \
  --in-place \
  --recursive \
  2> /dev/null

black app/ \
  --line-length $MAX_LINE_LENGTH

isort app/ \
  --line-length $MAX_LINE_LENGTH \
  -m 3 \
  --trailing-comma \
  --force-grid-wrap 0 \
  --use-parentheses \
  --ensure-newline-before-comments \
  --py 310

flake8 app/ \
  --max-line-length $MAX_LINE_LENGTH \
  --exclude ".git, --pycache--" \
  --extend-ignore "E203" \
  --count