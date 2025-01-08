import os
import ctypes
from ctypes import wintypes

class FontFixer:

    def __init__(self):
        self.system_font_path = os.path.join(os.environ['WINDIR'], 'Fonts')

    def list_fonts(self):
        """List all installed fonts."""
        fonts = [f for f in os.listdir(self.system_font_path) if f.endswith('.ttf') or f.endswith('.otf')]
        return fonts

    def verify_font_registry(self):
        """Verify font entries in the Windows registry."""
        try:
            reg_font_key = r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'
            reg = ctypes.windll.advapi32.RegOpenKeyExW
            reg.restype = wintypes.LONG
            reg_handle = wintypes.HANDLE()
            reg_err = reg(ctypes.windll.advapi32.HKEY_LOCAL_MACHINE, reg_font_key, 0, wintypes.KEY_READ, ctypes.byref(reg_handle))
            if reg_err == 0:
                ctypes.windll.advapi32.RegCloseKey(reg_handle)
                return "Registry check passed."
            else:
                return "Registry check failed."
        except Exception as e:
            return f"Error checking registry: {e}"

    def reinstall_font(self, font_name):
        """Reinstall a specified font."""
        try:
            font_path = os.path.join(self.system_font_path, font_name)
            if os.path.exists(font_path):
                ctypes.windll.gdi32.RemoveFontResourceW(font_path)
                ctypes.windll.gdi32.AddFontResourceW(font_path)
                ctypes.windll.user32.SendMessageTimeoutW(0xFFFF, 0x1D, 0, 0, 0, 1000)
                return f"{font_name} reinstalled successfully."
            else:
                return f"{font_name} not found in system font directory."
        except Exception as e:
            return f"Error reinstalling font: {e}"

    def fix_font_issues(self):
        """Fix common font issues."""
        try:
            fonts = self.list_fonts()
            for font in fonts:
                self.reinstall_font(font)
            return "Font issues fixed."
        except Exception as e:
            return f"Error fixing font issues: {e}"

if __name__ == "__main__":
    font_fixer = FontFixer()
    print("Listing available fonts:")
    print(font_fixer.list_fonts())
    print(font_fixer.verify_font_registry())
    print(font_fixer.fix_font_issues())