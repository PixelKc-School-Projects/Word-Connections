"""
Helper functions for Word Connections game.
Provides keyboard input handling with arrow key support.
"""

import sys

# Cross-platform single character input (no Enter required)
# Supports both WASD and arrow keys
if sys.platform == 'win32':
    import msvcrt
    
    def getch():
        """Get a single character from keyboard on Windows.
        Supports WASD and arrow keys.
        """
        key = msvcrt.getch()
        
        # Check for arrow keys (Windows sends \xe0 followed by direction)
        if key == b'\xe0':
            arrow = msvcrt.getch()
            if arrow == b'H':  # Up arrow
                return 'up'
            elif arrow == b'P':  # Down arrow
                return 'down'
            elif arrow == b'K':  # Left arrow
                return 'left'
            elif arrow == b'M':  # Right arrow
                return 'right'
        
        # Regular key
        try:
            return key.decode('utf-8').lower()
        except (UnicodeDecodeError, AttributeError):
            return key.decode('latin-1').lower()
else:
    import termios
    import tty
    
    def getch():
        """Get a single character from keyboard on Unix/Mac.
        Supports WASD and arrow keys.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            
            # Check for arrow keys (Unix/Mac sends escape sequence)
            if ch == '\x1b':  # ESC character
                # Read the next two characters
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                
                # Arrow keys send: \x1b[A (up), \x1b[B (down), \x1b[C (right), \x1b[D (left)
                # Or: \x1bOA, \x1bOB, \x1bOC, \x1bOD (application mode)
                if ch2 == '[':
                    if ch3 == 'A':  # Up arrow
                        return 'up'
                    elif ch3 == 'B':  # Down arrow
                        return 'down'
                    elif ch3 == 'C':  # Right arrow
                        return 'right'
                    elif ch3 == 'D':  # Left arrow
                        return 'left'
                elif ch2 == 'O':
                    if ch3 == 'A':  # Up arrow (application mode)
                        return 'up'
                    elif ch3 == 'B':  # Down arrow (application mode)
                        return 'down'
                    elif ch3 == 'C':  # Right arrow (application mode)
                        return 'right'
                    elif ch3 == 'D':  # Left arrow (application mode)
                        return 'left'
                
                # If it's not an arrow key, return the ESC character
                return ch.lower()
            
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


