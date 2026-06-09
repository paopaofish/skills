#!/bin/bash
# Script to list all MD files that need translation
find /workspace -name "*.md" -type f | grep -v "_CN.md" | grep -v "node_modules" | sort
