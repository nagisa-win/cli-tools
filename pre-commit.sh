#!/bin/bash
# Pre-commit hook to generate project tree structure

# Generate tree structure
TREE_CONTENT=$(find . -not -path '*/\.*' -not -path '*node_modules*' | \
    sed 's|[^/]*/|- |g' | \
    sort -f | \
    sed 's/|- /├── /g')

# Update README.md
sed -i.bak '/<!--INSERT Tree of Files HERE-->/!b;n;c\'"$TREE_CONTENT" README.md
rm README.md.bak

# Add updated README.md to commit
git add README.md
