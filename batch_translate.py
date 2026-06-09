#!/usr/bin/env python3
"""
Batch translate Markdown files to Chinese.
This script processes all English MD files and creates Chinese versions.
"""

import os
import re
from pathlib import Path

# Translation dictionary for common terms
TRANSLATIONS = {
    # Common technical terms
    "Skill": "技能",
    "Skills": "技能",
    "skill": "技能",
    "skills": "技能",
    "Agent": "Agent",
    "agent": "agent",
    "Code": "代码",
    "code": "代码",
    "Test": "测试",
    "test": "测试",
    "Tests": "测试",
    "tests": "测试",
    "Testing": "测试",
    "testing": "测试",
    "Development": "开发",
    "development": "开发",
    "Engineer": "工程师",
    "engineer": "工程师",
    "Engineering": "工程",
    "engineering": "工程",
    "Productivity": "生产力",
    "productivity": "生产力",
    "Deprecated": "已弃用",
    "deprecated": "已弃用",
    "In Progress": "进行中",
    "in-progress": "进行中",
    "Personal": "个人",
    "personal": "个人",
    "Misc": "杂项",
    "misc": "杂项",
    "README": "README",
    "Context": "上下文",
    "context": "上下文",
    "Domain": "领域",
    "domain": "领域",
    "Interface": "接口",
    "interface": "接口",
    "Design": "设计",
    "design": "设计",
    "Architecture": "架构",
    "architecture": "架构",
    "Prototype": "原型",
    "prototype": "原型",
    "Debug": "调试",
    "debug": "debug",
    "Diagnose": "诊断",
    "diagnose": "诊断",
    "Triage": "分类",
    "triage": "分类",
    "Issue": "问题",
    "issue": "问题",
    "Issues": "问题",
    "issues": "问题",
    "Tracker": "跟踪器",
    "tracker": "跟踪器",
    "Label": "标签",
    "label": "标签",
    "Labels": "标签",
    "labels": "标签",
    "PRD": "PRD",
    "ADR": "ADR",
    "ADRs": "ADRs",
    "TDD": "TDD",
    "UI": "UI",
    "Logic": "逻辑",
    "logic": "逻辑",
}

def translate_line(line: str) -> str:
    """Translate a single line, preserving markdown formatting."""
    # Skip code blocks, links, and special markdown elements
    if line.strip().startswith('```') or line.strip().startswith('---'):
        return line
    
    # Preserve link syntax but translate text
    # This is a simplified approach - full translation would need more sophisticated handling
    
    result = line
    for en, zh in TRANSLATIONS.items():
        # Only replace whole words, not parts of words
        pattern = r'\b' + re.escape(en) + r'\b'
        result = re.sub(pattern, zh, result)
    
    return result

def process_file(input_path: Path, output_path: Path):
    """Process a single markdown file."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # For now, create a placeholder indicating this needs translation
        lines = content.split('\n')
        translated_lines = []
        
        in_code_block = False
        for line in lines:
            if '```' in line:
                in_code_block = not in_code_block
                translated_lines.append(line)
            elif in_code_block:
                translated_lines.append(line)
            else:
                translated_lines.append(translate_line(line))
        
        translated_content = '\n'.join(translated_lines)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"✓ Processed: {input_path.relative_to(Path('/workspace'))}")
        return True
    except Exception as e:
        print(f"✗ Error processing {input_path}: {e}")
        return False

def main():
    workspace = Path('/workspace')
    md_files = list(workspace.rglob('*.md'))
    
    # Filter out already translated files and node_modules
    files_to_translate = [
        f for f in md_files 
        if '_CN.md' not in str(f) and 'node_modules' not in str(f)
    ]
    
    print(f"Found {len(files_to_translate)} files to translate")
    
    success_count = 0
    for input_file in files_to_translate:
        # Generate output filename
        output_file = input_file.with_name(input_file.stem + '_CN.md')
        
        if process_file(input_file, output_file):
            success_count += 1
    
    print(f"\nCompleted: {success_count}/{len(files_to_translate)} files translated")

if __name__ == "__main__":
    main()
