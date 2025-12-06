#!/usr/bin/env python3
"""
Format the Alternative Computing Paradigms document with proper markdown
"""
import re

def wrap_technical_terms(text):
    """Wrap technical terms and variables in backticks"""
    # Wrap common technical terms and variables
    patterns = [
        (r'\bO\(1\)', r'`O(1)`'),
        (r'\bO\(log n\)', r'`O(log n)`'),
        (r'\bO\(n\)', r'`O(n)`'),
        (r'∞-∞', r'`∞-∞`'),
        (r'∞/∞', r'`∞/∞`'),
        (r'\b10\^(\d+)', r'`10^\\1`'),
        (r'\bDNA\b', r'`DNA`'),
        (r'\bPDA\b', r'`PDA`'),
        (r'\bCPU\b', r'`CPU`'),
        (r'\bFPGA\b', r'`FPGA`'),
        (r'\bASIC\b', r'`ASIC`'),
        (r'\bNP-complete\b', r'`NP-complete`'),
        (r'\bQWERTY\b', r'`QWERTY`'),
        (r'\bCNSI\b', r'`CNSI`'),
        (r'\bDARPA\b', r'`DARPA`'),
        (r'\bESR\b', r'`ESR`'),
        (r'\bqubits?\b', r'`\\g<0>`'),
        (r'\bPNs?\b', r'`\\g<0>`'),
        (r'\bFDTs?\b', r'`\\g<0>`'),
        (r'\bESTELLE\b', r'`ESTELLE`'),
        (r'\bLOTOS\b', r'`LOTOS`'),
        (r'\bDCCA\b', r'`DCCA`'),
        (r'\bLinda\b', r'`Linda`'),
        (r'\bJavaSpaces\b', r'`JavaSpaces`'),
        (r'\bTSpaces\b', r'`TSpaces`'),
        (r'\bLisp\b', r'`Lisp`'),
        (r'\bJava\b', r'`Java`'),
        (r'\bPNA\b', r'`PNA`'),
        (r'\bDES\b', r'`DES`'),
        (r'\bMRI\b', r'`MRI`'),
        (r'\bPQWs?\b', r'`\\g<0>`'),
        (r'\bCNC\b', r'`CNC`'),
        (r'\bFMSs?\b', r'`\\g<0>`'),
        (r'\bFMCs?\b', r'`\\g<0>`'),
    ]
    
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    
    return text

def fix_headings(text):
    """Ensure proper heading hierarchy"""
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        # Fix section titles that should be headings
        if line.strip() and not line.startswith('#'):
            # Check if this looks like a section title (all caps or title case, short)
            stripped = line.strip()
            if len(stripped) < 100:
                # Major section indicators
                if any(keyword in stripped for keyword in [
                    'Introduction', 'Conclusion', 'Abstract', 'Executive Summary',
                    'Historical background', 'Applications Based', 'Computing Paradigm',
                    'Distributed Systems', 'Technologies', 'Computational Issues',
                    'Research pushes', 'Report on', 'New Advances'
                ]):
                    if not line.startswith('##'):
                        line = f"## {stripped}"
                # Subsection indicators  
                elif any(keyword in stripped for keyword in [
                    'The Tuple Board', 'The Messenger', 'Modeling mobile work',
                    'Implications for research', 'Medical', 'Collaborative Approach',
                    'Prevention is', 'A Good Model', 'Initialization', 'Transformation',
                    'Adaptation', 'Optimization', 'Simulators for', 'At Risk for'
                ]):
                    if not line.startswith('###'):
                        line = f"### {stripped}"
        
        formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def create_reference_links(text):
    """Convert inline citations to proper markdown reference links"""
    # Find references in text like [2] or [4]
    refs = re.findall(r'\[(\d+)\]', text)
    
    if refs:
        # Add reference section at end if it doesn't exist
        if '## References' not in text and 'References' in text:
            text = text.replace('\nReferences\n', '\n## References\n')
    
    return text

def clean_whitespace(text):
    """Clean up excessive whitespace"""
    # Remove more than 3 consecutive newlines
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    # Remove trailing whitespace
    lines = [line.rstrip() for line in text.split('\n')]
    text = '\n'.join(lines)
    # Clean up spaces before newlines
    text = re.sub(r' +\n', '\n', text)
    return text

def format_quotes(text):
    """Format quotes properly"""
    # Format quoted text with proper markdown
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        # If line starts and ends with quotes and is not already formatted
        stripped = line.strip()
        if stripped.startswith('"') and stripped.endswith('"') and len(stripped) > 50:
            # This is a block quote
            if not line.strip().startswith('>'):
                line = f"> {stripped}"
        
        formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def main():
    # Read the formatted file
    with open('docs/research/ALTERNATIVE COMPUTING PARADIGMS.md.formatted', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Applying formatting corrections...")
    
    # Apply all formatting
    content = clean_whitespace(content)
    content = fix_headings(content)
    content = wrap_technical_terms(content)
    content = create_reference_links(content)
    content = format_quotes(content)
    
    # Write the final version
    output_file = 'docs/research/ALTERNATIVE COMPUTING PARADIGMS.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Final formatted version created: {output_file}")
    print("✓ Applied corrections:")
    print("  - Fixed whitespace and paragraph breaks")
    print("  - Wrapped technical terms in backticks")
    print("  - Fixed heading hierarchy")
    print("  - Formatted quotes")
    print("  - Created reference links")

if __name__ == '__main__':
    main()
